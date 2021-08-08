def remover(index=int(), array=list()):
    for k in range(index, len(array) - 1):
        array[k] = array[k + 1]
    array.pop()
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
    is_rmv = False
    while not is_rmv:
        print("Укажите индекс элемента который желаете удалить")
        rmv_index = int(input()) - 1
        if rmv_index <= len(arr):
            is_rmv = remover(rmv_index, arr)
            for j in enumerate(arr):
                print(j)
        else:
            print("Указанный индекс слишком велик, в массиве нет такого елемента")

except ValueError:
    print("Вы ввели не число или дробное число")
