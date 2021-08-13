# def hi():
#     """ Печатает hi"""  # Описание ф-кции
#     print('hi')
#
#
# hello = hi
# hello()

# def func(*args):  # Ф-кция принимает список
#     print(args)
#     return args
#
#
# func(1,2,3,'abc')

# def func(**kwargs):  # Ф-кция принимает словарь
#     print(kwargs)
#     return kwargs
#
#
# func(a=1,b=2,c=3,d='abc')

# def func(c, a=int(), b=float()) -> int:
#     print(a+b+c)
#     return a
#
#
# func(1, 3, 2.4)

# f1 = lambda: 10+20
# f2 = lambda x, y: x + y
# f3 = lambda x, y, z: print(f1())
# print(f1())
# print(f2(5, 7))
# print('*'*20)
# print(f3(1, 2, 3))
# print('*'*20)

def gen_f(x, y):
    for i in range(1, x+1):
        yield i**y


# for n in gen_f(15, 3):
#     print(n, end=' ')
f = gen_f(4, 2)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
