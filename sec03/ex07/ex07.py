'''
사과나무(다이아몬드)

현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다.
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다
현수과 수확하는 사과의 총 개수를 출력하세요.
'''
import sys
sys.stdin = open("in.txt", "rt")

#강사 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n // 2

for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2: # 절반까지 내려오기 전
        s -= 1
        e += 1
    else: # 절반까지 내려온 후
        s += 1
        e -= 1

print(res)

'''
# 내 풀이
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

half = n//2
result = 0

for i in range(n):
    pointer = [[0, half]]
    if i <= half:
        for j in range(half - i, half + (i + 1)):
            result += a[i][j]
    else:
        for j in range(i - half, half + (n - i)):
            result += a[i][j]

print(result)
'''
