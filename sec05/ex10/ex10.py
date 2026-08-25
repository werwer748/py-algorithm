"""
* 최소힙

최소힙은 완전이진트리로 구현된 자료구조입니다.
그 구성은 부모 노드값이 왼쪽자식과 오른쪽 자식노드의 값보다 작게 트리를 구성하는 것입니다.
그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 작은 값이 저장되어 있습니다.
예를 들어 5 3 2 1 4 6 7순으로 입력되면 최소힙 트리는 아래와 같이 구성됩니다.

최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.
1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.

#! 입력 설명
첫 번째 줄부터 숫자가 입력된다.
입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.

#! 출력 설명
연산을 한 결과를 보여준다.
"""

import sys
import heapq as hq
import math

sys.stdin = open("in3.txt")

"""
핵심은 

힙(Heap) 내부에서 위치를 이동하고(Loop), 대상을 지정하고(Assign), 반복 조건을 따질 때는 철저하게 '인덱스(주소/방 번호)'만 가지고 계산한다. 
그러다가 실제로 크기를 비교해야 하는 '비교와 정렬의 순간'에만 그 인덱스를 사용해 실제 배열 안의 '노드 값(Value)'을 꺼내서 비교하는 것이다.
"""

'''
# 직접 구현
class MinHeap:
    def __init__(self):
        self.heap = [None]

    def heap_push(self, val):
        self.heap.append(val)
        cur = len(self.heap) - 1
        parent = math.trunc(cur / 2)

        while cur > 1 and (self.heap[parent] > self.heap[cur]):
            self.heap[parent], self.heap[cur] = self.heap[cur], self.heap[parent]
            cur = parent
            parent = math.trunc(cur / 2)

    def heap_pop(self):
        if len(self.heap) <= 1:
            return None

        hmin = self.heap[1]

        if len(self.heap) == 2:
            self.heap = [None]
            return hmin

        self.heap[1] = self.heap.pop()

        cur = 1

        while cur * 2 < len(self.heap):
            left = cur * 2
            right = left + 1
            imin = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                imin = right

            if self.heap[cur] <= self.heap[imin]:
                break

            self.heap[cur], self.heap[imin] = self.heap[imin], self.heap[cur]

            cur = imin

        return hmin

arr = MinHeap()
while True:
    input_num = int(input())

    if input_num == 0:
        pop_num = arr.heap_pop()
        print(pop_num)

    if input_num < 0:
        break
    if input_num > 0:
        arr.heap_push(input_num)
'''

# heapq 사용
a = []

while True:
    inp = int(input())

    if inp == 0:
        pop_num = hq.heappop(a)
        print(pop_num)

    if inp < 0:
        break
    if inp > 0:
        hq.heappush(a, inp)