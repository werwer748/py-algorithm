'''
리스트와 내장함수(2)
'''
a = [23, 12, 36, 53, 19]
print(a[:3]) # 0번째부터 2번째까지
print(a[1:4]) # 1번째부터 3번째까지
print(len(a)) # 리스트의 길이

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a: # x는 a 리스트의 인자들이 된다.
    print(x, end=' ')
print()

# 리스트 내에서 홀수값만 뽑기
for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a): # tuple 구조(index, 값)로 으로 나옴
    print(x)

b = (1, 2, 3, 4, 5) # 튜플이 만들어진다.
print(b[0])
# b[0] = 7 # 튜플은 리스트와 다르게 값을 변경할 수 없다.

for x in enumerate(a): # tuple 구조(index, 값)로 으로 나옴
    print(x[0], x[1])
print()

for index, value in enumerate(a): # 편하게 뽑아쓰기
    print(index, value)
print()

if all(60 > x for x in a): # a리스트에 for문을 도는데 조건 검사 후 모두가 참이면 true를 반환한다. 하나라도 false면 false
    print("Yes")
else:
    print("No")

if any(15 > x for x in a): # a리스트에 for문을 도는데 조건 검사 후 하나라도 참이면  true를 반환. 모두 false여야 false
    print("Yes")
else:
    print("No")