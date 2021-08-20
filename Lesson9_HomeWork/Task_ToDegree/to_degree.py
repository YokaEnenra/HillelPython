print("Дайте мне два числа и я возведу первое в степень второго")
print("Сколько чисел будем возводить?")
try:
    number_of_elements = int(input("Кол-во: "))
    first_numbers = [int(input("Первое число: ")) for i in range(number_of_elements)]
    second_numbers = [int(input("Второе число: ")) for i in range(number_of_elements)]
    result_for_print = list(map(lambda x, y=int(1): x ** y, first_numbers, second_numbers))
    print(result_for_print)
except ValueError:
    print("Вы ввели не число или дробное число")
