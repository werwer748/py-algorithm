"""
응급실

메디컬 병원 응급실에는 의사가 한 명밖에 없습니다. 응급실은 환자가 도착한 순서대로 진료를 합니다.
하지만 위험도가 높은 환자는 빨리 응급조치를 의사가 해야 합니다. 이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정합니다.
• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로
    다시 넣습니다. 그렇지 않으면 진료를 받습니다.

현재 N명의 환자가 대기목록에 있습니다.
N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료를 받는지 출력하는 프로그램을 작성하세요.
대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.

#! 입력 설명
첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.

#! 출력 설명
M번째 환자가 몇 번째로 진료받는지 출력하세요.
"""
import sys
from collections import deque
import heapq
sys.stdin = open("in1.txt", "r")

# 아이디어 검증
n, m = map(int, input().split())
patients = list(map(int, input().split()))

# 대기 순서 유지
q = deque((idx, risk) for idx, risk in enumerate(patients))

# 남아 있는 환자들의 위험도를 관리
# heap의 값은 음수로 넣어 max-heap처럼 사용
heap = [(-risk, idx) for idx, risk in enumerate(patients)]
heapq.heapify(heap)
print(heap)
treated = [False] * n
print(treated)
cnt = 0

while q:
    idx, risk = q.popleft()

    # heap에서 이미 진료된 환자 제거
    while heap and treated[heap[0][1]]:
        heapq.heappop(heap)

    # 가장 위험한 환자가 현재 환자가 아니면 뒤로 보냄
    if heap and -heap[0][0] > risk:
        q.append((idx, risk))
        continue

    cnt += 1
    treated[idx] = True

    if idx == m:
        print(cnt)
        break

'''
# 내 풀이 3
n, m = map(int, input().split())
patients = deque(
    (pos == m, val) for pos, val in enumerate(
        list(map(int, input().split()))
    )
)
cnt = 0

while True:
    cur = patients.popleft()
    danger_check = True

    for pos, val in patients:
        if cur[1] < val:
            patients.append(cur)
            danger_check = False
            break

    if danger_check:
        cnt += 1
        if cur[0]:
            print(cnt)
            break
'''
'''
# 내 풀이2
n, m = map(int, input().split())
patients = list(map(int, input().split()))
patients = deque((i, x) for i, x in enumerate(patients))
very_danger = max(patients, key=lambda x: x[1])
waiting = []

while patients:
    cur = patients.popleft()
    if very_danger[1] > cur[1]:
        patients.append(cur)
    else:
        waiting.append(cur)
    if patients:
        very_danger = max(patients, key=lambda x: x[1])


print(waiting)
for i, x in enumerate(waiting):
    if x[0] == m:
        print(i + 1)
        break
'''


'''
# 강사 풀이
n, m = map(int, input().split())
#* 리스트 컴프리헨션
# Q = [(pos == m, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()

    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)
'''


'''
# 내 풀이
n, m = map(int, input().split())
danger = list(map(int, input().split()))
danger = deque(list(map(lambda item: (int(item[1]), item[0] == m), enumerate(danger))))
cnt = 0

while True:
    p = danger.popleft()
    ok = False
    for x, y in danger:
        if p[0] < x:
            danger.append(p)
            break
    else:
        ok = True

    if ok:
        cnt += 1
        if p[1]:
            print(cnt)
            break
'''