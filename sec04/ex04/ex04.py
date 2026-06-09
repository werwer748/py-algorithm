"""
# 마구간 정하기(결정알고리즘)
N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다. 각 마구간에는 한 마리의 말만 넣을 수 있고,
가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

# 입력 설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

# 출력 설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.
"""

import sys
sys.stdin = open("in5.txt", "rt")

# 내 풀이2
house, horse = map(int, input().split())
dis = [int(input()) for _ in range(house)]
dis.sort() # 굳이 정렬함수 직접 짜는것보다 있는거 활용하는게 좋다고 함
res = 0
# lp = dis[0]
lp = 1 # --> 무조건 0번쨰부터 다음번째의 거리가 최소라고 생각하면 안된다.
rp = dis[house - 1]

def mid_checker(mid):
    # tmp = 0
    last = dis[0] # --> 메모리 성능(언어에따라 차이), 실수 가능성 고려시!
    cnt = 1
    checker = False

    for i in range(1, house):
        if mid <= dis[i] - last:
            cnt += 1
            last = dis[i]
        if cnt >= horse:
            checker = True
            break
    return checker


while lp <= rp:
    mid = (lp + rp) // 2

    if mid_checker(mid):
        lp = mid + 1
        if res < mid:
            res = mid
    else:
        rp = mid - 1

print(res)
# 1 2 4 8 9

'''
# 강사 풀이
n, c = map(int, input().split())
Line = []

def Count(len):
    cnt = 1
    ep = Line[0]

    for i in range(1, n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()

lt = 1
rt = Line[n - 1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
'''

'''
# 내 풀이
def i_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]


lt = a[0]
rt = a[n - 1]
cen = i_sort(a)
res = 0

def center_checker(m, hor):
    np = 0

    for i in range(1, len(cen)):
        if cen[i] - cen[np] >= m:
            hor -= 1
            np = i

    return hor


while lt <= rt:
    mid = (lt + rt) // 2

    horses = center_checker(mid, c - 1)

    if horses <= 0:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
'''