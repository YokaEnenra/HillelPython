import sys

sys.path.append('E:\Python Projects\HomeWork2\Lesson12_HomeWork\Task_SorterModule')
print(sys.path)
import sorters
import random


my_list = [random.randint(1,100) for i in range(15)]
my_list = sorters.bubble(my_list)
print(my_list)
