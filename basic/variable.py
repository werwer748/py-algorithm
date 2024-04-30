"""
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _ 로 시작한다.
4) 특수문자를 사용하면 안된다.(&, % emd)
5) 키워드를 사용하면 안된다. (if, for 등)
"""

a = 1
A = 2
A1 = 3
# 2b = 4 # 에러;;
_b = 4
print(a, A, A1, _b)

# 여러개 한번에 선언
a, b, c = 3, 2, 1
print(a, b, c)

#값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345
print(type(a)) #int 정수 타입

a = 12.123456789123456789
print(type(a)) # float 소수 타입

a = 'student'
print(a)
print(type(a)) # str

## 출력방법
print("number")
a, b, c = 1, 2, 3
print(a, b, c) #, 기준으로 띄어쓰기
print("number : ", a, b, c)
print(a, b, c, sep=' | ') # sep으로 , 사이를 어떻게 처리할지 정할 수 있다.
print(a, b, c, sep='\n') # 줄바꿈
print(a) # 기본적으로 print하고나면 줄바꿈
print(b)
print(c)
print(a, end=' ') # 프린트 찍히고 후처리를 결정 기본적으로 \n
print(b)
