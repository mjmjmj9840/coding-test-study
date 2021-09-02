from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


# javabackendjuniorpizza 형식으로 16가지 경우의 수 저장
def insertDict(info_dict, data):
    info_dict['----'].append(int(data[4]))
    for i in range(1, 5):
        for c in combinations([0, 1, 2, 3], i):
            key = ''
            for j in range(4):
                if j in c:
                    key += data[j]
                else:
                    key += '-'
            info_dict[key].append(int(data[4]))


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in range(len(info)):
        data = info[i].split(' ')
        insertDict(info_dict, data)

    for key in info_dict.keys():  # 점수 오름차순 정렬
        info_dict[key].sort()

    for q in query:
        data = q.split(' ')
        key = data[0] + data[2] + data[4] + data[6]
        score = int(data[-1])
        values = info_dict[key]  # 점수를 제외한 쿼리에 해당하는 지원자들의 점수

        cnt = len(values) - bisect_left(values, score)  # 이분 탐색

        answer.append(cnt)

    return answer
