'''
격자판 최대합
N*N의 격자판이 주어지면 각 행의 합, 각 열의합, 두 대각선의 합 중 가장 큰 합을 출력해라
'''
import sys
sys.stdin = open("in5.txt", "rt")

# 내 풀이2
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

row = 0
column = 0
leftDash = 0
rightDash = 0

for i in range(n):
    leftDash += a[i][i]
    rightDash += a[i][i - i - 1]
    sumRow = sumCol = 0
    for j in range(n):
        sumRow += a[i][j] # 행(가로, row) 더하기
        sumCol += a[j][i] # 열(세로, column) 더하기
    if row < sumRow:
        row = sumRow
    if column < sumCol:
        column = sumCol
else:
    print(max([row, column, leftDash, rightDash]))

'''
# 강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # n 행 만큼 읽어와서 리스트화시킴...

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 행(가로, row) 더하기
        sum2 += a[j][i] # 열(세로, column) 더하기
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)
'''

'''
# 내 풀이
n = int(input())
width = 0
height = [0] * n
left = 0
right = 0

for i in range(n):
    a = list(map(int, input().split()))
    tmp = sum(a)
    left += a[i]
    right += a[n - (i + 1)]
    if width < tmp:
        width = tmp
    for j in range(n):
        height[j] += a[j]

result = [width, left, right] + height

print(max(result))
'''