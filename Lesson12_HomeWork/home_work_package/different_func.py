"""Этот модуль представляет 3 уникальные ф-кции:
    1) Смена значений между двумя численными элементами
    2) Проверка вводимого пароля
    3) Поиск всех автоморфных чисел до указанной границы"""

__all__ = ["data_switcher", "password_checker", "automorphic_numbers"]


def data_switcher(x: float, y: float):
    """Эта ф-кция принимает параметрами два числа и затем меняет их местами
    вызов ф-кции осуществляется вот так: x,y = data_switcher(x,y)"""
    x += y
    y = x - y
    x -= y
    return x, y


def password_checker() -> bool:
    """Эта ф-кция првоеряет пароль пользователя и возвращает True или False
    в зависимости от результата проверки, не принимает никаких параметров """
    print("Приветствую тебя, пользователь, к сожалению я не могу пустить "
          "тебя дальше, без ввода пароля")
    received_pass = input("Введи пароль: ")
    usr_pass = {"IAmTheLaw", "KingGeorge", "GonFriсs"}
    if received_pass in usr_pass:
        print("Доступ подтвержден, отправляю тебя на сервер")
        return True
    else:
        print("Твой пароль недействителен! Если это не так, обратись "
              "к системному администратору")
        return False


def automorphic_numbers():
    """Эта ф-кция выводит все автоморфные числа до указанной границы,
    не принимает никаких параметров и ничего не
    возвращает """
    print("Приветствую, укажи натуральное число и я выведу все автоморфные "
          "числа, что стоят до него")
    str_number = input()
    try:
        int_number = int(str_number)
        for i in range(1, int_number):
            pow_i = i ** 2
            str_pow = str(pow_i)
            str_i = str(i)
            len_i = len(str_i)
            len_pow = len(str_pow)
            count = 0
            n = 0
            for j in range(len_pow - len_i, len_pow):
                if str_pow[j] == str_i[n]:
                    count += 1
                    n += 1
                else:
                    break
            if count == len_i:
                print(i, "*", i, "=", pow_i)
    except ValueError:
        print("Твое число", str_number, "не является натуральным или "
                                        "вообще не число")


if __name__ == "__main__":
    x = 3
    y = 5
    print(x, y)
    x, y = data_switcher(x, y)
    print(x, y)
    password_checker()
    automorphic_numbers()
