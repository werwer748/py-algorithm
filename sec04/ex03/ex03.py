"""
뮤직비디오(결정알고리즘)
"""
import sys
sys.stdin = open("in5.txt", "rt")

#! 못풀어서 강의보고 클론코딩... 문제 이해가 어려움
n, m = map(int, input().split()) # n = 부른 곡수, m = 소속사에서 찍어내려는 DVD 개수
music = list(map(int, input().split()))
max_m = max(music)

lt = 1
rt = sum(music)
res = 0

def checker(capacity):
    cnt = 1
    dvd_sum = 0
    for x in music:
        if dvd_sum + x > capacity:
            cnt += 1
            dvd_sum = x
        else:
            dvd_sum += x
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_m and checker(mid) <= m:
        res = mid
        rt = mid - 1 # 더 작은 범위 탐색
    else:
        lt = mid + 1
print(res)




