def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        result = ""
        previous = s[0:i]  # 이전에 압축한 문자열
        count = 1  # 압축된 문자열의 반복 횟수
        for j in range(i, len(s), i):
            now = s[j:j + i]
            if previous == now:
                count += 1
            else:
                # 이전 문자열을 결과에 추가
                if count == 1:
                    result += previous
                else:
                    result += str(count) + previous
                previous = now
                count = 1

        # 마지막 문자열 압축 결과를 추가
        if count == 1:
            result += previous
        else:
            result += str(count) + previous

        answer = min(answer, len(result))

    return answer
