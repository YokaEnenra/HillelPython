import random

print(
    'Приветствую вас в игре "Угадайка", я загадаю число от 1 до 100, а вы должны угадать это число, я буду давать '
    'подсказки')
is_game=True
while is_game:
    is_win = False
    right_answer = random.randint(1, 100)
    loose_counter = 1
    while not is_win:
        print("И так, твой ответ?")
        try:
            usr_answer = int(input())
            if right_answer == usr_answer and loose_counter == 1:
                print("Ты угадал с первой попытки, ничего себе, я удивлён, правильным числом было", right_answer)
            elif right_answer == usr_answer:
                print("Ты угадал, победа за тобой, это заняло у тебя", loose_counter,
                      "попыток, а правильным числом было", right_answer)
                is_win=True
            else:
                if usr_answer > right_answer:
                    print("Твое число больше, чем то, что я загадал")
                else:
                    print("Твое число меньше, чем то, что я загадал")
            loose_counter += 1
        except:
            print("Ты ввел не число или дробное число")
            loose_counter += 1
    print('Хочешь сыграть еще? "y-да" "n-нет"')
    usr_answer = input()
    if usr_answer == 'n':
        print("Ок, завершаю работу")
        is_game=False
    elif usr_answer != 'n' and usr_answer != 'y':
        print('Не хотел играть, написал бы "n", зачем билиберду писать')
        is_game = False
    else:
        print("Ок, продолжаем")
