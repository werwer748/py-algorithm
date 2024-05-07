import sys
sys.stdin = open("in1.txt", "rt")

'''
# 내 풀이
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
sumList = []

for v1 in range(n):
    for v2 in range(n):
        for v3 in range(n):
            if (v1 < v2 < v3):
                sumList.append(numbers[v1] + numbers[v2] + numbers[v3])

removeDup = sorted(list(set(sumList)), reverse=True)
print(removeDup[k - 1])
'''

# 강사 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
#? set(): 중복을 제거함.
res = set()
for i in range(n):
    for j in range(i + 1, n): # i + 1로 앞에 수 스킵
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m]) # 바로 중복제거하면서 set 자료구조에 추가

res = list(res)
res.sort(reverse=True)
print(res[k - 1])