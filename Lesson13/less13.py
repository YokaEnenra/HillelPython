class LeErr(Exception):
    def __str__(self):
        return "Ты шо, дурачек?"


try:
    raise LeErr
except LeErr as err:
    print(err)

# Чекнуть конструкию with as
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Строка\n")  # Запсываем строку в конец файла
