''' 이진 탐색 '''

# 재귀함수로 구현한 이진 탐색
# array 내의 target의 인덱스 반환
def binarySearch(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binarySearch(array, target, start, mid - 1)
  else:
    return binarySearch(array, target, mid + 1, end)



# 반복문으로 구현한 이진 탐색
# array 내의 target의 인덱스 반환
def binarySearch2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
    return None



# 사용 예시
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 9

result = binarySearch2(array, target, 0, len(array) - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result)
