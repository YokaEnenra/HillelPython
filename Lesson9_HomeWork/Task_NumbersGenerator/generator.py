def generate(gen_from: int = 1, gen_to: int = 100, gen_amount: int = 1):
    generated_number = gen_to - gen_from
    generated_numbers = list()
    if gen_to == gen_from or gen_to - gen_from == 1:
        return gen_to
    tmp = generated_number
    for i in range(gen_amount):
        tmp /= (gen_to / gen_from) / 2
        tmp *= (gen_to * gen_from) * 2
        while True:
            tmp = round(tmp)
            if tmp > gen_to:
                tmp /= (gen_to/gen_from)/2
            elif tmp < gen_from:
                tmp *= (gen_to*gen_from)*2
            elif tmp in range(gen_from, gen_to + 1) and tmp not in generated_numbers:
                generated_numbers.append(tmp)
                break
    return generated_numbers


print("Дайте мне 2 числа и я сгенерирую случайное число в этом диапазоне")
try:
    first_number = int(input("Первое число: "))
    second_number = int(input("Второе число: "))
    number_of_generated = int(input("Сколько чисел генерировать?: "))
    generation_result = generate(first_number, second_number, number_of_generated)
    print("Я сгенерировал числа:", end=' ')
    for i in generation_result:
        print(i, end=' ')
except:
    print("Вы ввели не число или дробное число")
