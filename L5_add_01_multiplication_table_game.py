# 20220520
# Multiplication Table Game

import random

counter_yes = 0
counter_no = 0

while True:
    rand_num_1 = random.randint(0, 10)                           # changes the range of the one number
    rand_num_2 = random.randint(0, 10)                           # changes the range of the other number

    answer_comp = rand_num_1 * rand_num_2
    print(f'Колко е {rand_num_1} * {rand_num_2} = ', end="")
    answer_human = int(input())

    if answer_human == answer_comp:
        counter_yes += 1
        print(f'ПРАВИЛНО!\n                    [Верни {counter_yes} - Грешни {counter_no}]\n')
    else:
        counter_no += 1
        print(f'ГРЕШКА! {rand_num_1} * {rand_num_2} = {answer_comp}\n                    [Верни {counter_yes} - Грешни {counter_no}]\n')

