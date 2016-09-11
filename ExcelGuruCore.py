
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
    'start': ['Привет, {}! Меня зовут ExcelGuru и я сделаю тебя крутейшим чуваком в использовании Excel для интернет-маркетинга. С чего начнём?']
    ,'help' : ['Привет! Меня зовут ExcelGuru и я научу тебя решать задачи интернет-маркетинга с помощью Excel.\n\nЯ понимаю команды:\n/start - запустить меня\n/help - коротко обо мне\n/about - подробнее обо мне\n']
    ,'about' : ['Этот бот создан по мотивам специализированного курса “Excel для интернет-маркетинга”. Он предназначен для интернет-маркетологов, веб-аналитиков, руководителей или владельцев бизнеса, желающих научиться использовать все возможности Microsoft Excel\n\nФормат обучения такой:\n• существует рейтинг, в котором в любой момент времени ты можешь сравнить, насколько ты классный по сравнению с другими студентами (которые прошли столько же, сколько и ты)\n• ежедневно мы отправляем тебе небольшое задание, которое можно выполнить буквально на ходу. У тебя 1 день на выполнение за полный балл, дальше - дадим, но просто меньше. Не тормози\n• каждые 5 уроков я буду предлагать тебе добровольные тесты по сразу нескольким пройденным материалам. Так ты сможешь понять, что ты усвоил надолго, а что тебе стоит повторить\n• в любой момент времени, например, когда тебе это понадобится в твоих проектах, ты можешь написать мне вопрос, и я постараюсь тебе автоматически ответить, а если у меня не получится тебе ответить - тогда ты всегда можешь обсудить свои вопросы в нашем коммьюнити: @ExcelGuruCommunity или задать вопрос преподавателю: @maxim_uvarov\n\nhttp://needfordata.ru/excel']
    ,'learning1' : ['Отлично! Давай начнем. Для курса нам понадобится Excel 2013 или Excel 2016. В этом коротком видео я расскажу о том, как начать работу с Excel']
    ,'learning2' : ['Сегодня без видео. 2+2=4, понятненько? А продолжение мы ещё не написали :(']
    ,'guide': ['Этот бот создан по мотивам специализированного курса “Excel для интернет-маркетинга”. Он предназначен для интернет-маркетологов, веб-аналитиков, руководителей или владельцев бизнеса, желающих научиться использовать все возможности Microsoft Excel\n\nФормат обучения такой:\n• существует рейтинг, в котором в любой момент времени ты можешь сравнить, насколько ты классный по сравнению с другими студентами (которые прошли столько же, сколько и ты)\n• ежедневно мы отправляем тебе небольшое задание, которое можно выполнить буквально на ходу. У тебя 1 день на выполнение за полный балл, дальше - дадим, но просто меньше. Не тормози\n• каждые 5 уроков я буду предлагать тебе добровольные тесты по сразу нескольким пройденным материалам. Так ты сможешь понять, что ты усвоил надолго, а что тебе стоит повторить\n• в любой момент времени, например, когда тебе это понадобится в твоих проектах, ты можешь написать мне вопрос, и я постараюсь тебе автоматически ответить, а если у меня не получится тебе ответить - тогда ты всегда можешь обсудить свои вопросы в нашем коммьюнити: @ExcelGuruCommunity или задать вопрос преподавателю: @maxim_uvarov\n\nhttps://vimeo.com/181415903\nhttp://needfordata.ru/excel\n\nНачнём?']
    ,'overview': ['1st lesson', '2nd lesson', '3rd lesson', '4th lesson'] # внутри функции
    ,'progress': ['Твой прогресс по программе курса:\n'] # + внутри функции
    ,'quiz1': ['Пройди тест. Он короткий.']
}


# In[4]:

replies = {
    'start': [ [['Прочитать гайд'],['Начать обучение'],['Обзор уроков']] ]
    ,'help' : []
    ,'about' : []
    ,'learning1' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'learning2' :  [ [[]] ] # ещё не готово :(
    ,'guide' : [ [['Начать обучение'],['Обзор уроков']] ]
    ,'overview': [ [[]] ] # внутри функции
    ,'progress': [ [[]] ] # внутри функции
    ,'quiz1': [ [['Перепройти тест'],['Следующий урок']] ] # внутри функции
}


# In[5]:

class ExcelGuruCore:

    def __init__(self):
        self.file_user_data = 'user_data/user_data.pkl'
        self.file_user_quiz_data = 'user_data/quiz_data.pkl'
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
            
    # Получить из файла количество сданных 
    def get_progress(self, chat_id):
        return(['+++++_____ (50%)'])
            
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
        elif self.get_state(chat_id) == 'switch_quiz1': return(self.switch_quiz1(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz1_afterparty': return(self.switch_quiz1_afterparty(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning1': return(self.switch_learning1(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning2': return(self.switch_learning2(chat_id,txt))
        else: return(-1,-1)
    
    # команды
    
    def slash_start(self, chat_id,txt = '', user_name = ''):
        print(user_name)
        msgs = texts['start']
        msgs[0] = msgs[0].format(user_name)
        self.set_state(chat_id,'switch_start')
        return(msgs, replies['start'])

    def slash_help(self,chat_id,txt = ''):
        return(texts['help'],replies['help'])

    def slash_about(self,chat_id,txt = ''):
        return(texts['about'],replies['about'])

    def slash_progress(self,chat_id,txt = ''):
        progr = self.get_progress(chat_id)
        msgs = texts['progress']
        msgs[0] = msgs[0] + progr[0]
        buttons = replies['progress']
        print(msgs)
        return(msgs, buttons)

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
    
    def state_learning2(self,chat_id,txt):
        self.set_state(chat_id,'switch_learning2')
        msgs,bttns = self.slash_start(chat_id,txt)
        msgs = [texts['learning2'][0],msgs[0]]
        bttns = [[],bttns[0]]
        return(msgs,bttns)
    
    def state_quiz1(self,chat_id,txt):
        self.set_state(chat_id,'switch_quiz1')
        tf = self.quiz_data_read()
        tf = tf[((tf.chat_id != chat_id) | (tf.quiz_num!=1))]
        tf.to_pickle(self.file_user_quiz_data)
        return(texts['quiz1']+self.quizes[0][0][0],[[],self.quizes[0][1][0]])

    # quizes
    
    def quiz_data_read(self,chat_id=-1):
        t = pd.read_pickle(self.file_user_quiz_data)
        if chat_id == -1: return(t)
        else: return(t[(t.chat_id==chat_id)])
        
    def quiz_data_add(self,quiz_num,question_num,chat_id,answer):
        tf = self.quiz_data_read()
        # если есть ответ - обновить, нет - дописать
        if len(tf[(tf.quiz_num==quiz_num)&(tf.question_num==question_num)&(tf.chat_id==chat_id)])==0:
            tf = tf.append(pd.DataFrame([[quiz_num,question_num,chat_id,answer]],columns = tf.columns))
        else:
            tf.loc[(tf.chat_id == ch)&(t.quiz_num==quiz_num)&(t.question_num==question_num), 'answer'] = answer
        tf.to_pickle(self.file_user_quiz_data)
    
    def switch_quiz1(self,chat_id,txt):
        quiz = self.quizes[0]
        t = self.quiz_data_read(chat_id)
        num_answered = len(t[t.quiz_num==1])
        print('answered = '+str(num_answered))
        if num_answered<len(quiz[0]): # ещё не всё отвечено, до этого вопроса
            self.quiz_data_add(1,num_answered,chat_id,txt)
            if (num_answered+1)<len(quiz[0]): # не последний вопрос был?
                return(quiz[0][num_answered+1],[quiz[1][num_answered+1]])
            
        # подсчёт статистики
        print('we are counting stats')
        ans = self.quizes[0][2]
        resp = list(self.quiz_data_read(chat_id).answer)
        match = [ans[i]==resp[i] for i in range(len(ans))]
        stat = sum(match)
        msgs = []
        
        if stat == len(ans): msgs.append('Вау! 100%! Ты крут!')
        elif stat/len(ans) > 0.8: msgs.append('Есть ошибочки, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0.4: msgs.append('Такооое, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0: msgs.append('Оч плохо, '+str(stat)+'/'+str(len(ans)))
        else: msgs.append('Тебе стоит усерднее заниматься, '+str(stat)+'/'+str(len(ans)))

        if not match[0]: msgs.append('Стоит повторить урок 1\nhttps://vimeo.com/164435024')
        if not match[1]: msgs.append('Стоит повторить урок 2\nhttps://vimeo.com/152878376')
        
        ret = []
        for i in msgs: ret.append([[]])
        ret[-1] = replies['quiz1'][0]
        
        self.set_state(chat_id,'switch_quiz1_afterparty')
        
        # генерация ссылок для повторения
        return(msgs,ret) # если всё отвечено теперь или было изначально
       
    def switch_quiz1_afterparty(self,chat_id,txt):
        if txt == self.unlist(replies['quiz1'][0])[0]: #rerun quiz1
            return(self.state_quiz1(chat_id,txt))
        elif txt == self.unlist(replies['quiz1'][0])[1]: #lesson2
            return(self.state_learning2(chat_id,txt))
        else:
            return([self.ku],replies['quiz1'])
        
        
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

