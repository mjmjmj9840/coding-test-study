''' 선택 정렬 '''

def sel_sort(array):
  for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

  return array

# 시간복잡도: O(N^2)
