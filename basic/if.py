'''
조건문 if (분기, 중첩)
'''

'''
x = 7
if x == 7:
    print('Lucky')
    print("ㅋㅋㅋㅋ") # 들여쓰기 잘못되면 에러
'''
'''
# 다중 if
x = 12
if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")

x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")
'''

'''
# 조건문 and
x = 7
if x > 0 and x < 10: 
    print("10보다 작은 자연수")

x = 7
if 0 < x < 10: #! 파이썬은 이렇게도 쓸 수 있다.
    print("10보다 작은 자연수")
'''

'''
#if else 분기문
x = -1
if x > 0:
    print("양수")
else:
    print("음수")
'''

# 다중 if - 하나의 문장구조 처음 걸리는 조건에서 값이 바로 리턴
x = 50
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")

y = 93 # 이렇게되면 모두 따로 작동되서 다찍힘
if y >= 90:
    print("A")
if y >= 80:
    print("B")
if y >= 70:
    print("C")