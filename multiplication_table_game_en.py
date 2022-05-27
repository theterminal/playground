# 20220520
# Learn to Multiply - (Multiplication Table Game for Kids)
import random

counter_yes, counter_no = 0, 0

while True:
    rand_num_1 = random.randint(0, 10)                           # range of the first number
    rand_num_2 = random.randint(0, 10)                           # range of the second number

    answer_comp = rand_num_1 * rand_num_2
    print(f'Calculate {rand_num_1} * {rand_num_2} = ', end="")
    answer_human = int(input())

    if answer_human == answer_comp:
        counter_yes += 1
        print(f'OK\n                       [Correct {counter_yes} - Incorrect {counter_no}]\n')
    else:
        counter_no += 1
        print(f'INCORRECT {rand_num_1} * {rand_num_2} = {answer_comp}\n                       [Correct {counter_yes} - Incorrect {counter_no}]\n')
