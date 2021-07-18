# 크로아티아 알파벳
chrt = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in chrt:
    word = word.replace(i,'*')
print(len(word))