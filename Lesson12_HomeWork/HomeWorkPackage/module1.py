def data_switcher(x: float, y: float):
    x += y
    y = x - y
    x -= y
    return x, y


def password_checker():
    print("Приветствую тебя, пользователь, к сожалению я не могу пустить тебя дальше, без ввода пароля")
    received_pass = input("Введи пароль: ")
    usr_pass = {"IAmTheLaw", "KingGeorge", "GonFricks"}
    if received_pass in usr_pass:
        print("Доступ подтвержден, отправляю тебя на сервер")
    else:
        print("Твой пароль недействителен! Если это не так, обратись к системному администратору")


def automorhic_numbers():
    print("Приветствую, укажи натуральное число и я выведу все автоморфные числа, что стоят до него")
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
        print("Твое число", str_number, "не является натуральным или вообще не число")


if __name__ == "__main__":
    x = 3
    y = 5
    print(x, y)
    x, y = data_switcher(x, y)
    print(x, y)
    password_checker()
    automorhic_numbers()
