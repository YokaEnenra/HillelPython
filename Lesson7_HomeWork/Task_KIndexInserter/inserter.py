def inserter(index, array, elem):
    for k in range(len(array) - 1, index - 1, -1):
        if k == len(array) - 1:
            array.append(array[k])
            if k == index:
                array[k] = elem
            else:
                array[k] = array[k - 1]
        elif k == index:
            array[k] = elem
        else:
            array[k] = array[k - 1]
    return True


try:
    print("Укажите кол-во елементов желаемого списка")
    elem_number = int(input())
    arr = list()
    i = 0
    while i < elem_number:
        number = input("Следующий элемент списка: ")
        try:
            arr.append(int(number))
            i += 1
        except ValueError:
            try:
                arr.append(float(number))
                i += 1
            except ValueError:
                print("Вы ввели не число")
    is_insert = False
    while not is_insert:
        print("Укажите индекс куда вы желаете вставить значение")
        insert_index = int(input()) - 1
        print("Укажите вставляемое значение")
        insert_elem = input()
        try:
            insert_elem = int(insert_elem)
        except ValueError:
            try:
                insert_elem = float(insert_elem)
            except ValueError:
                print("Вы ввели не число")
                continue
        if insert_index <= len(arr):
            is_insert = inserter(insert_index, arr, insert_elem)
            for j in enumerate(arr):
                print(j)
        else:
            print("Указанный индекс слишком велик, в массиве нет такого елемента")

except ValueError:
    print("Вы ввели не число или дробное число")
