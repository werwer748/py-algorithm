"""
*재귀함수를 이용한 이진수 출력

10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
단 재귀함수를 이용해서 출력해야 합니다.

#? 재귀함수
? - 자기가 자기자신을 반복해서 호출하는 것.
? - 반복문의 대체제
? - 다중 for문의 경우 코드의 유연성이 떨어지는데 재귀함수를 통해 해결할 수 있다.
? - 재귀함수는 스택을 활용하여 실행 된다.
? - 즉, 가장 늦게 호출된 함수가 가장 먼저 실행되는 것.
"""

import sys
sys.stdin = open("in1.txt")


# 수업
def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x, end=' ')


if __name__ == "__main__":
    n = int(input())
    # 깊이우선탐색의 줄임말 - DFS
    DFS(n)

"""
# 내가 그냥 해본거
n = int(input())

def fac(x):
    if x == 0:
        return ""
    return fac(x // 2) + str(x % 2)

print(fac(n))
"""
