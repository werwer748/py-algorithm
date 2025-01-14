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
sys.stdin = open("in2.txt", "r")

#* 강사풀이
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))] # 튜플로 만듬
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    # 현재 튜플에 0은 pos, 1은 val
    if any(cur[1] < x[1] for x in Q): # any 하나라도 참이면 참
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)


"""
* 내풀이

n, m = map(int, input().split())
patient = list(map(int, input().split()))
indexed_patient = deque([{'idx': idx, 'value': val} for idx, val in enumerate(patient)])
treatment = []

while indexed_patient:
    cur = indexed_patient.popleft()
    if indexed_patient and cur['value'] < max(indexed_patient, key=lambda x: x['value'])['value']:
        indexed_patient.append(cur)
    else:
        treatment.append(cur)

for idx, obj in enumerate(treatment):
    if obj['idx'] == m:
        print(idx + 1)
        break
"""