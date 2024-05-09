'''대표값'''
import sys
sys.stdin = open("in3.txt", "rt")

'''
# 내 풀이
n = int(input())
points = list(map(int, input().split()))
avg = round(sum(points) / n)

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

# 강사풀이
n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a)/n)
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