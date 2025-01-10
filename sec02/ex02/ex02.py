'''
K번째 수
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세
'''

import sys
sys.stdin = open("in5.txt", "rt")

# 내 풀이
t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))[s - 1: e]
    num_list.sort()

    # print(num_list)
    print("#%d %d" % (i + 1, num_list[k - 1]))
