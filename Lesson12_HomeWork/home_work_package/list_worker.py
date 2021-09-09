"""Этот модуль представляет 3 ф-кции работы с списком:
    1) Вставка элемента по индексу в список
    2) Удаление элемента по индексу
    3) Подсчет кол-ва уникальных элементов в двух списках"""

__all__ = ["inserter", "remover", "uniq_counter"]


def inserter(index: int, array: list, elem):
    """Эта ф-кция получает индекс элемента, список элементов и любое значение,
    затем добавляет полученное значение в список по указанному индексу,
    затем переиндекесирует и возвращает список """
    for k in range(len(array) - 1, index - 1, -1):
        if k == len(array) - 1:
            array.append(array[k])
            if k == index:
                array[k] = elem
            else:
                array[k] = array[k - 1]
        elif k == index:
            array[k] = elem
        else:
            array[k] = array[k - 1]
    return array


def remover(index: int, array: list):
    """Эта ф-кция принимает индекс и списко элементов, а затем удаляет
    элемент по указанному индексу, переиндексирует и возвращает список """
    for k in range(index, len(array) - 1):
        array[k] = array[k + 1]
    array.pop()
    return array


def uniq_counter(list1: list, list2: list):
    """Эта ф-кция принимает два списка и затем указывает сколько
    уникальных элементов в этих двух списках"""
    uniq_list = [k for k in list1 + list2 if list1.count(k)+list2.count(k) == 1]
    print(list1, list2, '\n', uniq_list)
    print("В двух списках всего", len(uniq_list), "уникальных елементов")
