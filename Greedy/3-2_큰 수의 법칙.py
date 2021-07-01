N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse = True) # 내림차순 정렬
answer = 0

# (K + 1)번이 반복되는 횟수
count = M // (K + 1)
answer += (numbers[0] * K + numbers[1]) * count
# 나머지 횟수
answer += numbers[0] * (M % (K + 1))

print(answer)
