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
        my_dict.update({my_list[i]: counter})
print('Все слова в переданном тексте посчитаны сейчас я выведу результат в формате "слово: кол-во раз"\n', my_dict)
