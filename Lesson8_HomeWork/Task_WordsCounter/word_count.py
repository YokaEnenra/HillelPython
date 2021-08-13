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

for i in range(len(my_list)):
    if my_list[i] not in my_dict:
        counter = my_list.count(my_list[i])
        my_dict.update({my_list[i]: counter})
print('Все слова в переданном тексте посчитаны сейчас я выведу результат в формате "слово: кол-во раз"\n', my_dict)
