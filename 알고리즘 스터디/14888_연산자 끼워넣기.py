# 14888번: 연산자 끼워넣기

# add, sub, mul, div: 현재까지 사용한 연산자 개수
# value: 현재까지의 계산값
# i: 현재 처리해야 하는 숫자의 index
def backtracking(add, sub, mul, div, value, i):
    global min_value, max_value
    # 연산자를 초과하여 쓴 경우 pruning
    if add > ops[0] or sub > ops[1] or mul > ops[2] or div > ops[3]:
        return

    # 연산자를 모두 사용한 경우 최댓값, 최솟값 갱신
    if i == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return

    # 4가지 연산에 대해 계산
    backtracking(add + 1, sub, mul, div, value + nums[i], i + 1)
    backtracking(add, sub + 1, mul, div, value - nums[i], i + 1)
    backtracking(add, sub, mul + 1, div, value * nums[i], i + 1)
    # 음수 계산 처리
    if value < 0:
        backtracking(add, sub, mul, div + 1, -(-value // nums[i]), i + 1)
    else:
        backtracking(add, sub, mul, div + 1, value // nums[i], i + 1)


n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_value = 1000000001
max_value = -1000000001

backtracking(0, 0, 0, 0, nums[0], 1)
print(max_value)
print(min_value)
