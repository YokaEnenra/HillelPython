with open('data.txt', 'r+') as f:
    my_text = f.read()
my_dict = dict()
my_list = list(my_text.split())
for i in range(len(my_list)):
    my_list[i] = my_list[i].lower()
    if ',' in my_list[i]:
        my_list[i] = my_list[i].replace(',', '')
    elif '.' in my_list[i]:
        my_list[i] = my_list[i].replace('.', '')
for i in range(len(my_list)):
    if my_list[i] not in my_dict:
        counter = my_list.count(my_list[i])
        my_dict.update({counter: my_list[i]})
keys_list = list(my_dict.keys())
keys_list = sorted(keys_list)
biggest_key = int(keys_list[-1])
print('Слово встречающееся в полученном тексте больше всего раз найдено, я выведу его в формате "кол-во раз: слово"\n'
      , str(biggest_key) + ': ' + my_dict.get(biggest_key))
