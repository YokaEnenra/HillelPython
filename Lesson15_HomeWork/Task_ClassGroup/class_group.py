class NumberIsZeroOrNegative(Exception):
    def __str__(self):
        return "Указанное вами число студентов равно 0 или отрицательное"


class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def grades_changer(self, new_grades: list):
        self.grades = new_grades

    def age_changer(self, new_age: int):
        self.age = new_age

    def name_changer(self, new_name: str):
        self.name = new_name


class Group:
    students_list = list()

    def __init__(self, students_counter: int):
        for i in range(students_counter):
            while True:
                try:
                    name = input(f"Укажите имя {i + 1} студента: ")
                    age = int(input(f"Укажите возраст {i + 1} "
                                    f"студента числом: "))
                    grades = (input(
                        f"Укажите оценки {i + 1} "
                        f"студента через пробел: ")).split()
                    for j in range(len(grades)):
                        grades[j] = int(grades[j])
                except ValueError:
                    print("Вы ввели не число или дробное число")
                else:
                    self.students_list.append(Student(name, age, grades))
                    break

    def std_grades_changer(self):
        while True:
            try:
                student_number = int(input("Выберите номер студента "
                                           "для изменения оценок: ")) - 1
                new_grades = (input(
                    f"Укажите новые оценки для {student_number + 1} "
                    f"студента через пробел: ")).split()
                for i in range(len(new_grades)):
                    new_grades[i] = int(new_grades[i])
            except ValueError:
                print("Вы ввели не число или дробное число")
            else:
                self.students_list[student_number].grades_changer(new_grades)
                print(f"Оценки {student_number + 1} студента изменены")
                break

    def std_age_changer(self):
        while True:
            try:
                student_number = int(input("Выберите номер студента "
                                           "для изменения возраста: ")) - 1
                new_age = int(input(f"Укажите новый возраст для "
                                    f"{student_number + 1} студента числом: "))
            except ValueError:
                print("Вы ввели не число или дробное число")
            else:
                self.students_list[student_number].age_changer(new_age)
                print(f"Возраст {student_number + 1} студента изменен")
                break

    def std_name_changer(self):
        while True:
            try:
                student_number = int(input("Выберите номер студента "
                                           "для изменения возраста: ")) - 1
                new_name = input(f"Укажите новое имя для "
                                 f"{student_number + 1} студента числом: ")
            except ValueError:
                print("Вы ввели не число или дробное число")
            else:
                self.students_list[student_number].name_changer(new_name)
                print(f"Имя {student_number + 1} студента изменено")
                break

    def stds_printer(self):
        for i in range(len(self.students_list)):
            print(f"{i + 1}) \nИмя:{self.students_list[i].name}\n"
                  f"Возраст:{self.students_list[i].age}\n"
                  "Оценки:", end="")
            for j in self.students_list[i].grades:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    print("Эта программа создает список студентов группы "
          "и позволяет управлять записью")
    try:
        stds_number = int(input("Укажите кол-во студентов в группе: "))
        if stds_number <= 0:
            raise NumberIsZeroOrNegative
    except ValueError:
        print("Вы ввели не число или дробное число")
    except NumberIsZeroOrNegative as err:
        print(err)
    else:
        first_group = Group(stds_number)
        while True:
            try:
                print("Выберите действие:\n1) Вывести всех студентов группы\n"
                      "2) Изменить имя студента\n"
                      "3) Изменить возраст студента\n"
                      "4) Изменить оценки студента\n"
                      "5) Конец работы")
                usr_choice = int(input("Ваш выбор: "))
            except ValueError:
                print("Вы ввели не число или дробное число")
            else:
                if usr_choice == 1:
                    first_group.stds_printer()
                elif usr_choice == 2:
                    first_group.std_name_changer()
                elif usr_choice == 3:
                    first_group.std_age_changer()
                elif usr_choice == 4:
                    first_group.std_grades_changer()
                elif usr_choice == 5:
                    break
                else:
                    print("Выбранного варианта не существует")
