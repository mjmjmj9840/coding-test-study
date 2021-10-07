from collections import defaultdict
from bisect import bisect_left, bisect_right


# 키워드와 매치되는 단어의 개수 구하기
def getMatchNums(query, array):
    # 가능한 단어의 시작과 끝
    start_word = query.replace('?', 'a')
    end_word = query.replace('?', 'z')
    # 시작 단어와 끝 단어의 위치 구하기
    left_idx = bisect_left(array[len(query)], start_word)
    right_idx = bisect_right(array[len(query)], end_word)

    return right_idx - left_idx


def solution(words, queries):
    answer = []
    word_dict = defaultdict(list)  # {단어 길이: 해당 길이의 단어 리스트} 정보
    reverse_word_dict = defaultdict(list)  # 단어를 뒤집어서 저장

    for word in words:
        word_dict[len(word)].append(word)
        reverse_word_dict[len(word)].append(word[::-1])
    
    for i in word_dict.keys():
        # 단어 정렬
        word_dict[i].sort()
        reverse_word_dict[i].sort()

    for query in queries:
        # 키워드가 ?로 시작하는 경우 reverse_word_dict에서 찾음
        if query[0] == '?':
            answer.append(getMatchNums(query[::-1], reverse_word_dict))
        else:
            answer.append(getMatchNums(query, word_dict))

    return answer