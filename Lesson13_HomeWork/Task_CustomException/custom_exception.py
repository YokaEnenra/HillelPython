class DontLikedNumber(Exception):
    def __str__(self):
        return "Это число не подходит, число должно быть больше 5"


try:
    number = int(input("Введи любое число больше 5: "))
    if number in range(1, 6):
        raise DontLikedNumber
except ValueError as err:
    print(f"Я же просил число\n{err}")
except DontLikedNumber as err:
    print(err)
