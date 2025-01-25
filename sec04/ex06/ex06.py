"""
씨름 선수(그리디)

현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습니다.
현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자 만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.

# 입력 설명
첫째 줄에 지원자의 수 N(5<=N<=50)이 주어집니다.
두 번째 줄부터 N명의 키와 몸무게 정보가 차례로 주어집니다. 각 선수의 키와 몸무게는 모두 다릅니다.

# 출력설명
첫째 줄에 씨름 선수로 뽑히는 최대 인원을 출력하세요.
"""
import sys
sys.stdin = open("in.txt")


# 강사 풀이
n = int(input())
body = [tuple(map(int, input().split())) for _ in range(n)]
body.sort(key=lambda x: (x[0], x[1]), reverse=True)

largest = 0
cnt = 0

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)

'''
# 내 풀이
n = int(input())
vt = [tuple(map(int, input().split())) for _ in range(n)]


def q_sorting(arr, pivot=0):
    if len(arr) <= 1:
        return arr

    h, w = arr[len(arr) // 2]
    r = [x for x in arr if x[pivot] < (h if pivot == 0 else w)]
    m = [x for x in arr if x[pivot] == (h if pivot == 0 else w)]
    l = [x for x in arr if x[pivot] > (h if pivot == 0 else w)]

    return q_sorting(l, pivot) + m + q_sorting(r, pivot)


sorted_vt_h = q_sorting(vt)
# print(sorted_vt_h)
accept = 0
largest = 0

# 내 풀이 3
for i in range(n):
    weight = sorted_vt_h[i][1]
    largest = max(weight, largest)

    if largest == weight:
        accept += 1
print(accept)
'''
'''
# 내 풀이 2
for i in range(n):
    weight = sorted_vt_h[i][1]
    for j in range(i, -1, -1):
        if sorted_vt_h[j][1] > weight:
            accept -= 1
            break
print(accept)
'''

'''
# 내 풀이 1
# print(sorted_vt_h)
sorted_vt_w = q_sorting(vt, 1)
accept = 0
for idx, (h, w) in enumerate(sorted_vt_h):
    find_h = h
    find_w = w
    for idx2, (h2, w2) in enumerate(sorted_vt_h):
        if idx == idx2:
            continue
        find_h = max(h, h2)
        find_w = max(w, w2)
        if find_h > h and find_w > w:
            break
    else:
        accept += 1

print(accept)
'''