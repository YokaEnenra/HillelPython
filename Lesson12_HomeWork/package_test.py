from HomeWorkPackage import list_worker
from HomeWorkPackage import different_func

import random


class NumberOut(Exception):
    def __str__(self):
        return "Этому номеру не соответствует ни один выбор"


while True:
    print(
        "Это проверка пакета, содержащего модули list_worker и different_func."
        "\nПервый модуль содержит 3 ф-кции работы со списком"
        "\nВторой модуль содержит разные ф-кции не обьединенных одной темой"
        "\n Введите 3 чтобы закончить работу")
    try:
        module_choose = int(input("Выберите тестируемый модуль: "))
        if module_choose not in range(1, 4):
            raise NumberOut
    except(ValueError, NumberOut) as err:
        print(err)
    else:
        if module_choose == 1:
            print("Вы выбрали первый модуль, теперь выберите 1 из 3 ф-кция, "
                  "где:"
                  "\n1) Вставка элемента по индексу в список"
                  "\n2) Удаление элемента по индексу"
                  "\n3) Подсчет кол-ва уникальных элементов в двух списках"
                  "\n4) Возврат к выбору модуля")
            try:
                func_choose = int(input("Ваш выбор: "))
                if func_choose not in range(1, 5):
                    raise NumberOut
            except(ValueError, NumberOut) as err:
                print(err)
            else:
                if func_choose == 1:
                    while True:
                        try:
                            number_of_elem1 = int(input("Укажите число "
                                                        "елементов в списке: "))
                        except ValueError as err:
                            print(err)
                        else:
                            array1 = [random.randint(1, 100) for i in
                                      range(number_of_elem1)]
                            print(array1, "\nМассив создан")
                            try:
                                elem_to_insert = int(input("Укажите елемент "
                                                           "который необходимо "
                                                           "вставить: "))
                            except ValueError as err:
                                print(err)
                            else:
                                try:
                                    index_to_insert = int(input("Укажите индекс"
                                                                "по которому "
                                                                "вставить "
                                                                "елемент: "))\
                                                      - 1
                                except ValueError as err:
                                    print(err)
                                else:
                                    if index_to_insert < len(array1):
                                        array1 = list_worker.inserter \
                                            (index_to_insert, array1,
                                             elem_to_insert)
                                        print(array1, "\nЭлемент вставлен")
                                        break
                                    else:
                                        print("Элемента с таким индексом нет")
                                        continue
                elif func_choose == 2:
                    while True:
                        try:
                            number_of_elem1 = int(
                                input("Укажите число елементов в списке: "))
                        except ValueError as err:
                            print(err)
                        else:
                            array1 = [random.randint(1, 100) for i in
                                      range(number_of_elem1)]
                            print(array1, "\nМассив создан")
                            try:
                                index_to_remove = int(input(
                                    "Укажите индекс по которому удалить "
                                    "елемент: ")) - 2
                            except ValueError as err:
                                print(err)
                            else:
                                if index_to_remove < len(array1):
                                    array1 = list_worker.remover(
                                        index_to_remove, array1)
                                    print(array1, "\nЭлемент удален")
                                    break
                                else:
                                    print("Элемента с таким индексом нет")
                                    continue
                elif func_choose == 3:
                    while True:
                        try:
                            number_of_elem1 = int(
                                input("Укажите число елементов в списке: "))
                        except ValueError as err:
                            print(err)
                        else:
                            array1 = [random.randint(1, 100) for i in
                                      range(number_of_elem1)]
                            print(array1, "\nМассив 1 создан")
                            try:
                                number_of_elem2 = int(
                                    input("Укажите число елементов в списке: "))
                            except ValueError as err:
                                print(err)
                            else:
                                array2 = [random.randint(1, 100) for i in
                                          range(number_of_elem1)]
                                print(array2, "\nМассив 2 создан")
                                array3 = list_worker.uniq_counter(array1,
                                                                  array2)
                                print(array3, "\nУникальные элементы посчитаны")
                                break
        elif module_choose == 2:
            print(
                "Вы выбрали второй модуль, теперь выберите 1 из 3 ф-кций, "
                "где:"
                "\n1) Смена значений между двумя численными элементами"
                "\n2) Проверка вводимого пароля"
                "\n3) Поиск всех автоморфных чисел до указанной границы"
                "\n4) Возврат к выбору модуля")
            try:
                func_choose = int(input("Ваш выбор: "))
                if func_choose not in range(1, 5):
                    raise NumberOut
            except(ValueError, NumberOut) as err:
                print(err)
            else:
                if func_choose == 1:
                    while True:
                        try:
                            elem1 = int(input("Укажите первый елемент: "))
                            elem2 = int(input("Укажите второй елемент: "))
                        except ValueError as err:
                            print(err)
                        else:
                            print(f"Было: {elem1},{elem2}")
                            elem1, elem2 = different_func.data_switcher(elem1,
                                                                        elem2)
                            print(f"Стало: {elem1},{elem2}")
                            break
                elif func_choose == 2:
                    if_pass = different_func.password_checker()
                elif func_choose == 3:
                    different_func.automorphic_numbers()
        else:
            break
