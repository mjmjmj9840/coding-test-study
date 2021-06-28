'''bisect(binary search)'''

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_left(a, x)  # 2
# 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 반환
bisect_right(a, x) # 4
 




'''정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구하기'''

from bisect import bisect_left, bisect_right

# 값이 [l_value, r_value]인 원소의 개수를 반환하는 함수
def count_by_range(a, l_value, r_value):
  l_index = bisect_left(a, l_value)
  r_index = bisect_right(a, r_value)
  
  return r_index - l_index
