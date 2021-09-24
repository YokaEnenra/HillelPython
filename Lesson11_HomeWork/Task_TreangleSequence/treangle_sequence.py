def count_first(nums, n: int):
    sum_to_return = 0
    j = 0
    if n == 1:
        print('1', end='')
    else:
        i = 1
        while sum_to_return < n:
            sum_to_return += i
            j = i
            i += 1
        print(count_first(None, n - 1), j, end='')
    return ''


print(count_first(None, int(input("Укажите сколько елементов вывести: "))))
