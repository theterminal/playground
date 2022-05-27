# 20220520
# Learn to Multiply - (Multiplication Table Game for Kids)
import random

counter_yes, counter_no = 0, 0

while True:
    rand_num_1 = random.randint(0, 10)                           # range of the first number
    rand_num_2 = random.randint(0, 10)                           # range of the second number

    answer_comp = rand_num_1 * rand_num_2
    print(f'Колко е {rand_num_1} * {rand_num_2} = ', end="")
    answer_human = int(input())

    if answer_human == answer_comp:
        counter_yes += 1
        print(f'ПРАВИЛНО!\n                    [Верни {counter_yes} - Грешни {counter_no}]\n')
    else:
        counter_no += 1
        print(f'ГРЕШКА! {rand_num_1} * {rand_num_2} = {answer_comp}\n                    [Верни {counter_yes} - Грешни {counter_no}]\n')
        