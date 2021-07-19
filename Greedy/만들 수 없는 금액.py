N = input()
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    # target을 만들 수 없는 경우
    if target < coin:
        break
    target += coin

print(target)
