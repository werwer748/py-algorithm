'''
봉우리
'''
import sys
sys.stdin = open("in5.txt", "rt")

# 강사 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)

'''
# 내 풀이
n = int(input())
a = [[0] * n] + [list(map(int, input().split())) for _ in range(n)] + [[0] * n]

def add_zero(x):
    x.insert(0, 0)
    x.append(0)

list(map(add_zero, a))

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        tmp = a[i][j]
        comp = [a[i - 1][j], a[i][j + 1], a[i + 1][j], a[i][j - 1]]
        if tmp > max(comp):
            cnt += 1

print(cnt)
'''




