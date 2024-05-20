'''
두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
'''
import sys
sys.stdin = open("in1.txt", "rt")

# 강사풀이
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c +b[p2:]

for x in c:
    print(x, end=' ')

'''
# 내 풀이
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

point1 = 0
point2 = 0
result = []

print(a1[point1], a2[point2])

for i in range(n1 + n2):
    if point1 >= n1:
        result = result + a2[point2:]
        break
    if point2 >=n2:
        result = result + a1[point1:]
        break
    if a1[point1] <= a2[point2]:
        result.append(a1[point1])
        point1 += 1
    else:
        result.append(a2[point2])
        point2 += 1

resultToString = ' '.join(map(str, result))
sys.stdin = open("out1.txt", "rt")
out = input()

if out == resultToString:
    print('Success')
else:
    print('Failure')
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
