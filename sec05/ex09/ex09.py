"""
*아나그램(딕셔너리 해쉬)

Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면
A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재
배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세
요. 아나그램 판별시 대소문자가 구분됩니다.

#! 입력 설명
첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
단어의 길이는 100을 넘지 않습니다.

#! 출력 설명
두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
"""

import sys
sys.stdin = open("in5.txt", "r")

# C++ 처럼 리스트로만 풀어보기
a = input()
b = input()

str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

'''
# 강사 풀이 2
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
'''

'''
# 강사 풀이 1
a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''

'''
# 내 풀이2
s1 = list(input())
s2 = list(input())
p = dict()
res = "YES"

for x in s1:
    p[x] = p.get(x, 0) + 1

for x in s2:
    check = p.get(x)

    if check is None:
        res = "NO"
        break
    else:
        p[x] -= 1

for k in p.keys():
    if p[k] != 0:
        res = "NO"
        break

print(res)
'''
'''
# 내 풀이
s1 = list(input())
s2 = list(input())
res = "YES"

p = {x: 0 for x in s1}
for x in s1:
    p[x] += 1

while s2:
    s = s2.pop()

    if p.get(s, False):
        p[s] -= 1
    else:
        res = "NO"
        break

for key, val in p.items():
    if val != 0:
        res = "NO"
        break

print(res)
'''