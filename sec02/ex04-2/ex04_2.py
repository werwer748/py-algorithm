# 대표값 문제 오류 수정(round는 round_half_even 방식을 채택함??)
'''
round_half_up: 이 우리가 흔히 생각하는 반올림(4이하는 버리고 5이상은 올리는 방법)
round_half_even: 4.500을 round로 감싸면 5가아닌 4가 나옴(짝수쪽으로 근사값을 준다.)
앞이 짝수면 5를 버리고 앞이 홀수면 올라가는듯?
a=4.500
print(round(a)) # 6

a = 66.5
a = a + 0.5 # 0.5를 더해서 소수점이 0.5이상인경우 1이 더해지게끔한다.
a = int(a) # int로 변환시켜 소수점을 떨어낸다.
print(a)
'''





'''
대표값
N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''
import sys
sys.stdin = open("in1.txt", "rt")


n = int(input())
scores = list(map(int, input().split()))

avg = int((sum(scores) / n) + 0.5)
tmp = float('inf')
res = 0
score = 0

for (i, x) in enumerate(scores):
    diff = abs(avg - x)

    if diff < tmp:
        tmp = diff
        res = i + 1
        score = x
    elif diff == tmp and score < x:
        res = i + 1
        score = x


print(avg, res, sep=" ")

'''
n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/n + 0.5)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
'''