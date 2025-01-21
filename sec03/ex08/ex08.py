'''
곳감(모래시계)
'''
import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 강사 풀이
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0))
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

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
for i in range(m):
    target, lr, ran = map(int, input().split())
    target_list = a[target - 1][:]
    for j in range(ran):
        if lr == 0:
            target_list.append(target_list[0])
            target_list.pop(0)
        else:
            target_list.insert(0, target_list[-1])
            target_list.pop()
    a[target - 1] = target_list

start = 0
end = n
res = 0

for i in range(n):
    for j in range(start, end):
        res += a[i][j]
    if i < n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(res)
'''