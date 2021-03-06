class NonRangeNumber(Exception):
    pass


print("Приветствую вас в программе постройки пирамиды, укажите число от 3 до 9 и я построю пирамиду")
try:
    pyramid_middle = input()
    int_pyramid_middle = int(pyramid_middle)
    if int_pyramid_middle not in range(3, 10):
        raise NonRangeNumber
    for i in range(1, int_pyramid_middle + 1):
        result_pyramid = ""
        for j in range(1, i):
            result_pyramid += str(j)
        for k in range(i, 0, -1):
            result_pyramid += str(k)
        print(result_pyramid)

except NonRangeNumber:
    print("Ваше число не входит в допустимый диапазон чисел")
except ValueError:
    print("Ваше число не натуральное или не число вовсе")
