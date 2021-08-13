with open('data.txt', 'r+') as f:
    my_text = f.read()
my_dict = dict()
my_list = list(my_text.split())
banned_list = (',', '.', '!', '?', ':', ';')
for i in range(len(my_list)):
    my_list[i] = my_list[i].lower()
    for j in banned_list:
        if j in my_list[i]:
            my_list[i] = my_list[i].replace(j, '')
for i in my_list:
    if i not in my_dict:
        counter = my_list.count(i)
        my_dict.update({i: counter})
biggest_amount = {'0': 0}
biggest_amount_key = '0'
for i in my_dict:
    if my_dict.get(i) > biggest_amount.get(biggest_amount_key):
        biggest_amount = biggest_amount.clear()
        biggest_amount = {i: my_dict.get(i)}
        biggest_amount_key = i
print('Слово встречающееся в полученном тексте больше всего раз найдено, я выведу его в формате "слово: кол-во раз"\n'
      , biggest_amount)
