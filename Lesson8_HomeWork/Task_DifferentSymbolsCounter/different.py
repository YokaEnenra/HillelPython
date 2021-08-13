import random

elem_number = int(input("Кол-во элементов списка: "))
my_list = [random.randint(-10, 10) for i in range(elem_number)]
my_set = set(my_list)
print("В полученном списке",my_list,"всего",len(my_set),"различных чисел, вот они:\n",my_set)