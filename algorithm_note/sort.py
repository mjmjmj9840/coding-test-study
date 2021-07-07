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




''' 삽입 정렬 '''

def ins_sort(array):
  for i in range(1, len(array)):
    for j in range(i, 0, -1):
      if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
        array[j], array[j - 1] = array[j - 1], array[j]
      else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        break

  return array

# 시간복잡도: O(N^2)
# 최선의 경우: O(N)
