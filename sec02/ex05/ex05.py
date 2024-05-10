'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''
import sys
sys.stdin = open("in5.txt", "rt")

'''
# 내 풀이
n, m = map(int,input().split())
allSumList = []
for x in range(1, n + 1):
    for y in range(1, m + 1):
        allSumList.append(x + y)

setAllSumList = list(set(allSumList))

count = list(range(len(setAllSumList)))
for i, s in enumerate(setAllSumList):
    count[i] = 0
    for a in allSumList:
        if s == a:
            count[i] = count[i] + 1

maxCnt = max(count)

result = []
for i, c in enumerate(count):
    if c == maxCnt:
        result.append(setAllSumList[i])

result.sort()
for r in result:
    print(r, end=' ')
print()
'''

'''
# 강사 풀이
n, m = map(int,input().split())

cnt = [0] * (n + m + 2) #? 두눈 최고수 합으로 미리 카운팅 리스트 범위를 잡는다(range에서 +1이붙으니까 여유분(2)을 조금 더 준다.)
max = -2147000000 # 가장작은값으로 초기화
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
'''

# 내풀이 최적화 해보기
n, m = map(int,input().split())

maxRange = n + m + 1
cnt = [0] * maxRange

for x in range(1, n + 1):
    for y in range(1, m + 1):
        cnt[x + y] += 1

maxCnt = max(cnt)
for i in range(maxRange):
    if cnt[i] == maxCnt:
        print(i, end=' ')


