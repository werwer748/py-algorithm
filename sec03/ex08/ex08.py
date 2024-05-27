'''
곳감(모래시계)
'''
import sys
sys.stdin = open("in1.txt", "rt")

# 강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())

    if t == 0: # 왼쪽
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n - 1

for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)

'''
# 내 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    position, lr, count = map(int, input().split())
    position -= 1
    for j in range(count):
        if lr == 0:
            a[position].append(a[position][0])
            a[position].pop(0)
        else:
            a[position].insert(0, a[position][n - 1])
            a[position].pop()



res = 0
s = 0
e = n

for i in range(n):
    ary = a[i]
    for j in range(s, e):
        res += ary[j]
    if i < (n // 2):
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
'''