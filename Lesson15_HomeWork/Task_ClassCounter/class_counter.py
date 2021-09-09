class CustomCounter:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val
        self.curr_val = min_val

    def get_val(self):
        return self.curr_val

    def increment_val(self):
        if self.curr_val < self.max_val:
            self.curr_val += 1
        return self.curr_val


class MinMoreThanMax(Exception):
    def __str__(self):
        return "Введенный вами минимум больше максимума"


if __name__ == "__main__":
    try:
        print("Эта программа создате счетчик от числа до числа")
        set_min_val = int(input("Введите минимальное значение счетчика: "))
        set_max_val = int(input("Введите максимальное значение счетчика: "))
        if set_min_val > set_max_val:
            raise MinMoreThanMax
        else:
            first_counter = CustomCounter(set_min_val, set_max_val)
            while True:
                print("Выберите действие:\n1) Прибавить счетчик\n"
                      "2) Вывести текущее значение счетчика\n"
                      "3) Конец работы")
                usr_choice = int(input("Ваш выбор: "))
                if usr_choice == 1:
                    print(first_counter.increment_val())
                elif usr_choice == 2:
                    print(first_counter.get_val())
                elif usr_choice == 3:
                    break
                else:
                    print("Выбранного варианта не существует")
    except ValueError:
        print("Вы ввели дробное число или не число вовсе")
    except MinMoreThanMax as err:
        print(err)
