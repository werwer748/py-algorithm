'''
반복문을 이용한 문제 풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
'''

n = int(input("정수입력: "))

''' 내 풀이
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i)
'''
# 강사 풀이
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

# 내 풀이 == 강사 풀이
sum = 0
for i in range(1, n + 1):
    sum += i
else: # 하나의 구조안에서 끝내기(혼자 해본거)
    print(sum)

# 내 풀이 == 강사 풀이
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')