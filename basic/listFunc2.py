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

for x in enumerate(a): # tuple 구조로 (index, 값)으로 나옴
    print(x)