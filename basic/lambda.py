'''
람다 함수(익명 함수)
'''


# 일반적인 함수 사용법
def plus_one(x):
    return x + 1

# print(plus_one(1))

# 람다로 함수 만들고 사용해 보기
plus_two = lambda x: x + 2
print(plus_two(1))

a = [1, 2, 3]
# print(list(map(plus_one, a))) # 일반함수 사용
print(list(map(lambda x: x + 1, a))) # 람다함수 사용