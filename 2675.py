# 문자열 반복
n = int(input())
for i in range(n):
    k = []
    a, b = input().split()
    a = int(a)
    b = str(b)

    for j in range(len(b)):
        c = b[j]*a
        k.append(c)

    answer = k[0]
    for m in range(1, len(b)):
        answer += k[m]
    print(answer)