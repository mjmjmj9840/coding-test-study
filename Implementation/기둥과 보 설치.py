# 기둥과 보 설치

def possible(answer):
  for x, y, frame in answer:
    # 기둥의 조건: 1. 바닥 위 2. 보 한쪽 끝 위 3. 다른 기둥 위
    if frame == 0:
      if not(y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer):
        return False
    # 보의 조건: 1. 한쪽 끝이 기둥 위 2. 양쪽 끝이 다른 보와 연결
    else:
      if not([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
        return False
      
  return True


def solution(n, build_frame):
    answer = []
    for x, y, frame, op in build_frame:
        if op == 0:
          answer.remove([x, y, frame])
          # 조건 불만족 시 해당 작업 무시
          if not possible(answer):
            answer.append([x, y, frame])
        else:
          answer.append([x, y, frame])
          # 조건 불만족 시 해당 작업 무시
          if not possible(answer):
            answer.remove([x, y, frame])

    return sorted(answer)
