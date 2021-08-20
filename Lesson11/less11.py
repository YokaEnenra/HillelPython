def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def sort(arr):
    def _sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _sort(items, low, split_index)
            _sort(items, split_index + 1, high)
    _sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    import random
    my_arr = [random.randint(1, 50) for i in range(10)]
    print(my_arr, '\n')
    sort(my_arr)
    print(my_arr)
