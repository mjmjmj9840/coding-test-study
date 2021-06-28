'''permutations'''

# data 객체에서 3개의 원소를 뽑아 나열하는 모든 경우(순서O 중복X)
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]



'''combinations'''

# data 객체에서 2개의 원소를 뽑는 모든 경우(순서X 중복X)
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]



'''product'''

# data 객체에서 2개의 원소를 뽑아 나열하는 모든 경우(순서O 중복O)
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat = 2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
 

'''combinations_with_replacement'''

# data 객체에서 2개의 원소를 뽑는 모든 경우(순서X 중복O)
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
