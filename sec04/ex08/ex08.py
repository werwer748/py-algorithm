"""
침몰하는 타이타닉

유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 있습니다.
구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있 으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

#! 입력설명
첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다. 각 승객의 몸무게는 M을 넘지는 않습니다.
즉 탈출을 못하는 경우는 없습니다.

#! 출력설명
첫째 줄에 구명보트의 최소 개수를 출력합니다.
"""
import sys
from collections import deque
sys.stdin = open("in3.txt")


# 강사 풀이2 => 성능 개선!
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p) #* deque라는 자료구조로 만든다.
cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft() #? 첫 번쨰 요소 제거
        p.pop()
        cnt += 1

print(cnt)

"""
# 강사 풀이
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0

#? while list: => 리스트가 비면 멈춘다!
#? pop은 성능상 좋지 못함.
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.pop(0)
        p.pop()
        cnt += 1

print(cnt)
"""

"""
# 내 풀이
n, m = map(int, input().split()) #* n: 승객 수, m: 보트 무게 제한
a = list(map(int, input().split())) #* 승객들 몸무게
a.sort()

boat = 0
lt = 0
rt = n - 1
while lt <= rt:
    boat += 1
    temp = a[lt] + a[rt]
    if temp <= m:
        lt += 1
        rt -= 1
    else:
        rt -= 1


print(boat)
"""