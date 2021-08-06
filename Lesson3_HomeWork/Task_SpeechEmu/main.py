import random

print('Приветствую, моё имя "Мистер Ди", а тебя как зовут?')
Name = input()

while (True):
    print('Привет "' + Name + '", меня создали 2 года назад, получается мой возраст 2 года, а твой?')
    AgeStr = input()
    try:
        AgeInt = int(AgeStr)
        break
    except:
        print("Кажется ты ввел не число")

if (AgeInt > 2 & AgeInt - 2 < 10):
    print("Это получается если тебе " + AgeStr + " лет, то ты старше меня на", AgeInt - 2)

elif (AgeInt < 2):
    print("Это получается если тебе " + AgeStr + " лет, то ты младше меня на", 2 - AgeInt)

else:
    print("Это получается если тебе " + AgeStr + " лет, мы с тобой одногодки")

while (True):
    print("Хочешь сыграем в игру? y-да,n-нет")
    Answer = input()
    if (Answer == "y"):
        while (True):
            print("Сейчас я загадаю число от 1 до 10, отгадаешь какое, ты победил")
            print("Загадал, ииииии, твой ответ?")
            try:
                GameAnswer = int(input())
                BotQuestion = random.randint(1, 10)
                if (GameAnswer == BotQuestion):
                    print("Ты победил! Хочешь сыграть еще? y-да,n-нет")
                    RestartAnswer = input()
                    if (RestartAnswer == "n"):
                        break
                    elif (RestartAnswer != "y"):
                        print("Не хочешь играть так и скажи, зачем писать какую-то билиберду")
                        break
                else:
                    print("Не угадал, моё число было",BotQuestion,"а ты сказал",GameAnswer,"хочешь сыграть еще? y-да,n-нет")
                    RestartAnswer = input()
                    if (RestartAnswer == "n"):
                        break
                    elif(RestartAnswer!="y"):
                        print("Не хочешь играть так и скажи, зачем писать какую-то билиберду")
                        break
            except:
                print("В ответе должно быть число")
        break

    elif (Answer == "n"):
        break

    else:
        print("Не хочешь играть так и скажи, зачем писать какую-то билиберду")
        break

print("Приятно было познакомиться, я бы с радостью продолжил общение, но моя батарея уже на пределе, еще увидимся")
