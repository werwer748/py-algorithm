'''
수들의 합

N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2],...
A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
,
'''
import sys
sys.stdin = open("in4.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))


# 내 풀이3
cnt = lp = 0
rp = 1
s = a[lp]

while True:
    if s < m:
        if rp < n:
            s += a[rp]
            rp += 1
        else:
            break
    elif s > m:
        s -= a[lp]
        lp += 1
    else:
        cnt += 1
        s -= a[lp]
        lp += 1

print(cnt)


'''
# 내 풀이2
cnt = 0
lp = 0
rp = 1
m_checker = a[lp]

while True:
    if m_checker < m:
        if rp < n:
            m_checker += a[rp]
            rp += 1
        else:
            break
    elif m_checker > m:
        lp += 1
        rp = lp + 1
        m_checker = a[lp]
    else:
        cnt += 1
        lp += 1
        rp = lp + 1
        m_checker = a[lp]

print(cnt)
'''


'''
# 강사 풀이
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
'''

'''
# 내 풀이
lp = 0
cnt = 0

while lp < n:
    tmp = 0

    for j in range(lp, n):
        if tmp == m or tmp > m:
            break
        else:
            tmp += a[j]
    if tmp == m:
        cnt += 1
    lp += 1

print(cnt)
'''
