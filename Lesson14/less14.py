fid = open(r'buratino.txt', 'w')
fid.writelines(['-"Стража"\n', 'Вскричал карабас.\n', '-"Ловите мальчишку!"'])
fid.close()
fid = open(r'buratino.txt', 'r')
print(fid.read())

