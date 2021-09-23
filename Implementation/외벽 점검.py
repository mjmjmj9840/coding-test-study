# 다시 푼 풀이
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_cnt = len(weak)  # 취약 지점 개수
    for i in range(weak_cnt):  # 취약 지점을 직선으로 표현
        weak.append(weak[i] + n)

    for start in range(weak_cnt):  # 점검 시작 위치
        end = start + weak_cnt  # 점검 종료 위치

        for friend in list(permutations(dist, len(dist))):  # 친구를 보내는 순서
            checked = weak[start] - 1  # 점검 완료 지점
            f_idx = 0
            for i in range(start, end):
                if weak[i] > checked:  # 다음 친구를 보냄
                    if f_idx >= len(dist):  # 취약 지점을 전부 점검할 수 없는 경우
                        f_idx += 1
                        break
                    checked = weak[i] + friend[f_idx]
                    f_idx += 1

            answer = min(answer, f_idx)

    return answer if answer <= len(dist) else -1
