
# coding: utf-8

# In[1]:



import pandas as pd
from pandas import read_excel,read_pickle
from jellyfish import damerau_levenshtein_distance
from re import findall


# In[2]:

texts = {
    'start': ['Это бот по мотивам специализированного курса “Excel для интернет - маркетинга”. Он предназначен для интернет - маркетологов, веб-аналитиков, руководителей или владельцев бизнеса желающих научиться использовать все возможности Microsoft Excel for Windows.\n\nПосле начала курса мы попросим тебя установить время для рассылки уведомлений о курсе. И ежедневно мы будем присылать тебе. Новые уроки открываются по расписанию при наличии выполненных домашних заданий от тебя. О невыполненных домашних заданиях мы тебе будем напоминать, но лучше не злоупотребляй - чем быстрее ты выполняешь домашние задания, тем больше очков ты получаешь.\n\nhttps://vimeo.com/181415903\n\nВыбирай мудро.']
    'start_learning' : ['Отлично! Давай начнем. Для курса нам понадобится Excel 2013 или Excel 2016. В этом коротком видео я расскажу о том, как начать работу с Excel']
}


# In[3]:

replies = {
    'start': [ [['Начать обучение'],['Все уроки']] ]
    'start_learning' : [ [['Отлично, готов к квизу'],['Вопрос преподавателю'],['Оглавление уроков']] ]
}


# In[4]:

class ExcelGuruCore:

    def __init__(self):
        self.file_user_data = 'user_data/user_data.pkl'
        self.texts = texts
        self.replies = replies
        
    # внутренние функции  
        
        
    def get_state(self,chat_id):
        user_data = pd.read_pickle(self.file_user_data)
        t = user_data[user_data.chat_id == chat_id]
        if len(t.values)>=1: return(t.iloc[0][1])
        else: return('')
        
    def set_state(self,chat_id,state):
        user_data = pd.read_pickle(self.file_user_data)
        if len(user_data[user_data.chat_id == chat_id].values)>=1:
            user_data.loc[user_data.chat_id == chat_id, 'state'] = state
            user_data.to_pickle(self.file_user_data)
            return(0)
        else:
            user_data = user_data.append(pd.DataFrame([[chat_id,state]],columns = ['chat_id', 'state']))
            user_data.to_pickle(self.file_user_data)
            return(0)
            
            
    def debug(self,t):
        messages,reply_keyboard = t
        for i in range(len(messages)):
            print('Msg #'+str(i+1)+'/'+str(len(messages)))
            print(messages[i])
            for j in reply_keyboard[i]: print(j)
            print('')
    
    # для запросов извне
    
    def process_txt(self,chat_id,txt=''):
        if self.get_state(chat_id) == '': return(self.slash_start(chat_id))
        elif self.get_state(chat_id) == 'switch_guide_or_overview': return(self.switch_guide_or_overview(chat_id,txt))
        else: return(-1,-1)
    
    # состояния и команды
    
    def slash_start(self,chat_id,txt = ''):
        messages = texts['start']
        reply_keyboard = replies['start']
        self.set_state(chat_id,'switch_guide_or_overview')
        
        return(messages,reply_keyboard)
    
    def switch_guide_or_overview(self,chat_id,txt):
        if txt == 'Все уроки': #or smth else
            return(self.state_start_guide(chat_id,txt))
        elif txt == 'Начать обучение':
            return(self.state_overview(chat_id,txt))
        else:
            return(['Ничего не понял :('],[[[]]])
            
    
    def state_start_guide(self,chat_id,txt):
        state = ''
        messages = []
        reply_keyboard = []
        
        if txt == 'Расскажи': # другие варианты ответа
            msg = 'Ае! Обожаю рассказывать. Если надоест - нажми /skip, и мы начнём заниматься.'
            messages.append()
            reply_keyboard.append([[[]]])
            state = 'guide0'
        elif txt == 'Давай начнём': # другие варианты ответа
            messages.append('Хорошо, но если ты захочешь всё же ознакомиться - нажми /start. А сейчас я расскажу о плане курса.')
            reply_keyboard.append([[[]]])
            state = 'overview'
        else: # непонятненько
            messages.append('К сожалению, я ничего не понял :( Пожалуйста, используй кнопки, я их сделал, чтобы ты мог быстрее со мной общаться')
            reply_keyboard.append([[[]]])
        
        return(state,messages,reply_keyboard)
    
    def state_overview(self,chat_id,txt):
        messages = []
        reply_keyboard = []
        state = ''
        
        messages.append(txt_overview)
        reply_keyboard.append([[['Приступить к обучению'],['Более подробная информация о уроках']]])        
        state = 'learning_or_more_info'
        
        return(state,messages,reply_keyboard)
    
    def state_learning_or_more_info(self,chat_id,txt):
        messages = []
        reply_keyboard = []
        state = ''
        
        messages.append(txt_overview)
        reply_keyboard.append([[['Приступить к обучению'],['Более подробная информация о уроках']]])        
        state = 'start_learning_or_more_info'
        
        return(state,messages,reply_keyboard)

