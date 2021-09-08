from itertools import combinations

def solution(relation):
    answer = []  # 후보키 리스트
    col_length = len(relation[0])  # 컬럼 개수

    for key_num in range(1, col_length + 1):
        candidates = list(combinations([i for i in range(col_length)], key_num))

        for cand in candidates:
            row_set = set()  # 후보키 컬럼 값들의 집합
            is_unique = True
            for row in relation:
                selection = tuple(row[i] for i in cand)  # 후보키 컬럼의 값만 뽑기
                if selection in row_set:
                    is_unique = False
                    break
                else:
                    row_set.add(selection)
            if not is_unique:  # 유일성을 만족하지 않을 경우
                continue

            is_minimal = True
            for key in answer:
                if key <= set(cand):  # 최소성을 만족하지 않을 경우
                    is_minimal = False
                    break
            if is_minimal:
                answer.append(set(cand))

    return len(answer)
