import random

elem_number1 = int(input("Кол-во элементов первого списка: "))
elem_number2 = int(input("Кол-во элементов второго списка: "))
my_list1 = [random.randint(-10, 10) for i in range(elem_number1)]
my_list2 = [random.randint(-10, 10) for j in range(elem_number2)]
my_set = set(my_list1 + my_list2)
print("В полученных списках", my_list1, my_list2, "всего", len(my_set), "различных чисел, вот они:\n", my_set)
