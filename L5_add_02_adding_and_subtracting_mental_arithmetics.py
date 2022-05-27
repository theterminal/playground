# 20220522
# MAE - Mental Arithmetic - Clever-3 - Book 'B'

# Homework - page 58 - # 1

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# lst = [[79, -70, 80, -24, 90],
#        [86, 10, -79, -15, 81],
#        [96, -25, 90, 20, -15],
#        [44, 81, -14, 40, 15],
#        [96, 20, -94, -21, 12],
#        [83, 44, 4, 90, -45],
#        [60, -50, 10, -7, -9],
#        [56, -1, -10, -7, -36],
#        [46, -5, 70, -29, 90],
#        [70, -1, -59, 10, -19]]

lst = [[79, -70, 80, -178, 90],
       [86, 10, -79, -15, 0],
       [96, -25, 90, 20, -178]]

final_counter_no = 0
cycle = 0

for i in range(len(lst)):
    counter_yes = 0
    counter_no = 0
    cycle = 0

    while True:
        clear_screen()
        print(f'\nЗадача № {i + 1} --------------------\n')
        print(lst[i], sum(lst[i]))                      # prints out the element of the list + the sum next to it
        # print(lst[i])                                 # prints out the element of the list
        result = int(input('\nсумата е: '))

        if result == sum(lst[i]):
            print('\n* * * * * * * * * * * * * * * *')
            print('*                             *')
            print('*            ВЯРНО!           *')
            print('*                             *')
            print('* * * * * * * * * * * * * * * *\n')
            counter_yes += 1
            break
        else:
            print('\n* * * * * * * * * * * * * * * *')
            print('*                             *')
            print('*  ГРЕШКА! - Изчисли отново!  *')
            print('*                             *')
            print('* * * * * * * * * * * * * * * *\n')
            counter_no += 1
            cycle += 1
            print(f'ВЕРНИ      [ {counter_yes} : {counter_no} ]     ГРЕШНИ')
            zero = input('\n\nEnter -> продължи')

    if cycle > 0:
        final_counter_no += 1

    print(f'ВЕРНИ      [ {counter_yes} : {counter_no} ]     ГРЕШНИ')
    zero = input('\n\nEnter -> продължи')

if final_counter_no == 1:
    print(f'\nОт {len(lst)} задачи, {final_counter_no} беше сгрешена и коригирана!\n')
else:
    print(f'\nОт {len(lst)} задачи, {final_counter_no} бяха сгрешени и коригирани!\n')
