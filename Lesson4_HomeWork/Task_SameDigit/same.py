print("Приветствую, укажи натуральное число и я скажу есть ли в нём повторяющиеся символы")
number = input()
try:
    tmp = int(number)
    is_same = False
    i = 0
    while (i < len(number) and is_same == False):
        current_digit = number[i]
        for j in range(i + 1, len(number)):
            current_digit_2 = number[j]
            if (current_digit == current_digit_2):
                is_same = True
        i += 1
    if (is_same == False):
        print("Твое число", number, "не имеет повторяющихся символов")
    else:
        print("Твое число", number, "имеет повторяющиеся символы")
except:
    print("Твое число", number, "не является натуральным или вообще не число")
