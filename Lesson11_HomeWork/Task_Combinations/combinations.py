def without_00(zero_number: int, unit_number: int):
    if zero_number > unit_number + 1:
        return 0
    if zero_number == 0 or unit_number == 0:
        return 1
    return without_00(zero_number, unit_number - 1) + without_00(
        zero_number - 1, unit_number - 1)


print(without_00(int(input("Укажите кол-во нулей: ")),
                 int(input("Укажите кол-во единиц: "))))
