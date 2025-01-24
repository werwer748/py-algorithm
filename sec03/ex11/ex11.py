'''
격자판 회문수
'''
import sys
sys.stdin = open("in5.txt", "rt")

board = [list(map(str, input().split())) for _ in range(7)]
cnt = 0

# 강사 풀이
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)

'''
# 내 풀이
def check_str_list(s):
    list_str = "".join(s)
    s.reverse()
    rev_list_str = "".join(s)

    if list_str == rev_list_str:
        return True
    else:
        return False


col_list = []

for i in range(7):
    for j in range(7):
        tmp = []
        get_list = board[i][j:j + 5]

        if j < 3:
            for k in range(j, j + 5):
                tmp.append(board[k][i])
            else:
                col_list.append(tmp)

        if len(get_list) < 5:
            continue
        if check_str_list(get_list):
            cnt += 1

for x in col_list:
    if check_str_list(x):
        cnt += 1

print(cnt)
'''

