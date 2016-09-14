
# coding: utf-8
# ### Библиотечки

# In[1]:

from sys import exc_info# для выдачи ошибок
from time import strftime # для логгирования
from os import environ # для TG_TOKEN
from random import randint


# In[2]:

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,RegexHandler # для работы бота в целом
from telegram import ReplyKeyboardMarkup,ReplyKeyboardHide,ReplyMarkup # для инлайновой клавиатуры


# ### Грузим класс, выполняющий ядро бота

# In[3]:

from ExcelGuruCore import *
eg = ExcelGuruCore()


# ### Именно телеграм

# In[4]:

def send_reply(bot, chat_id, msgs, buttons):
    print(buttons)
    for i in range(len(msgs)):
        if i < len(buttons) and len(buttons[i]) > 0 and len(buttons[i][0]) > 0:
            bot.sendMessage(chat_id=chat_id, text = msgs[i], reply_markup=ReplyKeyboardMarkup(buttons[i], one_time_keyboard=True))
        else:
            bot.sendMessage(chat_id=chat_id, text = msgs[i])


# In[5]:

def slash_help(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_help(chat_id)
    send_reply(bot, chat_id, msgs, buttons)


# In[6]:

def slash_about(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_about(chat_id)
    send_reply(bot, chat_id, msgs, buttons)


# In[7]:

def slash_progress(bot, update):
    chat_id = update.message.chat_id
    msgs,buttons = eg.slash_progress(chat_id)
    send_reply(bot, chat_id, msgs, buttons)


# In[8]:

def slash_start(bot, update):
    txt = update.message.text
    chat_id = update.message.chat_id
    user_name = update.message.from_user.first_name
    msgs,buttons = eg.slash_start(chat_id, txt, user_name)
    bot.sendDocument(chat_id=update.message.chat_id,document = 'BQADAgADUQADcPUPAh6EVwjy6aIEAg')
    send_reply(bot, chat_id, msgs, buttons)


# In[9]:

def inside_idle(bot,update,txt=-1,chat_id=-1):
    if txt == -1:
        txt = update.message.text
    if chat_id == -1:
        chat_id = update.message.chat_id
    try:
        msgs,buttons = eg.process_txt(chat_id,txt)
        
        # отладка
        print('### got: '+txt)
        print('state: ' + eg.get_state(chat_id))
        print(msgs)
        print(buttons)

        # если всё плохо
        # если нет подходящего стейта
        if msgs == -1:
            bot.sendMessage(chat_id=chat_id, text = "Произошла внутренняя ошибка. Приношу свои извенения. Пройдите в интересующий пункт меню")
            eg.slash_start(bot,update)
            return(0)
        
        if msgs[0] == eg.ku and len(msgs)==1:
            resp = faq(bot, update,txt,chat_id)
            if resp == 0: return(0)
            else: pass
        
        send_reply(bot, chat_id, msgs, buttons)
    except:
        print("Unexpected error:" + str(sys.exc_info()[0]))
        bot.sendMessage(chat_id=chat_id, text = "Произошла внутренняя ошибка. Приношу свои извенения. Пройдите в интересующий пункт меню")
        eg.slash_start(bot,update)
        return(0)


# In[10]:

def idle_main(bot, update):
    print(update.message.from_user)
    inside_idle(bot,update)


# In[11]:

def idle_doc(bot, update):
    try:
        doc = update.message.document
    except:
        print('Не смог получить файл')
    try:
        print(doc)
    except:
        print('Не смог напечатать файл')
    
    resp = ['Спасибо, обязательно ознакомлюсь','Ммм, документики','Это что за покемон?','А скан паспорта не пришлёшь?','Нажимай лучше на мои кнопки','Ладно, можешь хранить здесь свои файлы, не буду удалять','Ладно, можешь хранить здесь свои файлы, не буду удалять','Ладно, можешь хранить здесь свои файлы, не буду удалять']
    r = randint(1,len(resp))
    bot.sendMessage(chat_id = update.message.chat_id, text = resp[r-1])
    
    try:
        bot.sendDocument(chat_id=update.message.chat_id,document = 'BQADAgADUQADcPUPAh6EVwjy6aIEAg')
    except:
        print('не смог отравить BQADAgADUQADcPUPAh6EVwjy6aIEAg')


# In[12]:

def slash_faq(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text = 'Ты всегда можешь просто отправить мне текстовое сообщение о том, что тебе интересно. На данный момент перечень доступных тем выглядит так:\n🔸 Полный перечень горячих клавиш Excel\n🔸 Фиксация ширины столбцов в сводных таблицах.\n\nТакже ты всегда можешь обратиться с вопросом в наше коммьюнити, https://telegram.me/ExcelGuruCommunity, или прямо к преподавателю @maxim_uvarov')


# In[13]:

def slash_rating(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text = '*Здесь будет рейтинг по когортам прохождения*')


# In[14]:

def faq(bot, update,txt=-1,chat_id=-1):
    if txt == -1:
        txt = update.message.text
    if chat_id == -1:
        chat_id = update.message.chat_id
        
    txt = txt.lower()
    
    if 'клавиш' in txt or 'горячие' in txt or 'hot' in txt or 'key' in txt or 'клавиа' in txt:
        bot.sendMessage(chat_id=chat_id, text = 'Полный перечень горячих клавиш Excel')       
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADj6gxG3D1DwIrIbXFE6HmvOcGcQ0ABBfWYkGS7LQWwNUBAAEC', caption = 'Полный перечень горячих клавиш Excel, 1/6')
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADkKgxG3D1DwJLXq1rtpaciSkdcQ0ABLBgf1FysKmErdYBAAEC', caption = 'Полный перечень горячих клавиш Excel, 2/6')
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADkagxG3D1DwJPO1q63c9INKzWgQ0ABFiPBiIBfSn04WIAAgI', caption = 'Полный перечень горячих клавиш Excel, 3/6')
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADkqgxG3D1DwJZyA5B8BTVn5TigQ0ABGkv5MiplXQSUGYAAgI', caption = 'Полный перечень горячих клавиш Excel, 4/6')
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADk6gxG3D1DwIY6dL9yL_hQrLigQ0ABMQ4ku7Dc580P2UAAgI', caption = 'Полный перечень горячих клавиш Excel, 5/6')
        bot.sendPhoto(chat_id=update.message.chat_id,photo = 'AgADAgADlKgxG3D1DwKEuEfYIMEgcYkCcQ0ABC2dCFX6S9Vv5doBAAEC', caption = 'Полный перечень горячих клавиш Excel, 6/6')
        return(0)
    
    docs2send = []
    words2send = []
    
    if ('сводн' in txt or 'pivot' in txt) and ('ширин' in txt or 'столб' in txt):
        words2send.append('Фиксация ширины столбцов в сводных таблицах')            
        docs2send.append('BQADAgADbAADcPUPApNUYKoC-IrCAg')
    
    if ('сводн' in txt or 'pivot' in txt) and ('вычислим' in txt or 'пол' in txt or 'формул' in txt):
        words2send.append('Создание вычисляемых полей в сводных таблицах')
        docs2send.append('BQADAgADawADcPUPAqMTguRU1oWjAg')
    
    if len(docs2send)==0 and ('сводн' in txt or 'pivot' in txt):
        words2send.append('Фиксация ширины столбцов в сводных таблицах')
        docs2send.append('BQADAgADbAADcPUPApNUYKoC-IrCAg')
        words2send.append('Создание вычисляемых полей в сводных таблицах')
        docs2send.append('BQADAgADawADcPUPAqMTguRU1oWjAg')
    
    for i in range(len(docs2send)):
        #bot.sendMessage(chat_id=chat_id, text = words2send[i])
        bot.sendDocument(chat_id=chat_id,document = docs2send[i],caption = words2send[i])
    
    if len(docs2send)>0: return(0)
    
    return(-1)


# In[15]:

def idle_pic(bot, update):
    try:
        photo = update.message.photo
    except:
        print('Не смог получить файл')
    try:
        print(photo[-1])
    except:
        print('Не смог напечатать файл')
    
    resp = ['Спасибо, обязательно посмотрю позже','Ммм, фоточки','Это что за покемон?','А скан паспорта не пришлёшь?','Нажимай лучше на мои кнопки','Ладно, можешь хранить здесь свои файлы, не буду удалять','Ладно, можешь хранить здесь свои файлы, не буду удалять','Ладно, можешь хранить здесь свои фотки, не буду удалять']
    r = randint(1,len(resp))
    bot.sendMessage(chat_id = update.message.chat_id, text = resp[r-1])


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
    dp.add_handler(CommandHandler("faq", slash_faq),group=0)
    dp.add_handler(CommandHandler("rating", slash_rating),group=0)
    
    # on noncommand message
    dp.add_handler(MessageHandler([Filters.text], idle_main))
    dp.add_handler(MessageHandler([Filters.document], idle_doc))
    dp.add_handler(MessageHandler([Filters.photo], idle_pic))

    # Start the Bot
    updater.start_polling()

    # Run the bot
    updater.idle()


# ### Запускаем!

# In[ ]:

if __name__ == '__main__':
    main()

