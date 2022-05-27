# 20220520 - Python - Python Fundamentals - L5
# 08 - Additional problem

import random

question = ['България', 'Русия', 'САЩ', 'Канада', 'Великобритания', 'Германия', 'Румъния', 'Гърция', 'Франция', 'Италия', 'Испания']
answer_com = ['софия', 'москва', 'вашингтон', 'отава', 'лондон', 'берлин', 'букурещ', 'атина', 'париж', 'рим', 'мадрид']
counter_yes = 0
counter_no = 0
flag = ""

while True:
    a = random.randint(0, 5)

    print(f'Въпрос: Коя е столицата на {question[a]}?')
    answer_human = input('Отговор: ').lower()

    if answer_human == 'Стоп':
        break
    elif a == 0:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False
    elif a == 1:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False
    elif a == 2:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False
    elif a == 3:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False
    elif a == 4:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False
    elif a == 5:
        if answer_human == answer_com[a]:
            flag = True
        else:
            flag = False

    if flag:
        counter_yes += 1
        print(f'Правилно! => Верни {counter_yes} - Грешни {counter_no}\n')
    else:
        counter_no += 1
        print(f'Грешка! => Верни {counter_yes} - Грешни {counter_no}\n')
