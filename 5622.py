# 다이얼
dial = ['ABC', 'DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']
cha = input()

num = 0
for i in range(len(cha)):
    for j in dial:
        if cha[i] in j:
            num = num + dial.index(j) + 3
print(num)