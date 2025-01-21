'''
사과나무(다이아몬드)

현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다.
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다
현수과 수확하는 사과의 총 개수를 출력하세요.
'''
import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 강사 풀이
res = 0
s = e = n // 2

for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)

'''
# 내 풀이
cnt = 0
center = n // 2
start = end = center

for i in range(n):
    for j in range(start, end + 1):
        cnt += a[i][j]
    if i < center:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(cnt)
'''