"""
* 순열 구하기
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.

#! 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

#! 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다.
출력순서는 사전순으로 오름차순으로 출력합니다.
"""

import sys
txt_num = "5"
sys.stdin = open("in" + txt_num + ".txt", "r")

# 콘솔 출력을 변수로 저장하기 위한 설정
# from io import StringIO
# output_capture = StringIO()
# sys.stdout = output_capture  # 표준 출력을 StringIO로 변경

# 내 풀이
n, m = map(int, input().split())
res = [0] * m
blacklist = [0] * (n + 1)
cnt = 0

def DFS(l):
    global cnt

    if l == m:
        print(" ".join(map(str, res)))
        cnt += 1
        return

    for i in range(1, n + 1):
        if blacklist[i] != 1:
            blacklist[i] = 1
            res[l] = i
            DFS(l + 1)
            blacklist[i] = 0

DFS(0)
print(cnt)

'''
# 강사 풀이
def DFS(l):
    global cnt

    if l == m:
        for j in range(l):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                DFS(l + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)
'''

"""
# 표준 출력을 원래대로 복원
sys.stdout = sys.__stdout__

# 콘솔 출력 결과 가져오기 (오른쪽 공백 제거하고 빈 줄 무시)
console_output = [line.rstrip() for line in output_capture.getvalue().splitlines() if line.rstrip() != '']

# 정답 파일 불러오기 (오른쪽 공백 제거하고 빈 줄 무시)
with open("out" + txt_num + ".txt", "r") as f:
    correct_output = [line.rstrip() for line in f.read().splitlines() if line.rstrip() != '']

# 비교 및 결과 출력
if console_output == correct_output:
    print("OK")
else:
    print("FAIL")
    print("=== 콘솔 출력 ===")
    print("\n".join(console_output))
    print("=== 정답 파일 ===")
    print("\n".join(correct_output))
"""