def if_sum_in_list(my_list: list = [0], number: int = 1) -> bool:
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] + my_list[j] == number:
                return True
    else:
        return False


is_working = True
while is_working:
    print("Дайте мне список и число и я скажу есть ли в этом списке два числа, сумма которых дает введенное вами число")
    try:
        number_of_elements1 = int(input("Укажите число элементов списка: "))
        a_list1 = [int(input("Следующий элемент списка: ")) for i in range(number_of_elements1)]
        number_for_search1 = int(input("Укажите число которое будем проверять: "))
        if if_sum_in_list(a_list1, number_for_search1):
            print("В вашем списке есть два числа в сумме дающих введенное вами число")
        else:
            print("В вашем списке нету двух чисел в сумме дающих введенное вами число")
        print('Перепроверим с новыми данными?; "y-да", "n-нет"')
        if input() == 'n':
            is_working = False
    except ValueError:
        print("Вы ввели не число или дробное число")
