# 그룹 단어 체커
answer = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        answer += 1
print(answer)