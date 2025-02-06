"""
* 합이 같은 부분집합(DFS: 아마존 인터뷰)

N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어야 합니다.
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이
16으로 같은 경우가 존재하는 것을 알 수 있다.
"""
import sys
from collections import deque
sys.stdin = open("in4.txt")

def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 전체 종료
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)

# 강사 풀이
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")



'''
# 내 풀이
n = int(input())
a = list(map(int, input().split()))
res = "NO"

for i in range(n):
    a[i] = {"val": a[i], "use": False}



def DFS(v):
    global res

    if v == n:
        true_sum = 0
        false_sum = 0

        for x in a:
            if x["use"]:
                true_sum += x["val"]
            else:
                false_sum += x["val"]

        if true_sum == false_sum:
            res = "YES"
            return
        return
    a[v]["use"] = True
    DFS(v + 1)
    a[v]["use"] = False
    DFS(v + 1)


DFS(0)
print(res)
'''