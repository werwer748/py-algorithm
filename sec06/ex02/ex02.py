"""
이진 트리 순회 연습하기

* 전위 순회 출력
부모 -> 왼쪽 자식 -> 오른쪽 자식
ex) 1 2 4 5 3 6 7

* 중위 순회 출력
왼쪽 자식 -> 부모 -> 오른쪽 자식
ex) 4 2 5 1 6 3 7

* 후위 순회 출력
왼쪽 자식 -> 오른쪽 자식 -> 부모
ex) 4 5 2 6 7 3 1
"""

#* 전위 순회 출력 - 자기의 일을 먼저 처리
def DFS1(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS1(v * 2)
        DFS1(v * 2 + 1)

#* 중위 순회 출력 - 자기의 일을 중간에 처리
def DFS2(v):
    if v > 7:
        return
    else:
        DFS2(v * 2)
        print(v, end=' ')
        DFS2(v * 2 + 1)

#* 후위 순회 출력 - 자기의 일을 마지막에 처리
def DFS3(v):
    if v > 7:
        return
    else:
        DFS3(v * 2)
        DFS3(v * 2 + 1)
        print(v, end=' ')

if __name__ == "__main__":
    DFS1(1)
    print('', end="\n")
    DFS2(1)
    print('', end="\n")
    DFS3(1)
