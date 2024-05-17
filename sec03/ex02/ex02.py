'''
숫자만 추출

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉첫자리0은자연수화할때무시합니다.
출력은120를출력하고,다음줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
'''

import sys
sys.stdin = open("in1.txt", "rt")
# print(ord('0'), ord('9')) # 48 ~ 57

# 강사 풀이
s = input()
res = 0
for x in s: # isdigit: 모든 숫자로 보이는 형태를 찾아줌, isdecimal: 0~9까지 숫자인지 체크
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(cnt)

'''
# 내 풀이
text = input()
numText = ''

for c in text:
    if ord(c) >= 48 and ord(c) <= 57:
        numText += c

num = int(numText)
cnt = 0

for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)
'''


