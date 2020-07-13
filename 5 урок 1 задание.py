filename = input('Файл: ')
f = open(filename,'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()