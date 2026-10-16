"""
* 인접행렬(가중치 방향그래프)
그래프 정보를 인접 행렬로 표현해보세요.

!# 입력설명
첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보와 거리비용이 주어진다.

!# 출력설명
인접행렬을 출력하세요.
"""

import sys

#1 무방향 그래프
sys.stdin = open("practice1.txt")

n1, m1 = map(int, input().split())
g1 = [[0] * (n1 + 1) for _ in range(n1 + 1)]

for i in range(m1):
    a, b = map(int, input().split())
    g1[a][b] = 1
    g1[b][a] = 1

for i in range(1, n1 + 1):
    for j in range(1, n1 + 1):
        print(g1[i][j], end=' ')
    print()

print("=============================")

#2 가중치 방향 그래프
sys.stdin = open("in.txt")

n2, m2 = map(int, input().split())
g2 = [[0] * (n2 + 1) for _ in range(n2 + 1)]

for i in range(m2):
    a, b, c = map(int, input().split())
    g2[a][b] = c

for i in range(1, n2 + 1):
    for j in range(1, n2 + 1):
        print(g2[i][j], end=' ')
    print()