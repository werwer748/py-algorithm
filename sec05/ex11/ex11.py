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
from typing import List

import math

open_number = "5"
sys.stdin = open("in" + open_number + ".txt", "r")

# 콘솔 출력을 변수로 저장하기 위한 설정
from io import StringIO
output_capture = StringIO()
sys.stdout = output_capture  # 표준 출력을 StringIO로 변경

'''
# 직접 구현
class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def heap_append(self, n: int):
        self.heap.append(n)
        cur = len(self.heap) - 1
        parent = math.trunc(cur / 2)

        while cur > 1 and self.heap[cur] > self.heap[parent]:
            self.heap[cur], self.heap[parent] = self.heap[parent], self.heap[cur]
            cur = parent
            parent = math.trunc(cur / 2)

    def heap_pop(self):
        if len(self.heap) <= 1:
            return None

        max_num = self.heap[1]

        if len(self.heap) == 2:
            self.heap = [None]
            return max_num

        self.heap[1] = self.heap.pop()

        cur = 1

        while cur * 2 < len(self.heap):
            left = cur * 2
            right = left + 1
            tmp = left

            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                tmp = right

            if self.heap[cur] > self.heap[tmp]:
                break

            self.heap[cur], self.heap[tmp] = self.heap[tmp], self.heap[cur]

            cur = tmp

        return max_num


a = MaxHeap()
while True:
    n = int(input())

    if n < 0:
        break
    elif n == 0:
        pop_num = a.heap_pop()
        if pop_num:
            print(pop_num)
        else:
            print(-1)
    else:
        a.heap_append(n)
'''


# heapq 사용
a = []
while True:
    n = int(input())

    if n < 0:
        break
    elif n == 0:
        max_pop = -1 if len(a) == 0 else -(hq.heappop(a))
        print(max_pop)
    else:
        hq.heappush(a, -n)



# 표준 출력을 원래대로 복원
sys.stdout = sys.__stdout__

# 콘솔 출력 결과 가져오기
console_output = output_capture.getvalue().strip().split("\n")

# 정답 파일 불러오기
with open("out" + open_number + ".txt", "r") as f:
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
