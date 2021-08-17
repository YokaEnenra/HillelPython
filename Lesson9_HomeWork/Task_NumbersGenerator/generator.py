def random_generate(gen_from: int = 1, gen_to: int = 100, gen_amount: int = 1):
    generated_number = gen_to - gen_from
    generated_numbers = list()
    for j in range(1, gen_amount+1):
        generated_number /= (gen_to / gen_from) / j
        generated_number *= (gen_to * gen_from) * j
        n = j
        while True:
            generated_number = round(generated_number)
            if generated_number < gen_from:
                # generated_number /= (gen_to / gen_from) * n * 2
                generated_number *= (gen_to * gen_from) / n / 2
                n += 1
            else:
                yield generated_number
                generated_numbers.append(generated_number)
                break


print("Дайте мне 2 числа и я сгенерирую случайное число в этом диапазоне")
try:
    first_number = int(input("Первое число: "))
    second_number = int(input("Второе число: "))
    number_of_generated = int(input("Сколько чисел генерировать?: "))
    if second_number - first_number > 0 and second_number - first_number + 1 >= number_of_generated > 0:
        print("Я сгенерировал вот такие числа:", end=' ')
        for i in random_generate(first_number, second_number, number_of_generated):
            print(i, end=' ')
    else:
        print("Проверьте ввод, возможны ошибки: \n1)Кол-во генерируемых чисел больше промежутка чисел\n"
              "2)Левая граница больше либо равна правой\n3)Кол-во генериремых чисел меньше или равно 0")
except:
    print("Вы ввели не число или дробное число")
