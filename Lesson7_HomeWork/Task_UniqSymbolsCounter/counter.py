import random


list1 = [random.randint(-10, 10) for i in range(10)]
list2 = [random.randint(-10, 10) for j in range(10)]
# list1 = [input("Элемент:") for j in range(5)]
# list2 = [input("Элемент:") for i in range(5)]
uniq_list = [k for k in list1 + list2 if list1.count(k)+list2.count(k) == 1]
# uniq_list = list()
# for k in list1+list2:
#     counter = 0
#     for n in list1+list2:
#         if k == n:
#             counter += 1
#     if counter == 1:
#         uniq_list.append(k)

print(list1, list2, '\n', uniq_list)
print("В двух списках всего", len(uniq_list), "уникальных елементов")