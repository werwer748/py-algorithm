'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper()) # 모든 문자열이 대문자 (원본 유지)
print(msg.lower()) # 모든 문자열 소문자화 (원본 유지)

tmp = msg.upper()
print(tmp) # 대문자로 바꾼 문자열을 변수에 대입
print(tmp.find('T')) # 처음 찾은 T의 index 번호
print(tmp.count('T')) ## 문자열 내에 T의 갯수

print(msg)
print(msg[:2]) # msg의 0번째부터 1번까지 문자
print(msg[3:5]) # 3번째부터 4번째까지
print(len(msg)) # 공백 포함한 문자열 길이(공백도 문자니까)

# 문자열로 for문
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg: # x는 msg 문자열의 요소들
    print(x, end=' ')
print()

for x in msg:
    if (x.isupper()): # 대문자만
        print(x, end='')
print()

for x in msg:
    if (x.islower()): # 소문자만
        print(x, end=' ')
print()

for x in msg:
    if (x.isalpha()): # 알파벳 체크
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x)) # 아스키 넘버 출력

tmp = 'az'
for x in tmp:
    print(ord(x)) # 아스키 넘버 출력

tmp = 65
print(chr(tmp)) # 아스키넘버 => 문자

