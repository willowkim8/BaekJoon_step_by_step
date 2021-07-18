# 단어 공부 1157
# 틀은 짜졌는데 모르겠어서 구글링함
a = input()
a = a.upper()
a_list = list(set(a))
cnt = []

for i in a_list:
    count = a.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')

else:
    print(a_list[cnt.index(max(cnt))].upper())


# if max(a)가 여러개이면 :
    # print('?')
# else:
    # # print(max(a))