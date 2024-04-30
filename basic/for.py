'''
반복문 (for, while)
'''
'''
a = range(10) # 0 ~ 9 까지 정수리스트 만들기
print(a) # range(0,10)
print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(1, 11) # 1 ~ 10 까지 정수리스트 만들기
print(a) # range(1,11)
print(list(a)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

'''
# for
for i in range(1, 10):
    # print("hello")
    print(i)

for i in range(10, 0, -1): # 역순으로 갈경우 인자를 하나 더 해준다.(마지막인자)
    print(i)
'''

'''
# while
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 10
while i >= 1:
    print(i)
    i = i - 1
'''

'''
# break
i = 1
while True: # while true 무한반복
    print(i)
    if i == 10:
        break # 반복문 종료시킴
    i += 1
'''

'''
# continue
for i in range(1, 11):
    if i % 2 == 0:
        continue # continue 아래로 스킵하고 다음 반복
    print(i)
'''

# for else
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else: # for문이 정상적으로 모든 범위를 돌았을 때 작동됨. break로 range 범위를 못채우면 작동하지 않는다.
    print(11)

