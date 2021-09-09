"""Этот модуль предназначен для сортировки списков чисел 3мя методами:
    1) Сортировка пузырьком ф-кция bubble
    2) Сортировка выбором ф-кция choose
    3) Сортировка вставками ф-кция insert
    Все ф-кции сортировки имеют два параметра:
    1. Список чисел;
    2. True-Сортировка от большего к меньшему и
    False-Сортировка от меньшего к большему.
    2ой параметр является необзяательным и по умолчанию установлен True"""

__all__ = ["bubble", "choose", "insert"]


def bubble(received_list: list, what_type: bool = True) -> list:
    """Эта функция сортирует список чисел методом пузырька, по умолчанию
    сортировка производится от большего к меньшему, для сортировки от меньшего
    к большему необходимо вторым параметром передать False"""
    if what_type:
        for i in range(len(received_list)):
            for j in range(len(received_list) - 1):
                if received_list[j] < received_list[j + 1]:
                    received_list[j], received_list[j + 1] = \
                        received_list[j + 1], received_list[j]
        return received_list
    else:
        for i in range(len(received_list)):
            for j in range(len(received_list) - 1):
                if received_list[j] > received_list[j + 1]:
                    received_list[j], received_list[j + 1] = \
                        received_list[j + 1], received_list[j]
        return received_list


def choose(received_list: list, what_type: bool = True) -> list:
    """Эта функция сортирует список чисел методом выбора, по умолчанию
    сортировка производится от большего к меньшему, для сортировки от меньшего
    к большему необходимо вторым параметром передать False"""
    if what_type:
        for i in range(len(received_list) - 1):
            m = i
            for j in range(i + 1, len(received_list)):
                if received_list[j] > received_list[m]:
                    m = j
                j += 1
            received_list[i], received_list[m] = \
                received_list[m], received_list[i]
            i += 1
        return received_list
    else:
        for i in range(len(received_list) - 1):
            m = i
            for j in range(i + 1, len(received_list)):
                if received_list[j] < received_list[m]:
                    m = j
                j += 1
            received_list[i], received_list[m] = \
                received_list[m], received_list[i]
            i += 1
        return received_list


def insert(received_list: list, what_type: bool = True) -> list:
    """Эта функция сортирует список чисел методом вставок, по умолчанию
    сортировка производится от большего к меньшему, для сортировки от меньшего
    к большему необходимо вторым параметром передать False"""
    if what_type:
        for i in range(1, len(received_list)):
            key = received_list[i]
            j = i - 1
            while j >= 0 and key > received_list[j]:
                received_list[j + 1] = received_list[j]
                j -= 1
            received_list[j + 1] = key
        return received_list
    else:
        for i in range(1, len(received_list)):
            key = received_list[i]
            j = i - 1
            while j >= 0 and key < received_list[j]:
                received_list[j + 1] = received_list[j]
                j -= 1
            received_list[j + 1] = key
        return received_list


if __name__ == "__main__":
    pass
