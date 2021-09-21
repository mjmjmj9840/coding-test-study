# 올바른 괄호 문자열인지 판단하는 함수
def isCorrect(p):
    cnt = 0
    for x in p:
        if x == '(':
            cnt += 1
        elif cnt > 0:
            cnt -= 1
        else:
            return False

    return True if cnt == 0 else False


# 올바른 괄호 문자열로 변환하는 함수
def makeCorrect(p):
    if isCorrect(p):  # 올바른 괄호 문자열인 경우
        return p

    left, right = 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 균형잡힌 괄호 문자열
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if isCorrect(u):
        return u + makeCorrect(v)

    result = '(' + makeCorrect(v) + ')'
    for i in range(1, len(u) - 1):  # 괄호 방향 뒤집어서 이어 붙이기
        if u[i] == '(':
            result += ')'
        else:
            result += '('

    return result


def solution(p):
    return makeCorrect(p)
