"""
증가수열 만들기(그리디)

1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열 을 만듭니다.
이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4, 왼쪽끝에서5를가져와 2345증가수열을만들수있습니다.

#! 입력 설명
첫째 줄에 자연수 N(3<=N<=100)이 주어집니다. 두 번째 줄에 N개로 구성된 수열이 주어집니다.

#! 출력 설명
첫째 줄에 최대 증가수열의 길이를 출력합니다.
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)

? 헷갈렸던거 정리!
? 주어진 수열(리스트_에서) 순서 유지하면서 증가하는 형태를 가진 배열을 만들라는 거였음... 아아
"""
import sys
sys.stdin = open("in3.txt")

# # 강사풀이
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear() # 비우기

print(len(res))
print(res)

"""
# 내 풀이
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n - 1
last = 0
point = ''

while last <= a[lt] or last <= a[rt]:
    temp = []
    print(last, a[lt], a[rt])
    if last <= a[lt]:
        temp.append((a[lt], 'L'))
    if last <= a[rt]:
        temp.append((a[rt], 'R'))
    temp.sort()
    last = temp[0][0]
    point += temp[0][1]

    if temp[0][1] == 'L':
        lt += 1
    else:
        rt -= 1

print(len(point))
print(point)
"""