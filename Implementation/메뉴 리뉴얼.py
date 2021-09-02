from itertools import combinations


def solution(orders, course):
    answer = []
    all_menu = set()  # 모든 메뉴 집합

    for order in orders:
        all_menu.update(list(order))

    for n in course:
        n_result = set()  # 요리 n개 코스요리 결과
        max_cnt = 2  # 두 번 이상 주문해야 코스로 추가 가능

        candidates = set()
        for order in orders:  # 한 주문에서 만들 수 있는 후보군 생성
            if len(order) >= n:
                candidates.update(set(combinations(order, n)))

        for candidate in candidates:
            cnt = 0
            for order in orders:
                inOrder = True  # 후보 코스요리가 order에 포함되는지
                for i in range(n):
                    if candidate[i] not in order:
                        inOrder = False
                        break
                if inOrder:
                    cnt += 1

            if cnt == max_cnt:  # 주문 횟수가 같다면 result에 추가
                n_result.add(''.join(sorted(candidate)))
            elif cnt > max_cnt:  # 이전까지의 주문은 없애고 현재 주문만 추가
                n_result = {''.join(sorted(candidate))}
                max_cnt = cnt

        for r in n_result:
            answer.append(r)

    return sorted(answer)



# 천재의 풀이
'''
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
        
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ] 
'''