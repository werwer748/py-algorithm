import sys
sys.stdin = open("in5.txt", "rt")

# 내 풀이
t = int(input())

for i in range(0, t):
    n, s, e, k = map(int, input().split())
    numbers = sorted(list(map(int, input().split()))[s - 1:e])
    # sortNumbers = numbers
    # print('4개 숫자 =', n, s, e, k)
    # print('숫자리스트 =', numbers)
    # print('정렬 =', sortNumbers)
    print("#%d %d" %(i + 1, numbers[k - 1]))

'''
# 강사풀이
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1:e]
    a.sort()
    print("#%d %d" %(t + 1, a[k - 1]))
'''