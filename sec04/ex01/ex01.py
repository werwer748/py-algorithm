"""
이분 검색
임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
단 중복값은 존재하지 않습니다.

입력 설명
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다. 두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.
"""
import sys
sys.stdin = open("in5.txt", "rt")

# 내 풀이2-2
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lp, rp = 0, n - 1
res = -1  # 못 찾았을 때를 명시적으로 표현

while lp <= rp:
    cp = (lp + rp) // 2
    if a[cp] == m:
        res = cp + 1
        break
    elif a[cp] < m:
        lp = cp + 1
    else:
        rp = cp - 1
print(res) # 0 대신 -1이면 못 찾은 것

'''
# 내 풀이2-1
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lp, rp = 0, n - 1
result = 0

while lp <= rp:
    if a[lp] == m:
        result = lp
        break
    else:
        lp += 1
    if a[rp] == m:
        result = rp
        break
    else:
        rp -= 1

print(result + 1)
'''

'''
# 재풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] < m:
        lt = mid + 1 # mid도 체크한 숫자니까 포함해서 작은 범위 버리기
    else:
        rt = mid - 1 # mid도 체크한 숫자니까 포함해서 큰 범위 버리기
'''


"""
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

"""
# 내 풀이 (이분검색 모름)
n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
findM = a.index(m)
print(findM + 1)
"""


