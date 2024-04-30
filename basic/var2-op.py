"""
변수입력과 연산자
"""

# a = input("숫자를 입력하세요 : ") # 입력 받기
# print(a)

'''
a, b = input("숫자를 입력하세요 : ").split() # 띄어쓰기를 구분점 삼아서 입력값을 따로 대입함.
print(type(a))
# print(a + b) # 입력받으면 문자형으로 받아짐(문자열 더하기가 된다.)
c = a + b # 마찬가지로 문자열이 더해진 값이 됨.
print(type(c))
print(c)
'''

'''
# 정수형으로 바꿔서 계산
a, b = input("숫자를 입력하세요 : ").split()
a = int(a) # str => int
print(type(a))
b = int(b)
print(a + b) # 숫자로 더 해짐
'''

'''
# 입력값 타입 받을때부터 바꾸기
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 몫
print(a % b) # 나머지
print(a**b) # 거듭제곱
'''

a = 4.3
b = 5
c = a + b
print(type(c)) # 실수 + 정수 = 실수 (타입은 더 넓은 범위를 가진 타입이 된다)
print(c)