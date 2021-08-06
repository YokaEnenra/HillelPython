# Ввод одномерного массива
# my_list=list()
# for i in range(5):
#     number=int(input())
#     my_list.append(number)
# print(my_list)

# Создание нескольких одинаковых массивов(2) в одном
# arr=[[]]*2
# arr[0].append(5)
# print(arr)


# Работа с двумерным массивом
# list=[[1,2,3],[4,5,6],[7,8,9]]
# print(list)
# list[1][1]=15
# print(list)


# Генератор одномерного массива
# list=[input() for x in range(10)]
# print(list)


# Множественное присвоение значений из массива в переменные
# *x,y,z=[1,2]
# print(x,"\n",y,"\n",z)


# Попытка в двумерный массив
# a=int(input())
# b=int(input())
# arr=[[]]
# arr*=a
# for i in range(0,a-1):
#     arr[i]=[]*b
# for i in range(a):
#     for j in range(b):
#         arr[i][j] =int(input)


#
# list=[1,4,5,6,7]
# my_expr=(i for i in list if i%2==0)
# print(sum(my_expr))


# Кортежи
t=(5,)
print(type(t))
