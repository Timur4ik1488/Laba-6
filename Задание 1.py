try:
    def f(s):
            #Инициализация всех переменных
        max_r=0 #максимальная доля
        res_words=[] #список слов
        cur_word="" #отдельное слово из строки
        total_count=0 #общее количество букв А и Б
        count_a=0
        count_b=0
        for i in s: #перебор элементов из списка
            if i != ' ': #если символ не будет являться проблелом, то добавляем будем добавлять его в отдельную строку
                cur_word+=i
                if i == ('а'):
                    count_a+=1
                elif i == 'б':
                    count_b+=1
                total_count+=1 #общее воличество букв в слове
            else:
                if cur_word:
                    if total_count>0:
                        r=(count_a + count_b)/total_count #высчитываем общее количество букв а и б в слове
                    else:
                        r=0

                    # сравниваем с максимальной долей в слове
                    if r > max_r:
                        max_r = r
                        res_words = [cur_word]  # начинаем новый список с текущим словом
                    elif r == max_r:
                        res_words = [*res_words, cur_word]  # заносим это слово в список с конечным результатом

                # сбрасываем счётчики для нового слова
                cur_word = ""
                total_count = 0
                count_a = 0
                count_b = 0
















