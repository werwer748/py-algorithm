"""
쇠막대기

여러 개의 쇠막대기를 레이저로 절단하려고 한다.
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
쇠막대기와 레이저의 배치는 다음 조건을 만족한다.


• 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
• 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
• 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

#! 입력 설명
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

#! 출력 설명
잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
"""
import sys
sys.stdin = open("in5.txt", "r")

s = input()
stack = []
cnt = 0

# 재풀이 2
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)






"""
s = input()
stack = []
cnt = 0

# 재풀이
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
"""



"""
s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(': # 막대기 추가
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(': # 레이저
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
"""