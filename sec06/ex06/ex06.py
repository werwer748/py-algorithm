"""
* 중복순열 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

#! 입력 설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

#! 출력 설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.
"""
import sys
sys.stdin = open("in5.txt", "r")

from io import StringIO
output_capture = StringIO()
sys.stdout = output_capture

'''
# 강사 풀이
def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ' if j != m-1 else '')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
'''


# 내 풀이
n, m = map(int, input().split())
a = list(range(1, n + 1))
cnt = 0

def DFS(v):
    global cnt
    if len(v) == m:
        print(" ".join(map(str, v)))
        cnt += 1
        return
    else:
        for i in range(n):
            tmp = [a[i]]
            DFS(v + tmp)


DFS([])
print(cnt)

sys.stdout = sys.__stdout__
console_output = output_capture.getvalue().strip().split("\n")

with open("out5.txt") as f:
    correct_output = f.read().strip().split("\n")

if console_output == correct_output:
    print("OK")
else:
    print("FAIL")
    print("=== 콘솔 출력 ===")
    print("\n".join(console_output))
    print("=== 정답 파일 ===")
    print("\n".join(correct_output))