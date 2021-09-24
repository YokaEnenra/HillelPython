def count_first(nums, n: int):
    summ = 0
    j = 0
    if n == 1:
        print('1', end='')
    else:
        i = 1
        while summ < n:
            summ += i
            j = i
            i += 1
        print(count_first(None, n - 1), j, end='')
    return ''


print(count_first(None, int(input("Укажите сколько елементов вывести: "))))
