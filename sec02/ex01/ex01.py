'''
K번째 약수 구하기
'''
import sys
sys.stdin = open("in5.txt", "rt")
n, k = map(int, input().split())


# 내풀이
result = 0
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        result = i
        break
else:
    result = -1

print(result)