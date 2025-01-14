'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.
'''

import sys
sys.stdin = open("in5.txt", "rt")

'''
# 내 풀이
n = int(input())
ary = input().split()

def digit_sum(str_num):
    tmp = 0
    for x in str_num:
        tmp += int(x)
    return tmp

res = 0
max_str = ''

for x in ary:
    sum_res = digit_sum(x)
    if res < sum_res:
        res = sum_res
        max_str = x

print(max_str)
'''

# 강사풀이
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0

    # 방법1
    # while x > 0:
    #     sum += x % 10
    #     x = x//10

    # 방법2 - str(x) => 123 = '123'
    for i in str(x):
        sum += int(i)

    return sum

# max = -2147000000
max = float("-inf")

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)