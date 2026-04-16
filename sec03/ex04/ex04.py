'''
두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
'''
import sys
sys.stdin = open("in1.txt", "rt")

'''
# 내 풀이 2 - pop 들어가면 속도면에서 처진다
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

res = []

while a1 or a2:
    if a1 and a2:
        if a1[0] >= a2[0]:
            res.append(a2.pop(0))
            continue
        if a2[0] >= a1[0]:
            res.append(a1.pop(0))
    if not a1 and a2:
        res += a2
        break
    if not a2 and a1:
        res += a1
        break

print(" ".join(map(str, res)))
'''


# 강사 풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0

c = []

while p1 < n and p2 < m:
    if a[p1] >= b[p2]:
        c.append(b[p2])
        p2 += 1
    else:
        c.append(a[p1])
        p1 += 1

if p1 < n:
    c += a[p1:]
if p2 < m:
    c += b[p2:]

print(" ".join(map(str, c)))

#     if a[p1] <= b[p2]:
#         c.append(a[p1])
#         p1 += 1
#     else:
#         c.append(b[p2])
#         p2 += 1
# if p1 < n:
#     c = c + a[p1:]
# if p2 < m:
#     c = c + b[p2:]
#
# for x in c:
#     print(x, end=" ")


'''
# 내 풀이
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

res = []

p1 = 0
p2 = 0

while len(res) < (n1 + n2):
    if a1[p1] > a2[p2]:
        res.append(a2[p2])
        p2 += 1
    else:
        res.append(a1[p1])
        p1 += 1

    if p1 == len(a1) and p2 < len(a2):
        res = res + a2[p2::]
    elif p1 < len(a1) and p2 == len(a2):
        res = res + a1[p1::]

print(" ".join(map(str, res)))
'''

'''
# 떠오르는데로 그냥 풀면...
# sort 가 nlogn번 도는데 더 빠르게 정렬하는 방법을 사용해 풀어야한다고 함.
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

sumA = a1 + a2
sumA.sort()
for x in sumA:
    print(x, end=' ')
'''