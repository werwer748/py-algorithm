'''
함수 만들기
'''

'''
# 함수 기본 형 
def add(a, b):
    c = a + b
    print(c)

add(3,2)
add(5, 7)
'''

'''
# return 함수
def add(a, b):
    c = a + b
    return c
# print(add(3, 2)) # 함수는 내부적으로 계산만하고 print로 결과를 따로 출력

x = add(3, 2)
print(x)
'''

'''
# 함수 하나로 여러가지 값 return
def add(a, b):
    c = a + b
    d = a - b
    return c, d

print(add(3, 2))
'''

# 소수 판정하는 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False # False 반환하고 함수 종료
    return True

a = [12, 13, 7, 9, 19]
for v in a:
    if isPrime(v):
        print(v, end=' ')
print()