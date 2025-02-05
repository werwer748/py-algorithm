"""
* 최대힙

최대힙은 완전이진트리로 구현된 자료구조입니다.
그 구성은 부모 노드값이 왼쪽자식과 오른쪽 자식노드의 값보다 크게 트리를 구성하는 것입니다.
그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 큰 값이 저장되어 있습니다.
예를 들어 5 3 2 1 4 6 7순으로 입력되면 최대힙 트리는 아래와 같이 구성됩니다

최대힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.
1) 자연수가 입력되면 최대힙에 입력한다.
2) 숫자 0 이 입력되면 최대힙에서 최댓값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.

#! 입력 설명
첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.

#! 출력 설명
연산을 한 결과를 보여준다.
"""
import sys
import heapq as hq
sys.stdin = open("in5.txt", "r")

# 콘솔 출력을 변수로 저장하기 위한 설정
from io import StringIO
output_capture = StringIO()
sys.stdout = output_capture  # 표준 출력을 StringIO로 변경

a = []

while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print("-1")
        else:
            print(-(hq.heappop(a)))
    else:
        hq.heappush(a, -n)

# 표준 출력을 원래대로 복원
sys.stdout = sys.__stdout__

# 콘솔 출력 결과 가져오기
console_output = output_capture.getvalue().strip().split("\n")

# 정답 파일 불러오기
with open("out5.txt", "r") as f:
    correct_output = f.read().strip().split("\n")

# 비교 및 결과 출력
if console_output == correct_output:
    print("OK")
else:
    print("FAIL")
    print("=== 콘솔 출력 ===")
    print("\n".join(console_output))
    print("=== 정답 파일 ===")
    print("\n".join(correct_output))