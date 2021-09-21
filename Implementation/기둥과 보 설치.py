# [x, y, a] 구조물이 규칙에 맞는지 확인
def check(answer, x, y, a):
    if a == 0:  # 기둥
        if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
            return True
        return False
    else:  # 보
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
            return True
        return False


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            for i, j, k in answer:  # 모든 구조물 검사
                # 규칙에 맞지 않으면 복구
                if not check(answer, i, j, k):
                    answer.append([x, y, a])
                    break
        else:
            answer.append([x, y, a])
            # 규칙에 맞지 않으면 복구
            if not check(answer, x, y, a):
                answer.pop()

    return sorted(answer)
