"""
#? stack: stack자료 구조는 앞선 인덱스와 비교해서 자연스럽게 처리가능한 자료구조??
#?          last in first out L I F O, 먼저 들어간 값이 가장 나중에 나온다~

가장 큰 수

선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하 여 가장 큰 수를 만들라고 했습니다.
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.

#! 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

#! 출력설명
가장 큰 수를 출력합니다.
"""
import sys
sys.stdin = open("in4.txt")

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:m]
res = ''.join(map(str, stack))
print(res)


'''
# 내 풀이
num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
cnt = 0
for i in range(len(num)):
    if len(stack) == (len(num) - m):
        break
    copy_stack = stack[:]
    for y in copy_stack:
        if num[i] > y:
            stack.pop()
            cnt += 1
        if cnt == m:
            break
    if cnt == m:
        stack += num[i:]
        break
    stack.append(num[i])

res = "".join(map(str, stack))
# print(res)

sys.stdin = open("out4.txt")
correct = input()

if res == correct:
    print("SUCCESS")
else:
    print("FAIL")
    print("res:: ", res)
    print("correct:: ", correct)
'''




