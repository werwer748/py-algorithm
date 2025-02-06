"""
* 부분집합 구하기
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하세요.

#! 입력 설명
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

#! 출력 설명
첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다.
단 공집합은 출력하지 않습니다.
"""
import sys
sys.stdin = open("in5.txt", "r")

# 콘솔 출력을 변수로 저장하기 위한 설정
from io import StringIO
output_capture = StringIO()
sys.stdout = output_capture  # 표준 출력을 StringIO로 변경

'''
## 강사 풀이
def DFS(v):
    if v == n + 1:
        for i, x in enumerate(ch):
            if x == 1:
                # 정답지처럼 출력하기용
                # print(i, end=' ')
                # 같은값 출력 확인용
                print(i, end='')
        print(end="\n")
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)

# if __name__ == "__main__":
n = int(input())
ch = [0] * (n + 1)
DFS(1)
'''
n = int(input())
a = []

# 내 풀이 - 중위 순회로 하니까 풀림
def DFS(v, ary):
    if v > n:
        return
    else:
        ary.append(v)
        DFS(v + 1, ary)
        for x in ary:
            # print(x, end=' ')
            print(x, end='')
        print(end='\n')
        ary.pop()
        DFS(v + 1, ary)


DFS(1, a)


# 표준 출력을 원래대로 복원
sys.stdout = sys.__stdout__

# 콘솔 출력 결과 가져오기
console_output = output_capture.getvalue().strip().split("\n")

# 정답 파일 불러오기
with open("out5.txt", "r") as f:
    correct_output = f.read().strip().replace(" ", "").split("\n")

# 비교 및 결과 출력
if console_output == correct_output:
    print("OK")
else:
    print("FAIL")
    print("=== 콘솔 출력 ===")
    print("\n".join(console_output))
    print("=== 정답 파일 ===")
    print("\n".join(correct_output))