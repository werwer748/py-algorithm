''' 버블 정렬 '''
l = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(l)):
    for j in range(1, len(l) - i):
        if l[j - 1] >= l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]

print(l)

''' 삽입 정렬 '''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [5, 3, 8, 6, 2]
print(insertion_sort(arr))

''' 퀵 정렬 '''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 3, 8, 6, 2]
print(quick_sort(arr))

''' 병합 정렬 '''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5, 3, 8, 6, 2]
print(merge_sort(arr))

''' 힙 정렬 '''
import heapq

def heap_sort(arr):
    heap = []
    for elem in arr:
        heapq.heappush(heap, elem)

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

arr = [5, 3, 8, 6, 2]
print(heap_sort(arr))