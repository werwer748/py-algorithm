"""
이분 검색
"""
import sys
sys.stdin = open("in5.txt", "rt")

# 이분검색? => 검색범위를 절반씩 잘라서 없애는거..? logN번만에 해결된다 함.
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort() # 오름차순 정렬
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

"""
# 내 풀이 (이분검색 모름)
n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
findM = a.index(m)
print(findM + 1)
"""


