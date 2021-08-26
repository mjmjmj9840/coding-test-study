# 외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)  # 취약 지점의 개수
    for i in range(length):  # 원형을 일자 형태로 전환
      weak.append(weak[i] + n)

    for start in range(length):
      # 친구를 나열하는 모든 방법
      for friends in list(permutations(dist, len(dist))):
        count = 1  # 외벽 점검에 보낼 친구 수
        visit = weak[start] + friends[count - 1]  # 점검 가능한 위치 중 가장 큰 값
        # 점검해야할 모든 외벽 검사
        for i in range(start, start + length):
          if weak[i] > visit:
            count += 1  # 친구 추가
            if count > len(dist):
              break  # 모든 외벽 점검 불가
            visit = weak[i] + friends[count - 1]  # 점검 가능 위치 갱신
            
        answer = min(answer, count)  # 보내야하는 최소 친구 수

    return answer if answer <= len(dist) else -1
