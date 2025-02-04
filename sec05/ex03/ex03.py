"""
후위표기식 만들기

중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있 으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
(3+5)*2 이면 35+2* 로 바꾸어야 합니다.

#! 입력설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다. 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다

#! 출력 설명
후위표기식을 출력한다.
"""
import sys
solution_num = "5"
input_txt = 'in' + solution_num + ".txt"
output_txt = 'out' + solution_num + ".txt"
sys.stdin = open(input_txt)

# 강사 풀이
a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()


sys.stdin = open(output_txt)
correct = input().replace(" ", "")

if res == correct:
    print("SUCCESS")
else:
    print("FAIL")
    print("res:: ", res)
    print("correct:: ", correct)






'''
# 내 풀이
s = input()
stack = []
res = ''

for x in s:
    if x.isdecimal():
        res += x
    elif x == "(":
        stack.append(x)
    elif x == "*" or x == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            res += stack.pop()
        stack.append(x)
    elif x == "+" or x == "-":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.append(x)
    else:
        while stack:
            last = stack.pop()
            if last != "(":
                res += last
            else:
                break

res += "".join(stack)

sys.stdin = open(output_txt)
correct = input().replace(" ", "")

if res == correct:
    print("SUCCESS")
else:
    print("FAIL")
    print("res:: ", res)
    print("correct:: ", correct)
'''