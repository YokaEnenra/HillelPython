from math import log10


def reverse_it(n: int) -> int:
    if n > 10:
        current_number = n % 10
        not_reversed_numbers = n // 10
        degree_counter = int(log10(not_reversed_numbers) + 1)

        return current_number * 10 ** degree_counter + reverse_it(not_reversed_numbers)
    else:
        return n


counter = int(input("Сколько чисел будем переворачивать? "))
for i in range(counter):
    print(reverse_it(int(input("Введите число: "))))
