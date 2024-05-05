'''
K번째 약수 구하기
'''
import sys

sys.stdin = open("in2.txt", "rt")
n, k = map(int, input().split())

'''
# 내풀이
ary = []
for i in range(1, n + 1):
    if n % i == 0:
        ary.append(i)

result = -1
if (len(ary) > k - 1):
    result = ary[k - 1]

print(result)
'''
# 강사풀이
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else: # for 정상실행후에 답이 없을경우 -1
    print(-1)


# def checkResult(x):
#     #=== 실제 문제 푸는 영역 start ===#
#     sys.stdin = open(f"in{x}.txt", "rt")
#     n, k = map(int, input().split(" "))
#
#
#     ary = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             ary.append(i)
#
#     result = -1
#     if (len(ary) > k - 1):
#         result = ary[k - 1]
#
#     sys.stdin = open(f"out{x}.txt", "rt")
#     out = int(input())
#     #=== 실제 문제 푸는 영역 end ===#
#
#     if result == out:
#         return True
#
#     return False
#
# if all(checkResult(x) for x in range(1, 6)):
#     print("Pass All")
# else:
#     print(f"Wrong Answer")