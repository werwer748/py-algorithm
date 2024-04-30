'''
중첩 반복문(2중 for문)
'''

'''
# 구조 확인
for i in range(5):
    print('i: ', i, sep='', end=' ')
    for j in range(5):
        print('j: ', j, sep='', end=' ')
    print()
'''

'''
# 별찍기
for i in range(5):
    for j in range(i + 1):
        print("*", end=' ')
    print()
'''

'''
# 별찍기 역순 - 내풀이
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()
'''
# 별찍기 역순 - 강사 풀이
for i in range(5):
    for j in range(5 - i):
        print("*", end=' ')
    print()