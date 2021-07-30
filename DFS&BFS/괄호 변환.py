# 괄호 변환

def dfs(w):
    if w == '':
        return ''

    left = 0  # '('의 개수
    right = 0  # ')'의 개수

    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    u = w[:i + 1]
    v = w[i + 1:]

    if correct(u):
        return u + dfs(v)
    else:
        # u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향 뒤집은 문자열
        temp = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        return '(' + dfs(v) + ')' + temp


# 올바른 문자열인지 판단
def correct(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True


def solution(p):
    answer = dfs(p)
    return answer
