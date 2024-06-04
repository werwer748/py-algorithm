'''
스도쿠 검사
'''
import sys

sys.stdin = open("in5.txt", "rt")


## 강사 코드 설명
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
a = [list(map(int, input().split())) for _ in range(9)]
res = 'YES'

for i in range(9):
    rc = [0] * 10
    cc = [0] * 10
    for j in range(9):
        rc[a[i][j]] = 1
        cc[a[j][i]] = 1
    if sum(rc) != 9 or sum(cc) != 9:
        res = 'NO'

for i in range(3):
    for j in range(3):
        sc = [0] * 10
        for k in range(3):
            for s in range(3):
                sc[a[i * 3 + k][j * 3 + s]] = 1
        if sum(sc) != 9:
            res = 'NO'

print(res)
'''
