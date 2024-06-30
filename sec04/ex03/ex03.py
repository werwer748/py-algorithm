"""
뮤직비디오(결정알고리즘)
지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
DVD에는 총 N개의 곡이 들어가는데, DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지 되어야 한다. 순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다.
즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다.
또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 이 사업에 낭비되는 DVD를 가급적 줄이려고 한다.
고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 하였다.
이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 꼭 같은 크기로 해야 한다.

입력 설명
첫째 줄에 자연수 N(1≤N≤1,000), M(1≤M≤N)이 주어진다.
다음 줄에는 조영필이 라이브에서 부른 순서대로 부른 곡의 길이가 분 단위로(자연수) 주어진다.
부른 곡의 길이는 10,000분을 넘지 않는다고 가정하자.

출력 설명
첫 번째 줄부터 DVD의 최소 용량 크기를 출력하세요.
"""
import sys
sys.stdin = open("in5.txt", "rt")

# 재풀이
n, m = map(int, input().split()) # n = 곡수, m = DVD 수
songs = list(map(int, input().split()))
maxSong = max(songs)

sumSongs = sum(songs) # 1장에 모두 담을 수 있는 용량
res = 0 # 최소 몇분짜리 DVD여야 하는가?

lt = 1
rt = sumSongs

def checker(mid):
    cnt = 1
    tmp = 0
    for x in songs:
        tmp += x
        if tmp > mid:
            cnt += 1
            tmp = x
    if cnt <= m:
        return True
    else:
        return False


while lt <= rt:
    mid = (lt + rt) // 2
    if checker(mid) and mid >= maxSong:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)



"""
#! 못풀어서 강의보고 클론코딩... 문제 이해가 어려움
n, m = map(int, input().split()) # n = 부른 곡수, m = 소속사에서 찍어내려는 DVD 개수
music = list(map(int, input().split()))
max_m = max(music)

lt = 1
rt = sum(music)
res = 0

def checker(capacity):
    cnt = 1
    dvd_sum = 0
    for x in music:
        if dvd_sum + x > capacity:
            cnt += 1
            dvd_sum = x
        else:
            dvd_sum += x
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_m and checker(mid) <= m:
        res = mid
        rt = mid - 1 # 더 작은 범위 탐색
    else:
        lt = mid + 1
print(res)
"""


