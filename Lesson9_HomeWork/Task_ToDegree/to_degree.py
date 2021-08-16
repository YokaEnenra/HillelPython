result = lambda x, y=int(1): x ** y

print("Дайте мне два числа и я возведу первое в степень второго")
try:
    first_number = int(input("Первое число: "))
    second_number = int(input("Второе число: "))

    print(result(first_number, second_number))
except:
    print("Вы ввели не число или дробное число")
