
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:

quiz1 = [
    [
        ['Почему мы не выгружаем метрики из Яндекс.Директ о CTR и стоимости клика для анализа данных в сводных таблицах?\n\nА. В статистике Яндекс.Директ нет возможности выгружать более 12 столбцов\nБ. CTR и Стоимость клика не информативные метрики для контекстной рекламы, а следовательно их надо исключить из анализа\nВ. Эти метрики корректно рассчитывать в сводной таблице на основе абсолютных значений о расходе и количестве кликов']
        ,['Какие метрики из перечисленных ниже являются абсолютными?\n\nА. CTR\nБ. Коэффициент конверсии\nВ. Доход']
    ]
    ,[
        [['А','Б','В']]
        ,[['А','Б','В']]
    ]
    ,['В','В']
    ]


# In[3]:

quiz2 = [
    [
        ['Почему ширина столбцов в сводной таблице постоянно изменяется при её обновлении?\n\nА. Это поведение Excel по умолчанию. Чтобы такого не происходило - в настройках сводной таблицы нужно снять галку в специальном поле\nБ. В настройках Excel выбран язык отличный от языка системы по умолчанию\nВ. Это говорит о том, что включено классическое представление сводных таблиц']
    ]
    ,[
        [['А','Б','В']]
    ]
    ,['А']
    ]


# In[4]:

quiz3 = [
    [
        ['Можно ли при помощи сводной таблицы быстро найти рекламные кампании, которые потратили 80% денег?\n\nА. Нет, нельзя. Для этого необходимо пользоваться функционалом классических фильтров Excel\nБ. Да, можно, при помощи создания вычисляемого поля\nВ. Да, можно, при помощи дополнительных операций вычисления']
    ]
    ,[
        [['А','Б','В']]
    ]
        ,['В']
    ]


# In[5]:

quiz4 = [
    [
        ['Согласно просмотренному видео скажите, как отличается стоимость заказа у посетителей старше 35 лет\n\nА. Стоимость заказа отличается незначительно\nБ. Стоимость заказа существенно ниже, нужно повышать ставки\nВ. Стоимость заказа существенно выше, нужно понижать ставки на этих пользователей']
    ]
    ,[
        [['А','Б','В']]
    ]
        ,['В']
    ]


# In[6]:

texts = {
    'start': ['Привет, {}! Меня зовут ExcelGuru и я сделаю тебя крутейшим спецом в использовании Excel для интернет-маркетинга. С чего начнём?']
    ,'help' : ['Привет! Меня зовут ExcelGuru и я научу тебя решать задачи интернет-маркетинга с помощью Excel.\n\nЯ понимаю команды:\n/start - запустить меня\n/help - коротко обо мне\n/about - подробнее обо мне\n']
    ,'about' : ['Этот бот создан по мотивам специализированного курса “Excel для интернет-маркетинга”. Он предназначен для интернет-маркетологов, веб-аналитиков, руководителей или владельцев бизнеса, желающих научиться использовать все возможности Microsoft Excel\n\nФормат обучения такой:\n• существует рейтинг, в котором в любой момент времени ты можешь сравнить, насколько ты классный по сравнению с другими студентами (которые прошли столько же, сколько и ты)\n• ежедневно мы отправляем тебе небольшое задание, которое можно выполнить буквально на ходу. У тебя 1 день на выполнение за полный балл, дальше - дадим, но просто меньше. Не тормози\n• каждые 5 уроков я буду предлагать тебе добровольные тесты по сразу нескольким пройденным материалам. Так ты сможешь понять, что ты усвоил надолго, а что тебе стоит повторить\n• в любой момент времени, например, когда тебе это понадобится в твоих проектах, ты можешь написать мне вопрос, и я постараюсь тебе автоматически ответить, а если у меня не получится тебе ответить - тогда ты всегда можешь обсудить свои вопросы в нашем коммьюнити: @ExcelGuruCommunity или задать вопрос преподавателю: @maxim_uvarov\n\nhttp://needfordata.ru/excel']
    ,'learning1' : ['Выгрузка данных для анализа из Яндекс.Директ\n\nhttps://vimeo.com/182268195']
    ,'learning2' : ['Создание сводной таблицы\n\nhttps://vimeo.com/182268912']
    ,'learning3' : ['Дополнительные операции (процент по столбцу, доля нарастающим итогом), использование принципа Паретто\n\nhttps://vimeo.com/182270833']
    ,'learning4' : ['Анализ статистики эффективности контекстной рекламы по демографическим факторам\n\nhttps://vimeo.com/182269395']
    ,'guide': ['Этот бот создан по мотивам специализированного курса “Excel для интернет-маркетинга”. Он предназначен для интернет-маркетологов, веб-аналитиков, руководителей или владельцев бизнеса, желающих научиться использовать все возможности Microsoft Excel\n\nФормат обучения такой:\n• существует рейтинг, в котором в любой момент времени ты можешь сравнить, насколько ты классный по сравнению с другими студентами (которые прошли столько же, сколько и ты)\n• ежедневно мы отправляем тебе небольшое задание, которое можно выполнить буквально на ходу. У тебя 1 день на выполнение за полный балл, дальше - дадим, но просто меньше. Не тормози\n• каждые 5 уроков я буду предлагать тебе добровольные тесты по сразу нескольким пройденным материалам. Так ты сможешь понять, что ты усвоил надолго, а что тебе стоит повторить\n• в любой момент времени, например, когда тебе это понадобится в твоих проектах, ты можешь написать мне вопрос, и я постараюсь тебе автоматически ответить, а если у меня не получится тебе ответить - тогда ты всегда можешь обсудить свои вопросы в нашем коммьюнити: @ExcelGuruCommunity или задать вопрос преподавателю: @maxim_uvarov\n\nhttps://vimeo.com/181415903\nhttp://needfordata.ru/excel\n\nНачнём?']
    ,'overview': [] # меняется локальная копия при инициализации класса
    ,'progress': ['Твой прогресс по программе курса:\n'] # + внутри функции
    ,'quiz1': ['Приступим к первому тесту. В нём мы проверим, насколько ты усвоил полученные в видео знания']
    ,'quiz2': ['Второй тест. Ну-ка']
    ,'quiz3': ['Тест #3']
    ,'quiz4': ['Starting test #4']
    ,'final': ['Спасибо вам за то, что прошли наш мини-курс по оценке кампаний Яндекс.Директ при помощи Excel. Надеемся, вы нашли для себя в нем что-то новое.\n\nЭтот курс был снять за 1 ночь и выложен в бота, который был запрограммирован за 1 ночь, ожидайте обновлений. Если вам интересно изучение Excel для интернет-маркетинга - обращайтесь к Максим Уваров в needfordata.ru/excel или здесь: @maxim_uvarov']
}


# In[7]:

replies = {
    'start': [ [['Прочитать гайд'],['Начать обучение'],['Обзор уроков']] ]
    ,'help' : []
    ,'about' : []
    ,'learning1' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'learning2' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'learning3' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'learning4' : [ [['Отлично, готов к quiz'],['Обзор уроков']] ]
    ,'guide' : [ [['Начать обучение'],['Обзор уроков']] ]
    ,'overview': [ [[]] ] # внутри функции
    ,'progress': [ [[]] ] # внутри функции
    ,'quiz1': [ [['Перепройти тест'],['Следующий урок']] ] # внутри функции
    ,'quiz2': [ [['Перепройти тест'],['Следующий урок']] ] # внутри функции
    ,'quiz3': [ [['Перепройти тест'],['Следующий урок']] ] # внутри функции
    ,'quiz4': [ [['Перепройти тест'],['Следующий урок']] ] # внутри функции
}


# In[1]:

class ExcelGuruCore:

    def __init__(self):
        self.file_user_data = 'user_data/user_data.pkl'
        self.file_user_quiz_data = 'user_data/quiz_data.pkl'
        self.texts = texts
        self.replies = replies
        self.texts['overview'] = [texts['learning1'][0],texts['learning2'][0],texts['learning3'][0],texts['learning4'][0]]
        self.ku = 'Ничего не найдено :('
        self.quizes = [quiz1,quiz2,quiz3,quiz4]
        
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
        past = 0
        resp = list(self.quiz_data_read(chat_id).quiz_num)
        if len(resp) > 0: 
            past = max(resp)
        progress = 100 * past / len(self.quizes)
        return(['{}%'.format(progress)])
            
   
    # для запросов извне
    
    def process_txt(self,chat_id,txt=''):
        if self.get_state(chat_id) == '': return(self.slash_start(chat_id))
        elif self.get_state(chat_id) == 'switch_start': return(self.switch_start(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_guide': return(self.switch_guide(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz1': return(self.switch_quiz1(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz1_afterparty': return(self.switch_quiz1_afterparty(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz2': return(self.switch_quiz2(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz2_afterparty': return(self.switch_quiz2_afterparty(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz3': return(self.switch_quiz3(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz3_afterparty': return(self.switch_quiz3_afterparty(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz4': return(self.switch_quiz4(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_quiz4_afterparty': return(self.switch_quiz4_afterparty(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning1': return(self.switch_learning1(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning2': return(self.switch_learning2(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning3': return(self.switch_learning3(chat_id,txt))
        elif self.get_state(chat_id) == 'switch_learning4': return(self.switch_learning4(chat_id,txt))
        else: return(-1,-1)
    
    # команды
    
    def slash_start(self, chat_id,txt = '', user_name = ''):
        self.set_state(chat_id,'switch_start')
        msgs = texts['start'][:]
        msgs[0] = msgs[0].format(user_name)
        return(msgs, replies['start'])

    def slash_help(self,chat_id,txt = ''):
        return(texts['help'],replies['help'])

    def slash_about(self,chat_id,txt = ''):
        return(texts['about'],replies['about'])

    def slash_progress(self,chat_id,txt = ''):
        progr = self.get_progress(chat_id)
        msgs = texts['progress'][:] # по значению
        msgs[0] = msgs[0] + progr[0]
        buttons = replies['progress']
        print(msgs)
        return(msgs, buttons)

    # состояния

    def state_guide(self,chat_id,txt):
        self.set_state(chat_id,'switch_guide')
        return(texts['guide'],replies['guide'])
    
    def state_overview(self,chat_id,txt):
        print('state_overview')
        return(texts['overview'],replies['overview'])
    
    def state_learning1(self,chat_id,txt):
        print('state_learning1')
        self.set_state(chat_id,'switch_learning1')
        return(texts['learning1'],replies['learning1'])
    
    def state_learning2(self,chat_id,txt):
        print('state_learning2')
        self.set_state(chat_id,'switch_learning2')
        return(texts['learning2'],replies['learning2'])
    
    def state_learning3(self,chat_id,txt):
        print('state_learning3')
        self.set_state(chat_id,'switch_learning3')
        return(texts['learning3'],replies['learning3'])
    
    def state_learning4(self,chat_id,txt):
        print('state_learning4')
        self.set_state(chat_id,'switch_learning4')
        return(texts['learning4'],replies['learning4'])
    
    def state_quiz1(self,chat_id,txt):
        print('state_quiz1')
        self.set_state(chat_id,'switch_quiz1')
        tf = self.quiz_data_read()
        tf = tf[((tf.chat_id != chat_id) | (tf.quiz_num!=1))]
        tf.to_pickle(self.file_user_quiz_data)
        return(texts['quiz1']+self.quizes[0][0][0],[[],self.quizes[0][1][0]])
    
    def state_quiz2(self,chat_id,txt):
        print('state_quiz2')
        self.set_state(chat_id,'switch_quiz2')
        tf = self.quiz_data_read()
        tf = tf[((tf.chat_id != chat_id) | (tf.quiz_num!=2))]
        tf.to_pickle(self.file_user_quiz_data)
        print('a')
        resp = (texts['quiz2']+self.quizes[1][0][0],[[],self.quizes[1][1][0]])
        print('b')
        return(resp)
    
    def state_quiz3(self,chat_id,txt):
        print('state_quiz3')
        self.set_state(chat_id,'switch_quiz3')
        tf = self.quiz_data_read()
        tf = tf[((tf.chat_id != chat_id) | (tf.quiz_num!=3))]
        tf.to_pickle(self.file_user_quiz_data)
        return(texts['quiz3']+self.quizes[2][0][0],[[],self.quizes[2][1][0]])
    
    def state_quiz4(self,chat_id,txt):
        print('state_quiz4')
        self.set_state(chat_id,'switch_quiz4')
        tf = self.quiz_data_read()
        tf = tf[((tf.chat_id != chat_id) | (tf.quiz_num!=4))]
        tf.to_pickle(self.file_user_quiz_data)
        return(texts['quiz4']+self.quizes[3][0][0],[[],self.quizes[3][1][0]])

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
        print('switch_quiz1')
        quiz = self.quizes[0]
        t = self.quiz_data_read(chat_id)
        num_answered = len(t[t.quiz_num==1])
        print('answered = '+str(num_answered))
        if num_answered<len(quiz[0]): # ещё не всё отвечено, до этого вопроса
            self.quiz_data_add(1,num_answered,chat_id,txt)
            if (num_answered+1)<len(quiz[0]): # не последний вопрос был?
                return(quiz[0][num_answered+1],[quiz[1][num_answered+1]])
            
        # подсчёт статистики
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

        if stat != len(ans): msgs.append('Стоит повторить урок 1\nhttps://vimeo.com/182268195')
        
        ret = []
        for i in msgs: ret.append([[]])
        ret[-1] = replies['quiz1'][0]
        
        self.set_state(chat_id,'switch_quiz1_afterparty')
        
        # генерация ссылок для повторения
        return(msgs,ret) # если всё отвечено теперь или было изначально
       
    def switch_quiz1_afterparty(self,chat_id,txt):
        print('switch_quiz1_afterparty')
        if txt == self.unlist(replies['quiz1'][0])[0]: #rerun quiz1
            return(self.state_quiz1(chat_id,txt))
        elif txt == self.unlist(replies['quiz1'][0])[1]: #lesson2
            return(self.state_learning2(chat_id,txt))
        else:
            return([self.ku],replies['quiz1'])

    def switch_quiz2(self,chat_id,txt):
        print('switch_quiz2')
        cur_quiz = 2
        quiz = self.quizes[cur_quiz-1]
        t = self.quiz_data_read(chat_id)
        num_answered = len(t[t.quiz_num==cur_quiz])
        print('answered = '+str(num_answered))
        if num_answered<len(quiz[1]): # ещё не всё отвечено, до этого вопроса
            self.quiz_data_add(cur_quiz,num_answered,chat_id,txt)
            if (num_answered+1)<len(quiz[0]): # не последний вопрос был?
                return(quiz[0][num_answered+1],[quiz[1][num_answered+1]])
            
        # подсчёт статистики
        ans = self.quizes[cur_quiz-1][2]
        resp = list(self.quiz_data_read(chat_id).answer)
        match = [ans[i]==resp[i] for i in range(len(ans))]
        stat = sum(match)
        msgs = []
        
        if stat == len(ans): msgs.append('Вау! 100%! Ты крут!')
        elif stat/len(ans) > 0.8: msgs.append('Есть ошибочки, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0.4: msgs.append('Такооое, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0: msgs.append('Оч плохо, '+str(stat)+'/'+str(len(ans)))
        else: msgs.append('Тебе стоит усерднее заниматься, '+str(stat)+'/'+str(len(ans)))

        if not match[0]: msgs.append('Стоит повторить урок 2\nhttps://vimeo.com/182268912')
        
        ret = []
        for i in msgs: ret.append([[]])
        ret[-1] = replies['quiz'+str(cur_quiz)][0]
        
        self.set_state(chat_id,'switch_quiz'+str(cur_quiz)+'_afterparty')
        
        # генерация ссылок для повторения
        return(msgs,ret) # если всё отвечено теперь или было изначально
       
    def switch_quiz2_afterparty(self,chat_id,txt):
        print('switch_quiz2_afterparty')
        cur_quiz = 2
        if txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[0]: #rerun quiz1
            return(self.state_quiz2(chat_id,txt))
        elif txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[1]: #lesson2
            return(self.state_learning3(chat_id,txt))
        else:
            return([self.ku],replies['quiz'+str(cur_quiz)])


    def switch_quiz3(self,chat_id,txt):
        print('switch_quiz3')
        cur_quiz = 3
        quiz = self.quizes[cur_quiz-1]
        t = self.quiz_data_read(chat_id)
        num_answered = len(t[t.quiz_num==cur_quiz])
        print('answered = '+str(num_answered))
        if num_answered<len(quiz[1]): # ещё не всё отвечено, до этого вопроса
            self.quiz_data_add(cur_quiz,num_answered,chat_id,txt)
            if (num_answered+1)<len(quiz[0]): # не последний вопрос был?
                return(quiz[0][num_answered+1],[quiz[1][num_answered+1]])
            
        # подсчёт статистики
        ans = self.quizes[cur_quiz-1][2]
        resp = list(self.quiz_data_read(chat_id).answer)
        match = [ans[i]==resp[i] for i in range(len(ans))]
        stat = sum(match)
        msgs = []
        
        if stat == len(ans): msgs.append('Вау! 100%! Ты крут!')
        elif stat/len(ans) > 0.8: msgs.append('Есть ошибочки, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0.4: msgs.append('Такооое, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0: msgs.append('Оч плохо, '+str(stat)+'/'+str(len(ans)))
        else: msgs.append('Тебе стоит усерднее заниматься, '+str(stat)+'/'+str(len(ans)))

        if not match[0]: msgs.append('Стоит повторить урок 3\nhttps://vimeo.com/182270833')
        
        ret = []
        for i in msgs: ret.append([[]])
        ret[-1] = replies['quiz'+str(cur_quiz)][0]
        
        self.set_state(chat_id,'switch_quiz'+str(cur_quiz)+'_afterparty')
        
        # генерация ссылок для повторения
        return(msgs,ret) # если всё отвечено теперь или было изначально
       
    def switch_quiz3_afterparty(self,chat_id,txt):
        print('switch_quiz3_afterparty')
        cur_quiz = 3
        if txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[0]: #rerun quiz1
            return(self.state_quiz3(chat_id,txt))
        elif txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[1]: #lesson2
            return(self.state_learning4(chat_id,txt))
        else:
            return([self.ku],replies['quiz'+str(cur_quiz)])

    def switch_quiz4(self,chat_id,txt):
        print('switch_quiz4')
        cur_quiz = 4
        quiz = self.quizes[cur_quiz-1]
        t = self.quiz_data_read(chat_id)
        num_answered = len(t[t.quiz_num==cur_quiz])
        print('answered = '+str(num_answered))
        if num_answered<len(quiz[1]): # ещё не всё отвечено, до этого вопроса
            self.quiz_data_add(cur_quiz,num_answered,chat_id,txt)
            if (num_answered+1)<len(quiz[0]): # не последний вопрос был?
                return(quiz[0][num_answered+1],[quiz[1][num_answered+1]])
            
        # подсчёт статистики
        ans = quiz[2]
        resp = list(self.quiz_data_read(chat_id).answer)
        match = [ans[i]==resp[i] for i in range(len(ans))]
        print('switch_quiz_4')
        print(quiz)
        print(ans)
        print(resp)
        stat = sum(match)
        msgs = []
        
        if stat == len(ans): msgs.append('Вау! 100%! Ты крут!')
        elif stat/len(ans) > 0.8: msgs.append('Есть ошибочки, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0.4: msgs.append('Такооое, '+str(stat)+'/'+str(len(ans)))
        elif stat/len(ans) > 0: msgs.append('Оч плохо, '+str(stat)+'/'+str(len(ans)))
        else: msgs.append('Тебе стоит усерднее заниматься, '+str(stat)+'/'+str(len(ans)))

        if not match[0]: msgs.append('Стоит повторить урок 3\nhttps://vimeo.com/182270833')
        
        ret = []
        for i in msgs: ret.append([[]])
        ret[-1] = replies['quiz'+str(cur_quiz)][0]
        
        self.set_state(chat_id,'switch_quiz'+str(cur_quiz)+'_afterparty')
        
        # генерация ссылок для повторения
        return(msgs,ret) # если всё отвечено теперь или было изначально
       
    def switch_quiz4_afterparty(self,chat_id,txt):
        print('switch_quiz4_afterparty')
        cur_quiz = 4
        if txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[0]: #rerun quiz1
            return(self.state_quiz4(chat_id,txt))
        elif txt == self.unlist(replies['quiz'+str(cur_quiz)][0])[1]: #lesson2
            return(self.state_learning4(chat_id,txt))
        else:
            return([self.ku],replies['quiz'+str(cur_quiz)])

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
        print('switch_learning1')
        if txt == self.unlist(replies['learning1'][0])[0]: #quiz
            return(self.state_quiz1(chat_id,txt))
        elif txt == self.unlist(replies['learning1'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['learning1'])
    
    def switch_learning2(self,chat_id,txt):
        print('switch_learning2')
        if txt == self.unlist(replies['learning2'][0])[0]: #quiz
            return(self.state_quiz2(chat_id,txt))
        elif txt == self.unlist(replies['learning2'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['learning2'])
    
    def switch_learning3(self,chat_id,txt):
        print('switch_learning3')
        if txt == self.unlist(replies['learning3'][0])[0]: #quiz
            return(self.state_quiz3(chat_id,txt))
        elif txt == self.unlist(replies['learning3'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['learning3'])
    
    def switch_learning4(self,chat_id,txt):
        print('switch_learning4')
        if txt == self.unlist(replies['learning4'][0])[0]: #quiz
            return(self.state_quiz4(chat_id,txt))
        elif txt == self.unlist(replies['learning4'][0])[1]: #overview
            return(self.state_overview(chat_id,txt))
        else:
            return([self.ku],replies['learning4'])


# In[ ]:



