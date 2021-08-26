N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x - mid > 0:
            total += (x - mid)

    # 잘린 떡의 양에 따라 높이를 조절
    if total < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
