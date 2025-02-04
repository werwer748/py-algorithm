'''
카드 역배치(정올 기출)

1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓 여있다.
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.

이제 여러분은 다음과 같은 규칙으로 카드의 위치를 바꾼다:
구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면,
위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다. 이제 전체 카드가 놓인 순서는 아래 그림과 같다.

이 상태에서 구간 [9, 13]이 다시 주어진다면, 위치 9부터 위치 13까지의 카드 6, 5, 11, 12, 13을 역순으로 하여 13, 12, 11, 5, 6으로 놓는다.
이제 전체 카드가 놓인 순서는 아래 그림 과 같다.

오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치 를 구하는 프로그램을 작성하시오.
'''
import sys
sys.stdin = open("in1.txt", "rt")

'''
# 내 풀이
ary = list(range(0, 21))

for i in range(10):
    ai, bi = map(int, input().split())
    rev = ary[ai:bi + 1]
    rev.reverse()
    ary[ai:bi + 1] = rev

print(" ".join(map(str, ary[1:])))
'''

a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]

a.pop(0)
for x in a:
    print(x, end=' ')