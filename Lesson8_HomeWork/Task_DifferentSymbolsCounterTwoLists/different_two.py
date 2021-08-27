import random

elem_number1 = int(input("Кол-во элементов первого списка: "))
elem_number2 = int(input("Кол-во элементов второго списка: "))
my_list1 = [random.randint(-10, 10) for i in range(elem_number1)]
my_list2 = [random.randint(-10, 10) for j in range(elem_number2)]
my_set = set(i for i in my_list1 if i in my_list2)
print("В первом полученном списке", my_list1, "всего", len(my_set), "различных чисел, встречающихся во втором списке", my_list2,"вот они:\n", my_set)
