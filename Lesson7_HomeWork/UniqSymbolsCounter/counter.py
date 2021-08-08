import random


def uniq(array, uniq_list):
    for k in range(len(array)):
        is_uniq = True
        for n in range(len(uniq_list)):
            if uniq_list[n] == array[k]:
                is_uniq = False
        if is_uniq:
            uniq_list.append(array[k])
    return uniq_list


list1 = [random.randint(-20, 20) for i in range(10)]
list2 = [random.randint(-20, 20) for j in range(10)]
# uniq_list = [k for k in list1 + list2 if k not in ]
uniq_list = list()
uniq_list = uniq(list1, uniq_list)
uniq_list = uniq(list2, uniq_list)
print(list1, list2, '\n', uniq_list)
print("В двух списках всего", len(uniq_list), "уникальных елементов")
