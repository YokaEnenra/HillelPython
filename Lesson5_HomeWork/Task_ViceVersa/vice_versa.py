print("Приветствую, в ViceVersaWriting4000, запиши мне словосочетание и я полностью переверну его")
try:
    first_word, second_word, *tmp = input().split()
    new_second_word = second_word[::-1]
    new_second_word = new_second_word.lower()
    new_second_word = new_second_word.replace(new_second_word[0],new_second_word[0].upper())
    new_first_word = first_word[::-1]
    new_first_word = new_first_word.lower()
    new_first_word = new_first_word.replace(new_first_word[0],new_first_word[0].upper())
    print('"' + new_second_word, new_first_word + '"')
except:
    print("Кажется ты ввел меньше двух слов")
