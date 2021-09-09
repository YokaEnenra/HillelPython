f = open("src_14.txt", "r+", encoding="windows-1251")
class_counter = 0
file_data = list()
for i in f:
    file_data.append(i.split())
    class_counter += 1
f.close()
pupils = list()
for i in range(len(file_data)):
    pupils.append(list())
    line_storage = file_data[i]
    for j in range(3):
        if j == 0:
            line_storage[j] = line_storage[j][0]
            line_storage[j] += '.'
            pupils[i].append(line_storage[j])
        elif j == 1:
            pupils[i].append(line_storage[j])
            pupils[i][j], pupils[i][j - 1] = pupils[i][j - 1], pupils[i][j]
        else:
            tmp = int()
            for n in range(j, len(line_storage)):
                tmp += int(line_storage[n])
            tmp /= (len(line_storage) - j)
            pupils[i].append(round(tmp, 2))
print("Учащиеся со средним баллом ниже 5:")
class_middle_mark = float()
f = open("class_info.txt", "w")
for i in pupils:
    class_middle_mark += i[2]
    tmp = str()
    tmp += i[0] + ' ' + i[1]
    for j in range(len(tmp), 20):
        tmp += ' '
    tmp += str(i[2])
    f.write(tmp + '\n')
    if i[2] < 5:
        print(tmp)
f.close()
class_middle_mark /= class_counter
print("\nСредний балл класса:", round(class_middle_mark, 2))
