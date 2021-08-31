import sorters_tmp
import random


my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.bubble(my_list)
print("Сортировка от большего к меньшему пузырьком:\n", my_list)
my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.bubble(my_list, False)
print("Сортировка от меньшего к большему пузырьком:\n", my_list)
my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.choose(my_list)
print("Сортировка от большего к меньшему выбором:\n", my_list)
my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.choose(my_list, False)
print("Сортировка от меньшего к большему выбором:\n", my_list)
my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.insert(my_list)
print("Сортировка от большего к меньшему вставками:\n", my_list)
my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters_tmp.insert(my_list, False)
print("Сортировка от меньшего к большему вставками:\n", my_list)
