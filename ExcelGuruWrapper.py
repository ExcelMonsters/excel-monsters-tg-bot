
# coding: utf-8

# ### Библиотечки

# In[ ]:

from sys import exc_info# для выдачи ошибок
from time import strftime # для логгирования
from os import environ # для TG_TOKEN


# In[ ]:

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,RegexHandler # для работы бота в целом
from telegram import ReplyKeyboardMarkup,ReplyKeyboardHide,ReplyMarkup # для инлайновой клавиатуры


# ### Грузим класс, выполняющий ядро бота

# In[ ]:

from ExcelGuruCore import *


# In[ ]:

eg = ExcelGuruCore()


# ### Создаём дополнительные функции

# Функция, которая разбивает превашающие лимит размера сообщения телеграма на блоки

# In[ ]:

def split_msg(txt):
    if len(txt)<4095: return([txt])
    
    l = txt.split('\n')
    for p in l:
        if len(p)>4095:
            return(-1) #impossible then
        #may go into each p > 4095, change in loop there every last " " to "\n"
        #for poems may split firstly by "\n\n", only then inside by "\n", "."," "
    
    s = 0
    for i in range(1,len(l)):
        t = "\n".join(l[:i])
        if len(t)>4095:
            s = i
            break
    s = s-1        
    
    resp = "\n".join(l[:s])
    left = "\n".join(l[s:])
    if len(left)<4096: return([resp,left])
    else: return([rest]+split_msg(left))


# ### Именно телеграм

# In[ ]:
def send_reply(bot, chat_id, msgs, buttons):
    print(buttons)
    for i in range(len(msgs)):
        if i < len(buttons) and len(buttons[i]) > 0 and len(buttons[i][0]) > 0:
            bot.sendMessage(chat_id=chat_id, text = msgs[i], reply_markup=ReplyKeyboardMarkup(buttons[i], one_time_keyboard=True))
        else:
            bot.sendMessage(chat_id=chat_id, text = msgs[i])

def slash_help(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_help(chat_id)
    send_reply(bot, chat_id, msgs, buttons)

def slash_about(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_about(chat_id)
    send_reply(bot, chat_id, msgs, buttons)

def slash_progress(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_progress(chat_id)
    send_reply(bot, chat_id, msgs, buttons)

# In[ ]:

def slash_start(bot, update):
    txt = update.message.text
    chat_id = update.message.chat_id
    user_name = update.message.from_user.first_name
    msgs,buttons = eg.slash_start(chat_id, txt, user_name)
    send_reply(bot, chat_id, msgs, buttons)


# In[ ]:

def inside_idle(bot,update,txt=-1,chat_id=-1):
    if txt == -1:
        txt = update.message.text
    if chat_id == -1:
        chat_id = update.message.chat_id
    try:
        msgs,buttons = eg.process_txt(chat_id,txt)
        print('### got: '+txt)
        print('state: ' + eg.get_state(chat_id))
        print(msgs)
        print(buttons)
        if msgs == -1:
            bot.sendMessage(chat_id=chat_id, text = "smth wrong with states")
            return(0)
        send_reply(bot, chat_id, msgs, buttons)
        # for i in range(len(msgs)):
        #     if i < len(buttons) and len(buttons[i]) > 0 and len(buttons[i][0]) > 0:
        #         bot.sendMessage(chat_id=chat_id, text = msgs[i], reply_markup=ReplyKeyboardMarkup(buttons[i], one_time_keyboard=True))
        #     else:
        #         bot.sendMessage(chat_id=chat_id, text = msgs[i])
    except:
        bot.sendMessage(chat_id=chat_id, text = "Unexpected error:" + str(sys.exc_info()[0]))


# In[ ]:

def idle_main(bot, update):
    inside_idle(bot,update)


# In[ ]:
tg_token = environ['TG_TOKEN']

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(tg_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", slash_start),group=0)
    dp.add_handler(CommandHandler("help", slash_help),group=0)
    dp.add_handler(CommandHandler("about", slash_about),group=0)
    dp.add_handler(CommandHandler("progress", slash_progress),group=0)
    
    # on noncommand message
    dp.add_handler(MessageHandler([Filters.text], idle_main))

    # Start the Bot
    updater.start_polling()

    # Run the bot
    updater.idle()


# ### Запускаем!

# In[ ]:

if __name__ == '__main__':
    main()


# In[ ]:



