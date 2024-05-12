import sys
sys.stdin = open("in5.txt", "rt")

'''
# 내 풀이
n = int(input())
ary = input().split()

max = -2147000000
result = ary[0]

def digit_sum(x):
    decompX = list(map(int, list(x)))
    return sum(decompX)

for i in range(n):
    temp = digit_sum(ary[i])
    if temp > max:
        max = temp
        result = ary[i]

print(result)
'''

# 강사 풀이
n = int(input())
a = list(map(int, input().split()))

## 방법 1
def digit_sum_number(x):
    sum = 0
    while x > 0:
        sum += x % 10 # 한자리씩 밀어내면서 자릿수 더하기
        x = x//10
    return sum
## 방법 2
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)