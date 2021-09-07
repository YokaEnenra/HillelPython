f = open("user_data.txt", "a")
while True:
    data = input()
    if data == '':
        break
    f.write(data + '\n')
f.close()
