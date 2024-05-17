'''
회문 문자열 검사

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''
import sys
sys.stdin = open("in1.txt", "rt")

n = int(input())

'''
# 강사 풀이 - 이렇게 직접 구현하는 것이 중요하다
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    # print(s[-1])# 파이썬은 array[-1] 이런식으로 배열의 뒤부터 접근할 수 있다.
    for j in range(size//2):
        if s[j] != s[-1 - j]:
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))
'''

# 강사 풀이2 - 더 파이썬스럽게(짧게)
for i in range(n):
    s = input()
    s = s.upper()
    # print(s[::-1]) # s[::-1] 문자열을 뒤집어줌...
    if s == s[::-1]:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" %(i + 1))

'''
# 내 풀이
for i in range(n):
    str = input().lower()
    strToList = list(str)
    strToList.reverse()
    joinStrList = ''.join(strToList)

    if str == joinStrList:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))
'''
