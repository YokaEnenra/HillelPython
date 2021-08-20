import random


class NotInValueRange(Exception):
    pass


def two_dim_arr_sorter(my_arr):
    """Ф-кция сортировки матрицы по сумме эелементов столбцов и затем сортировка столбцов по возрастанию снизу вверх
    и сверху вниз для нечетных и четных столбцов соответственно """
    '''Сортировка столбцов по сумме их элементов'''
    counter_of_col = list()
    for i in range(len(my_arr)):
        counter_of_col.append(0)
        for k in range(len(my_arr)):
            for n in range(len(my_arr[k])):
                if n == i:
                    counter_of_col[i] += my_arr[k][n]
    for i in range(len(counter_of_col) - 1):
        for j in range(len(counter_of_col) - 2, i - 1, -1):
            if counter_of_col[j + 1] < counter_of_col[j]:
                counter_of_col[j + 1], counter_of_col[j] = counter_of_col[j], counter_of_col[j + 1]
                for k in range(len(my_arr)):
                    for n in range(len(my_arr[k])):
                        my_arr[n][j + 1], my_arr[n][j] = my_arr[n][j], my_arr[n][j + 1]
    '''Сортировка нечетных столбцов по возрастанию снизу вверх
       и четных столбцов по возрастанию сверху вниз'''
    for i in range(len(my_arr)):
        curr_col_arr = list()
        for k in range(len(my_arr)):
            for n in range(len(my_arr[k])):
                if n == i:
                    curr_col_arr.append(my_arr[k][n])
        if i % 2 == 0:
            for k in range(len(curr_col_arr) - 1):
                for n in range(len(curr_col_arr) - 2, k - 1, -1):
                    if curr_col_arr[n + 1] > curr_col_arr[n]:
                        curr_col_arr[n + 1], curr_col_arr[n] = curr_col_arr[n], curr_col_arr[n + 1]
        else:
            for k in range(len(curr_col_arr) - 1):
                for n in range(len(curr_col_arr) - 2, k - 1, -1):
                    if curr_col_arr[n + 1] < curr_col_arr[n]:
                        curr_col_arr[n + 1], curr_col_arr[n] = curr_col_arr[n], curr_col_arr[n + 1]
        for k in range(len(my_arr)):
            for n in range(len(my_arr[k])):
                if n == i:
                    my_arr[k][n] = curr_col_arr[k]
    return my_arr


def two_dim_arr_printer(my_arr):
    counter_of_col = list()
    for i in range(len(my_arr)):
        counter_of_col.append(0)
        for k in range(len(my_arr)):
            for n in range(len(my_arr[k])):
                if n == i:
                    counter_of_col[i] += my_arr[k][n]
    for i in my_arr:
        print()
        for j in i:
            print(f'{j: 4}', end='')
    print()
    for i in counter_of_col:
        print(f'{i: 4}', end='')


print(
    "Приветствую вас в программе создания и сортироввки, укажите M, где MxM-итоговый двумерный массив, "
    "M должен быть больше 5")
try:
    number_of_elements = int(input("Ваше М: "))
    if number_of_elements <= 5:
        raise NotInValueRange
    created_array = [[random.randint(1, 50) for i in range(number_of_elements)] for j in range(number_of_elements)]
    print("\nСгенерированный двумерный массив до сортировки: ", end='')
    two_dim_arr_printer(created_array)
    sorted_array = two_dim_arr_sorter(created_array)
    print("\n\nСгенерированный двумерный массив после сортировки: ", end='')
    two_dim_arr_printer(sorted_array)
except ValueError:
    print("Вы ввели дробное число или не число вовсе")
except NotInValueRange:
    print("Вы ввели M меньший или равный 5")
