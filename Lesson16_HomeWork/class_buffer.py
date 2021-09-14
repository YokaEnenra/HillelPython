class Buffer:

    def __init__(self):
        self.sequence = list()

    def add(self, *a):
        for i in a:
            self.sequence.append(i)

    def get_current_part(self):
        if len(self.sequence) > 4:
            curr_sum = 0
            for i in range(0, 5):
                curr_sum += self.sequence[0]
                self.sequence.pop(0)
            return curr_sum
        # вернуть сохраненные в текущий момент элементы последовательности
        # в порядке, в котором они были добавлены


class StopCommand(Exception):
    def __str__(self):
        return "Работа завершена"


if __name__ == "__main__":
    print("Проверка класса Buffer")
    first_buffer = Buffer()
    while True:
        print('Введите "stop" чтобы завершить работу')
        try:
            data = input("Укажите новые елементы последовательности "
                         "через пробел: ")
            if 'stop' in data:
                raise StopCommand

            else:
                data_list = data.split()
                for i in range(len(data_list)):
                    data_list[i] = float(data_list[i])
                if '' not in data_list:
                    first_buffer.add(*data_list)
                result = first_buffer.get_current_part()
                if result is None:
                    print("В последовательности меньше пяти чисел")
                else:
                    print("Сумма первых пяти чисел:", result)

        except ValueError:
            print("Вы ввели не число")
        except StopCommand as err:
            print(err)
            break
