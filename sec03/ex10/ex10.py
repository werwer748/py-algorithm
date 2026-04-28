'''
스도쿠 검사
'''
import sys
sys.stdin = open("in5.txt", "rt")

'''
# 내 풀이 2
a = [list(map(int, input().split())) for _ in range(9)]
res = "YES"
circle = [-1, 0, 1]
n = 9

for i in range(n):
    tmp1 = [0] * n
    tmp2 = [0] * n
    for j in range(n):
        row = a[i][j] - 1
        if tmp1[row] == 0:
            tmp1[row] = 1
        else:
            res = "NO"
        col = a[j][i] - 1
        if tmp2[col] == 0:
            tmp2[col] = 1
        else:
            res = "NO"
        if i % 3 == 1 and j % 3 == 1:
            tmp3 = [0] * n
            for k in circle:
                for l in circle:
                    cir = a[i + k][j + l] - 1
                    if tmp3[cir] == 0:
                        tmp3[cir] = 1
                    else:
                        res = "NO"
                        break
        if res == "NO":
            break
    if res == "NO":
        break
print(res)
'''

'''
# 강사 풀이
def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")
'''

'''
# 내 풀이
a = [list(map(int, input().split())) for _ in range(9)]

res = "YES"

# [-1, -1][-1, 0][-1, 1]
# [0, -1][0, 0][0, 1]
# [1, -1][1, 0][1, 1]

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

for i in range(9):
    rc = set(a[i])
    cc = set()
    for j in range(9):
        cc.add(a[j][i])
        bc = set()
        if i % 3 == 1 and j % 3 == 1:
            for k in range(len(dx)):
                bc.add(a[j + dx[k]][i + dy[k]])
            else:
                if len(bc) != 9:
                    res = "NO"

    if len(rc) != 9 and len(cc) != 9:
        res = "NO"
print(res)
'''
