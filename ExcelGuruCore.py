
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:

quiz1 = [
    [
        ['Каким способом можно добавить кнопки в панель быстрого запуска?\n\nА. перетащив необходимую кнопку в панель быстрого запуска\nБ. Нажав правую кнопку на интересующей кнопке и выбрать пункт отправить на ***\nВ. Позвонить маме']
        ,['Какое слово съела корова?']
    ]
    ,[
        [['А','Б','В']]
        ,[['Первое'],['Второе']]
    ]
    ,['А','Первое']
    ]


# In[3]:

texts = {
    'start': ['Привет! Меня зовут ExcelGuru и я сделаю тебя крутейшим чуваком в использовании Excel для интернет-маркетинга. С чего начнём?']
    ,'learning1' : ['Отлично! Давай начнем. Для курса нам понадобится Excel 2013 или Excel 2016. В этом коротком видео я расскажу о том, как начать работу с Excel']
    ,'guide': ['Этот бот создан по мотивам специализированного курса “Excel для интернет-маркетинга”. Он предназначен для интернет-маркетологов, веб-аналитиков, руководителей или владельцев бизнеса, желающих научиться использовать все возможности Microsoft Excel\n\nФормат обучения такой:\n• существует рейтинг, в котором в любой момент времени ты можешь сравнить, насколько ты классный по сравнению с другими студентами (которые прошли столько же, сколько и ты)\n• ежедневно мы отправляем тебе небольшое задание, которое можно выполнить буквально на ходу. У тебя 1 день на выполнение за полный балл, дальше - дадим, но просто меньше. Не тормози\n• каждые 5 уроков я буду предлагать тебе добровольные тесты по сразу нескольким пройденным материалам. Так ты сможешь понять, что ты усвоил надолго, а что тебе стоит повторить\n• в любой момент времени, например, когда тебе это понадобится в твоих проектах, ты можешь написать мне вопрос, и я постараюсь тебе автоматически ответить, а если у меня не получится тебе ответить - тогда ты всегда можешь обсудить свои вопросы в нашем коммьюнити: @ExcelGuruCommunity или задать вопрос преподавателю: @maxim_uvarov\n\nhttps://vimeo.com/181415903\nhttp://needfordata.ru/excel\n\nНачнём?']
    ,'overview': [''] # внутри функции
}


# In[4]:

replies = {
    'start': [ [['Прочитать гайд'],['Начать обучение'],['Обзор уроков']] ]
    ,'learning1' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'guide' : [ [['Начать обучение'],['Обзор уроков']] ]
    ,'overview': [ [[]] ] # внутри функции
}


# In[5]:

class ExcelGuruCore:

    def __init__(self):
        self.file_user_data = 'user_data/user_data.pkl'
        self.texts = texts
        self.replies = replies
        self.ku = 'Ничего не найдено :('
        self.quizes = [quiz1]
        
    # внутренние функции  
    
    def unlist(self,l): return([item for sublist in l for item in sublist])
        
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
        elif self.get_state(chat_id) == 'switch_start': return(self.switch_start(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_guide': return(self.switch_guide(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning1': return(self.switch_learning1(chat_id,txt))
        else: return(-1,-1)
    
    # команды
    
    def slash_start(self,chat_id,txt = ''):
        self.set_state(chat_id,'switch_start')
        return(texts['start'],replies['start'])
            
    # состояния

    def state_guide(self,chat_id,txt):
        self.set_state(chat_id,'switch_guide')
        return(texts['guide'],replies['guide'])
    
    def state_overview(self,chat_id,txt):
        self.set_state(chat_id,'switch_overview')
        return(texts['overview'],replies['overview'])
    
    def state_learning1(self,chat_id,txt):
        self.set_state(chat_id,'switch_learning1')
        return(texts['learning1'],replies['learning1'])
    
    def state_quiz1(self,chat_id,txt):
        self.set_state(chat_id,'switch_quiz1')
        return(texts['quiz1'],replies['quiz1'])

    # разветвления после разных состояний (1 состояние = 1 разветвление)
    
    def switch_start(self,chat_id,txt):
        if txt == self.unlist(replies['start'][0])[0]: #guide
            return(self.state_guide(chat_id,txt))
        elif txt == self.unlist(replies['start'][0])[1]: #learning
            return(self.state_learning1(chat_id,txt))
        elif txt == self.unlist(replies['start'][0])[2]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['start'])

    def switch_guide(self,chat_id,txt):
        if txt == self.unlist(replies['guide'][0])[0]: #learning
            return(self.state_learning1(chat_id,txt))
        elif txt == self.unlist(replies['guide'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['guide'])

    def switch_learning1(self,chat_id,txt):
        if txt == self.unlist(replies['learning1'][0])[0]: #quiz
            return(self.state_quiz1(chat_id,txt))
        elif txt == self.unlist(replies['learning1'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['learning1'])

