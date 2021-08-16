def generate(gen_from: int = 1, gen_to: int = 100):
    generated_number = gen_to - gen_from
    if gen_to == gen_from or gen_to - gen_from == 1:
        return gen_to
    while True:
        generated_number *= 3
        generated_number /= 5
        generated_number = round(generated_number)
        if generated_number in range(gen_from, gen_to + 1):
            return generated_number


print("Дайте мне 2 числа и я сгенерирую случайное число в этом диапазоне")
try:
    first_number = int(input("Первое число: "))
    second_number = int(input("Второе число: "))
    print("Я сгенерировал число:", generate(first_number, second_number))
except:
    print("Вы ввели не число или дробное число")
