# 210928 재풀이
import heapq

def solution(food_times, k):
    answer = -1
    h = []  # (남은 음식 양, 음식 번호) 우선순위 큐
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))
    
    n = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 먹은 음식의 양
    while h:
        # 먹는데 걸리는 시간 = (현재 음식 양 - 이전에 먹은 음식 양) * 남은 음식 개수
        t = (h[0][0] - previous) * n
        # k초까지 시간이 남은 경우 현재 음식 삭제
        if t <= k:
            k -= t
            n -= 1
            previous, _ = heapq.heappop(h)
        # k초가 지난 경우 (k + 1)초의 음식 번호 찾기
        else:
            h.sort(key=lambda x: x[1])  # 음식 번호 순서대로 정렬
            answer = h[k % n][1]
            break
    
    return answer