"""
회의실 배정(그리디)
? 그리디 알고리즘:
? 문제를 풀어나가는 단계에서 가장 좋은 수를 선택해 나간다.
? 좋은 것을 판별하는 방법은 정렬을 통해 차례차례 선택해 나가면 된다.

한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다.
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
단, 회의는 한번 시작하면 중간에 중 단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

# 입력설명
첫째 줄에 회의의 수 n(1<=n<=100,000)이 주어진다.
둘째 줄부터 n+1 줄까지 각 회의의 정 보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.

# 출력설명
첫째 줄에 최대 사용할 수 있는 회의 수를 출력하여라.
"""
import sys
sys.stdin = open("in1.txt", "rt")

n = int(input()) # 회의의 갯수
meeting = [] # 빈리스트

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# meeting.sort() # 그냥 정렬시 튜플의 0번째 기준으로 정렬
#? 내장 함수 정렬!
# meeting.sort(key=lambda x: (x[1], x[0])) # 미팅시간을 종료시간 기준으로 정렬 - 1순위가 미팅 종료시간 2순위가 미팅 시작 시간
#? 퀵 정렬 활용해보기
def quick_sort(m):
    if len(m) < 1:
        return m

    _, pivot = m[len(m) // 2]
    left = [x for x in m if x[1] < pivot]
    middle = [x for x in m if x[1] == pivot]
    right = [x for x in m if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# def quick_sort(m):
#     if len(m) < 1:
#         return m
#
#     pivot = m[len(m) // 2]
#     left = [x for x in m if x < pivot]
#     middle = [x for x in m if x == pivot]
#     right = [x for x in m if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# end_time_list = [x for _, x in meeting]
sorted_meeting = quick_sort(meeting)
# print(sorted_meeting)

endTime = 0
cnt = 0

# for s, e in meeting:
for s, e in sorted_meeting:
    if s >= endTime:
        endTime = e
        cnt += 1

print(cnt)