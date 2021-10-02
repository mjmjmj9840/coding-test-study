import heapq

n = int(input())
h = [int(input()) for _ in range(n)]
heapq.heapify(h)

result = 0
for i in range(n - 1):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    result += a + b
    heapq.heappush(h, a + b)

print(result)