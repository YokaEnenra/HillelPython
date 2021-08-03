print("Приветствую, укажи натуральное число и я выведу все автоморфные числа, что стоят до него")
str_number = input()
try:
    int_number = int(str_number)
    for i in range(1, int_number):
        pow_i = i ** 2
        str_pow = str(pow_i)
        str_i = str(i)
        len_i = len(str_i)
        len_pow = len(str_pow)
        count = 0
        n = 0
        for j in range(len_pow - len_i, len_pow):
            if (str_pow[j] == str_i[n]):
                count += 1
                n += 1
            else:
                break
        if (count == len_i):
            print(i, "*", i, "=", pow_i)
except:
    print("Твое число", str_number, "не является натуральным или вообще не число")
