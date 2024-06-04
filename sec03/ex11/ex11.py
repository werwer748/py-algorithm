'''
격자판 회문수
'''
import sys
sys.stdin = open("in5.txt", "rt")

# 강사 풀이
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

'''
# 내 풀이
n = 7
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if j < 3:
            tempRow = []
            tempCol = []
            for k in range(j, j + 5):
                tempRow.append(a[i][k])
                tempCol.append(a[k][i])
            str1 = ''.join(str(s) for s in tempRow)
            tempRow.reverse()
            str2 = ''.join(str(s) for s in tempRow)
            if str1 == str2:
                cnt += 1
            str3 = ''.join(str(s) for s in tempCol)
            tempCol.reverse()
            str4 = ''.join(str(s) for s in tempCol)
            if str3 == str4:
                cnt += 1
print(cnt)
'''

