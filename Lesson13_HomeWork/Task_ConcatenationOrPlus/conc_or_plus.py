def conc_or_plus_func(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return str(a)+str(b)
    else:
        return a + b


elem1 = input("Введите елемент1: ")
elem2 = input("Введите елемент2: ")
print(conc_or_plus_func(elem1, elem2))
