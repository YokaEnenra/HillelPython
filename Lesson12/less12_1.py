# from less12_2 import igor as wegor
#
# wegor(int(input("Хачу число: ")))
# from math import(pi, floor, sin, cos)
#
# print(cos(0.5))
# print(pi)
# print(sin(0.5))
import sys
print(sys.path)

# C:\Python32\Lib\site-packages
# Создем файл с  расширением .pth и прописываем там пути где искать модули
# Пример содержимого test.pth:
# C:\folder1
# C:\folder2
# C:\folderN
# Варианты подключения пакетов:
# from my_package import *
# Каталоги разделяются точками
# from my_package.sub_package import *
#
# Чтобы поключить модуль распооженный в той же папке внутри пакета можно использовать относительный импорт:
# from . import module2
# Или указать полный путь относительно корниевого каталога
# import folder1.folder2.module2 as module2
