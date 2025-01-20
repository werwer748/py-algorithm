'''
격자판 최대합
N*N의 격자판이 주어지면 각 행의 합, 각 열의합, 두 대각선의 합 중 가장 큰 합을 출력해라
'''
import sys
sys.stdin = open("in5.txt", "rt")

# 강사풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -float("inf")

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 행
        sum2 += a[j][i] # 열
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
# 내 풀이
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

res = 0
row = 0
col = 0
col_list = [0] * n
leftDash = 0
rightDash = 0

for i in range(n):
    sumRow = sum(board[i])
    if row < sumRow:
        row = sumRow

    for j in range(n):
        col_list[j] += board[i][j]
        if i == j:
            leftDash += board[i][j]
            rightDash += board[i][j-1]
else:
    col = max(col_list)

print(max([row, col, leftDash, rightDash]))
'''