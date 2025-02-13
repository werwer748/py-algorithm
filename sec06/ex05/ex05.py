"""
* 바둑이 승차(DFS) - Cut Edge Tech

철수는 그의 바둑이들을 데리고 시장에 가려고 한다.
그런데 그의 트럭은 C킬로그램 넘게 태울 수 가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운
무게를 구하는 프로그램을 작성하세요.

#! 입력 설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다.
둘째 줄부터 N마리 바둑이의 무게가 주어진다.

#! 출력 설명
첫 번째 줄에 가장 무거운 무게를 출력한다.
"""

import sys
sys.stdin = open("in5.txt")

'''
# 강사 풀이
c, n = map(int, input().split())
a = [0] * n
total = 0
result = -2147000000
for i in range(n):
    w = int(input())
    a[i] = w
    total += w

def DFS(L, sum, t_sum):
    global result

    if sum + (total - t_sum) < result:
        return

    if sum > c:
        return

    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L + 1, sum + a[L], t_sum + a[L])
        DFS(L + 1, sum, t_sum + a[L])


DFS(0, 0, 0)
print(result)
'''


# 내 풀이
c, n = map(int, input().split())
res = 0
weights = [int(input()) for _ in range(n)]
total = sum(weights)
print(total)

def DFS(d, w_sum, tt):
    global res

    if w_sum + (total - tt) < res:
        return

    if w_sum > c:
        return

    if d == n:
        if res < w_sum:
            res = w_sum
        return
    else:
        next_w = w_sum + weights[d]

        DFS(d + 1, w_sum, next_w)
        DFS(d + 1, next_w, next_w)


DFS(0, 0, 0)
print(res)
