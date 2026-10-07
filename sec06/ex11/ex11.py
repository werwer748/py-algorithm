"""
* 수들의 조합
N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
예를 들면 5개의 숫자 2 4 5 8 12가 주어지고,
3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지가 있습니다.

#! 입력설명
첫줄에 정수의 개수 N(3<=N<=20)과 임의의 정수 K(2<=K<=N)가 주어지고,
두 번째 줄에는 N개의 정수가 주어진다.
세 번째 줄에 M이 주어집니다.

#! 출력설명
총 가지수를 출력합니다.
"""

import sys
sys.stdin = open("in5.txt")


# 내 풀이2
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

# 내 풀이2
def DFS(l, ai, s):
    global cnt

    if l == k:
        if s % m == 0:
            cnt += 1
        return

    for i in range(ai, n):
        DFS(l + 1, i + 1, s + a[i])

DFS(0, 0, 0)
print(cnt)

"""
# 강사 풀이
def DFS(l, s, sm):
    global cnt

    if l == k:
        if sm % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(l + 1, i + 1, sm + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
"""

"""
#  내 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

def DFS(l, s):
    global cnt

    if len(s) > k:
        return

    if l == n:
        if len(s) == k and sum(s) % m == 0:
            cnt += 1
            return
        return

    s.append(a[l])
    DFS(l + 1, s)
    s.pop()
    DFS(l + 1, s)


DFS(0, [])
print(cnt)
"""