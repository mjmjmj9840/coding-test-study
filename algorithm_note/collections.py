'''deque'''

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)  # 제일 왼쪽에 1 삽입
data.append(5)  # 제일 오른쪽에 5 삽입
data.pop()  # 제일 오른쪽 원소(5) 삭제
data.popleft()  # 제일 왼쪽 원소(1) 삭제





'''Counter'''

from collections import Counter

data = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(data)
dict(counter) # {'red': 2, 'blue': 3, 'green': 1}
