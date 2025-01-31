"""
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
예를 들어 다음과 같은 수열의 경우
4 8 6 2 5 1 3 7

1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개......
따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0 이 된다.

n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출력하는 프로그램을 작성하세요.

#! 입력 설명
첫 번째 줄에 자연수 N(3<=N<100)이 주어지고, 두 번째 줄에는 역수열이 숫자 사이에 한칸의 공백을 두고 주어진다.

#!출력설명
원래 수열을 출력한다.
"""
import sys
sys.stdin = open("in3.txt")

# 강사 풀이
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1

res = "".join(list(map(str, seq)))

sys.stdin = open("out3.txt")
correct = "".join((input().split()))
if res == correct:
    print("OK")
else:
    print("FAIL")
    print(res)
    print(correct)



'''
# 내 풀이
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n

for i in range(n):
    tmp = a[i] + 1
    p = 0
    for j in range(n):
        if seq[j] == 0:
            tmp -= 1
        if tmp == 0:
            p = j
            break

    if seq[p] != 0:
        for k in range(p + 1, n + 1):
            if seq[k] != 0:
                p = k

    seq[p] = i + 1

res = "".join(list(map(str, seq)))

sys.stdin = open("out5.txt")
correct = "".join((input().split()))
if res == correct:
    print("OK")
else:
    print("FAIL")
    print(res)
    print(correct)
'''