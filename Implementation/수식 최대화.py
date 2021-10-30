from itertools import permutations
import copy

def solution(expression):
    answer = 0
    # expression을 숫자와 연산으로 분리하여 리스트로 저장
    exp_list = []
    idx = 0  # 숫자가 시작되는 인덱스
    for i in range(len(expression)):
        # 연산자일 경우에 exp_list에 숫자와 연산 추가
        if not expression[i].isdigit():
            exp_list.append(int(expression[idx:i]))  # 연산자 앞의 수
            exp_list.append(expression[i])  # 연산자
            idx = i + 1
    # 마지막 수 추가
    exp_list.append(expression[idx:])
    
    # 모든 경우의 수 탐색
    for priority in permutations(['-', '+', '*'], 3):
        temp = copy.deepcopy(exp_list)  # 연산에 사용할 임시 리스트
        # 우선 순위가 높은 순서대로 연산 수행
        for i in range(3):
            j = 0
            while j < len(temp):
                if temp[j] == priority[i]:
                    num1 = temp[j - 1]
                    num2 = temp[j + 1]
                    result = eval(str(num1) + temp[j] + str(num2))
                    temp.pop(j - 1)
                    temp.pop(j - 1)
                    temp.pop(j - 1)
                    temp.insert(j - 1, result)
                    j -= 1
                j += 1
        # 최종 연산 결과 중 최대값 선택
        answer = max(answer, abs(temp[0]))
            
    return answer