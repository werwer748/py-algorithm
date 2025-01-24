'''
봉우리
'''
import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
# 네방향 초기화
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)

'''
# 내 풀이
n = int(input())
a = [[0] * (n + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 2)]

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        t = a[i][j]
        up = a[i - 1][j]
        right = a[i][j + 1]
        down = a[i + 1][j]
        left = a[i][j - 1]

        if t > up and t > right and t > down and t > left:
            cnt += 1

print(cnt)
'''
