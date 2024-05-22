'''
수들의 합

N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
sys.stdin = open("in5.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 강사 풀이 - 연산 속도 훨씬 빠름
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
        tot -= a[lt] # tot 하고 lt 싱크맞추는 용도
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)

'''
# 내 풀이... 뭔가 잘못됨
lt = 0
rt = 0
cnt = 0
# tot = a[0]
a = a + [0]

# for i in range(n):
for i in range(n):
    tot = a[i]
    for j in range(i + 1, n + 1):
        if tot == m:
            cnt += 1
            break
        elif tot < m:
            tot = tot + a[j]
        else:
            break

print(cnt)
'''

