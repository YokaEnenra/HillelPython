print("Приветствую тебя, пользователь, к сожалению я не могу пустить тебя дальше, без ввода пароля")
receivedpass = input()
usrpass = {"IAmTheLaw","KingGeorge","GonFricks"}
if(receivedpass in usrpass):
    print("Доступ подтвержден, отправляю тебя на сервер")
else:
    print("Твой пароль недействителен! Если это не так, обратись к системному администратору")
