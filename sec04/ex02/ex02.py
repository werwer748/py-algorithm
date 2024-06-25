"""
랜선 자르기(결정알고리즘)
결정 알고리즘의 경우 정해진 범위안에 무조건 답이 있음

엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이 다.
선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

입력 설명
첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다.
그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 2**31 - 1이하의 자연수로 주어진다.

출력 설명
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
"""
import sys
sys.stdin = open("in5.txt", "rt")

# 재풀이
k, n = map(int, input().split())
Line = []
res = 0
for _ in range(k):
    Line.append(int(input()))


lt = 0
rt = max(Line)
def lineChecker(m):
    cnt = 0
    for x in Line:
        cnt += x // m
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    check = lineChecker(mid)
    if check >= n:
        if res < mid:
            res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

"""
# 강사 풀이
k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

def Count(len):
    cnt = 0
    for x in Line:
        cnt += x // len
    return cnt


lt = 1
rt = largest


while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
"""

"""
# 내 풀이
k, n = map(int, input().split())
a = list(map(int, list(input() for _ in range(k))))
findMax = max(a)
findMin = 1
result = 0
def lineChecker(m):
    temp = 0
    for x in a:
        temp += x // m
    if temp >= n:
        return True
    else:
        return False


while findMin < findMax:
    mid = (findMin + findMax) // 2
    check = lineChecker(mid)

    if check:
        findMin = mid + 1
        if result < mid: # 어차피 최소범위가 느니까... 굳이 if문 처리가 필요가 없음...
            result = mid
    else:
        findMax = mid - 1

print(result)
"""

