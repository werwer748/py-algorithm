# 대표값 문제 오류 수정(round는 round_half_even 방식을 채택함??)
'''
round_half_up: 이 우리가 흔히 생각하는 반올림(4이하는 버리고 5이상은 올리는 방법)
round_half_even: 4.500을 round로 감싸면 5가아닌 4가 나옴(짝수쪽으로 근사값을 준다.)
앞이 짝수면 5를 버리고 앞이 홀수면 올라가는듯?
a=4.500
print(round(a)) # 6
'''
# a = 66.5
# a = a + 0.5 # 0.5를 더해서 소수점이 0.5이상인경우 1이 더해지게끔한다.
# a = int(a) # int로 변환시켜 소수점을 떨어낸다.
# print(a)

'''대표값'''
import sys
sys.stdin = open("in1.txt", "rt")

'''
# 내 풀이 - 오류 수정 적용
n = int(input())
points = list(map(int, input().split()))
avg = (sum(points) / n) + 0.5
avg = int(avg)

temp = max(points)
student = 0
for x in enumerate(points):
    absTemp = abs(avg - x[1])
    if temp == absTemp:
        if x[1] > points[student]:
            student = x[0]
    if temp > absTemp:
        student = x[0]
        temp = absTemp

studentNum = student + 1
print(avg, studentNum)
'''


# 강사풀이 - 오류 수정 적용
n = int(input())
a = list(map(int, input().split()))

ave = (sum(a)/n) + 0.5
ave = int(ave)
min = 2147000000 # 4바이트 최대 정수
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)



