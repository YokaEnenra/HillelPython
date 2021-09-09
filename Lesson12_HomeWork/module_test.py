import random
import sorters


class NumberOut(Exception):
    def __str__(self):
        return "Этому номеру не соответствует ни одно действие"


while True:
    print("Это тест модуля sorters, для начала укажите тип сортировки, "
          "где:"
          "\n1) Сортировка пузырьком"
          "\n2) Сортировка выбором"
          "\n3) Сортировка вставками"
          "\n4) Конец работы")
    try:
        choose_sorter = int(input("Ваш выбор: "))
        if choose_sorter not in range(1, 5):
            raise NumberOut
    except(NumberOut, ValueError) as err:
        print(err)
    else:
        if choose_sorter == 1:
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.bubble(my_list)
            print("Сортировка от большего к меньшему пузырьком:\n", my_list)
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.bubble(my_list, False)
            print("Сортировка от меньшего к большему пузырьком:\n", my_list)
        elif choose_sorter == 2:
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.choose(my_list)
            print("Сортировка от большего к меньшему выбором:\n", my_list)
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.choose(my_list, False)
            print("Сортировка от меньшего к большему выбором:\n", my_list)
        elif choose_sorter == 3:
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.insert(my_list)
            print("Сортировка от большего к меньшему вставками:\n", my_list)
            my_list = [random.randint(1, 100) for i in range(15)]
            my_list = sorters.insert(my_list, False)
            print("Сортировка от меньшего к большему вставками:\n", my_list)
        else:
            exit()
