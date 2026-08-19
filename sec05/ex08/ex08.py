"""
* 단어찾기

현수는 영어로 시는 쓰는 것을 좋아합니다. 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 여러분이 찾아 주세요.
"""

import sys
sys.stdin = open("in5.txt", "r")

# 내 풀이2
n = int(input())
words = {input(): 0 for _ in range(n)}

for _ in range(n - 1):
    words[input()] = 1

while words:
    w = words.popitem()
    if w[1] == 0:
        print(w[0])
        break




'''
# 강사 풀이
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
'''

'''
# 내 풀이
n = int(input())
words = {input(): 1 for _ in range(n)}

for i in range(n - 1):
    words[input()] -= 1

for k in words.keys():
    if words[k] == 1:
        print(k)
        break
'''