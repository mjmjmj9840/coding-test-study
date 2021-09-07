def solution(N, stages):
    not_clear_player = [0] * (N + 2)  # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수
    total_player = [0] * (N + 2)  # 스테이지에 도달한 플레이어 수

    for stage in stages:
        not_clear_player[stage] += 1

    total_player[1] = len(stages)  # 1번 스테이지에 도달한 플레이어 수
    for i in range(2, N + 1):
        total_player[i] = total_player[i - 1] - not_clear_player[i - 1]

    fail = []  # (스테이지 번호, 실패율) 리스트
    for i in range(1, N + 1):
        if total_player[i] == 0:
            fail.append((i, 0))
        else:
            fail.append((i, not_clear_player[i] / total_player[i]))

    fail.sort(key=lambda x: x[1], reverse=True)  # 내림차순 정렬
    answer = [stage for stage, _ in fail]

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
