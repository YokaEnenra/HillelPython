print('Приветствую вас в программе ответа на вопрос "А высокосный ли год", допустиые года 1900-1000000')
year = int(input())
if 1900 >= year or year >= 1000000:
    print("Введенный вами год не входит в допустимый предел")
else:
    print("Ваш год принят в обработку, ожидайте")
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Введенный вами", year, "год является високосным")

    else:
        print("Введенный вами", year, "год является невисокосным")
