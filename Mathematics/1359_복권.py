# 1359번: 복권

from itertools import combinations


# xCy의 개수 반환
def comb(x, y):
    if x < y:
        return 0
    data = [i for i in range(x)]
    return len(list(combinations(data, y)))


n, m, k = map(int, input().split())
result = 0

# i: 당첨 번호와 같은 수의 개수
for i in range(k, m + 1):
    result += comb(m, i) * comb(n - m, m - i) / comb(n, m)

print(result)
