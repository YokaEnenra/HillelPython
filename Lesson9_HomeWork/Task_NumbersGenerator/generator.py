def random_generate(gen_from: int = 1, gen_to: int = 100):
    for i in range(gen_from, gen_to):
        for j in range(2, round(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i

print("Дайте мне 2 числа и я сгенерирую случайное число в этом диапазоне")
try:
    first_number = int(input("Левая граница: "))
    second_number = int(input("Правая граница: "))
    if second_number - first_number > 0:
        print("В заданном диапазоне я нашел вот такие простые числа: ", end=' ')
        for i in random_generate(first_number, second_number):
            print(i, end=' ')
    else:
        print("Проверьте ввод, левая граница больше либо равна правой")
except:
    print("Вы ввели не число или дробное число")
