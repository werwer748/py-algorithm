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
sys.stdin = open("in5.txt")

# 강사 풀이
n = int(input()) # 지원자 수
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)

largest = 0
cnt = 0

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)

"""
# 내 풀이2
n = int(input()) # 지원자 수
specs = []
for i in range(n):
    h, w = map(int, input().split())
    specs.append((h, w))
specs.sort(reverse=True)

res = 1
large_w = specs[0][1]

for i, x in enumerate(specs):
    if i == 0:
        continue
    h, w = x
    if large_w < w:
        res += 1
        large_w = w

print(res)
"""

"""
# 내 풀이
n = int(input()) # 지원자 수
specs = []

for i in range(n):
    h, w = map(int, input().split())
    specs.append((h, w))
specs.sort(reverse=True)


result = 0

for _ in range(n):
    cnt = 1
    spec = specs.pop(0)
    for h, w in specs:
        vol_h, vol_w = spec
        if vol_h > h or vol_w > w:
            cnt += 1
    if cnt == n:
        result += 1
    specs.append(spec)

print(result)
"""