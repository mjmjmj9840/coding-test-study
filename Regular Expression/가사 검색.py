# 효율성 1, 2, 3번 시간 초과

from collections import defaultdict
import re


def solution(words, queries):
    answer = []

    # {단어 글자 수: 해당 글자 단어 리스트} 저장
    word_dict = defaultdict(list)
    for word in words:
        word_dict[len(word)].append(word)

    for query in queries:
        cnt = 0  # 매치되는 단어 수
        length = len(query)  # query 글자 수
        # 정규 표현식 사용
        p = re.compile(query.replace('?', '.'))
        for word in word_dict[length]:
            if p.match(word):
                cnt += 1

        answer.append(cnt)

    return answer
