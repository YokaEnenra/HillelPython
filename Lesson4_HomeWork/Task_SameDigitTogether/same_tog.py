print("Приветствую, укажи натуральное число и я скажу есть ли в нём повторяющиеся символы, что находятся рядом")
number = input()
try:
    tmp = int(number)
    is_same = False
    i = 0
    while (i < len(number)-1 and is_same == False):
        if (number[i] == number[i + 1]):
            is_same = True
        # for j in range(i + 1, len(number)):
        #     current_digit_2 = number[j]
        #     if (current_digit == current_digit_2):
        #         is_same = True
        i += 1
    if (is_same == False):
        print("Твое число", number, "не имеет находящихся рядом повторяющихся символов")
    else:
        print("Твое число", number, "имеет находящиеся рядом повторяющиеся символы")
except:
    print("Твое число", number, "не является натуральным или вообще не число")