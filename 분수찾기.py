n = int(input())
line = 0 # 사선 라인
max_num = 0 # 라인에서 가장 큰수
while n > max_num:
    line += 1
    max_num += line

gap = max_num - n # 이게 뭐지
if line % 2 == 0: # 짝수일 때
    top = line -gap
    under = gap - 1
else: # 홀수일 때
    top = gap + 1
    under = line - gap

print(f'{top}/{under}')
'''
처음 계획부터 틀린 문제
짝수 라인과 홀수 라인 자체를 생각을 못했다.
그 이유는 max_num을 생각하지 못했기 때문이다.
'''