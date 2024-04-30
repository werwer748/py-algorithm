'''
리스트와 내장함수(1)
'''
import random as r

# 빈 리스트 만드는 두가지 방법
a=[]
# print(a)
b = list()
# print(b)

# 초기화한 리스트 만들기
a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0]) # a의 0번째 index 값

# range를 활용하여 초기화한 리스트 만들기
b = list(range(1, 11))
# print(b)

# list 합치기... ㄷㄷㄷㄷㄷ
c = a + b
# print(c)

# 리스트에 값 추가
# print(a)
a.append(6) # 리스트 제일 마지막에 값 추가
# print(a)

a.insert(3, 7) # 3번째 index에 7을 추가 (3번째 뒤값들은 한칸씩 밀린다.)
# print(a)

a.pop() # 마지막 인자 제거
# print(a)
a.pop(3) # 3번째 인덱스 값 제거
# print(a)

a.remove(4) # 4라는 값을 제거
# print(a)

print(a.index(5)) # 5라는 값의 index 값

a = list(range(1, 11))
print(a)
print(sum(a)) # 리스트 내의 모든 값을 더 함.
print(max(a)) # 리스트 내에서 가장 큰 값
print(min(a)) # 리스트 내에서 가장 작은 값
print(min('나', '가','다')) # 결과값: 가

r.shuffle(a) # 무작위 셔플
print(a)

a.sort(reverse=True) # 내림차순 정렬
print(a)
a.sort() # 오름차순 정렬
print(a)
a.clear() # 리스트 비우기
print(a)