"""
랜선 자르기(결정알고리즘)
결정 알고리즘의 경우 정해진 범위안에 무조건 답이 있음
"""
import sys
sys.stdin = open("in5.txt", "rt")


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

