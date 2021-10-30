def solution(numbers, hand):
    answer = ''
    # 키패드의 숫자를 좌표로 표현
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    # 엄지손가락 시작 위치
    left_pos, right_pos = (3, 0), (3, 2)
    
    for n in numbers:
        n_pos = keypad[n]
        if n_pos[1] == 0:  # 왼손으로 누르는 경우
            left_pos = n_pos
            answer += 'L'
        elif n_pos[1] == 2:  # 오른손으로 누르는 경우
            right_pos = n_pos
            answer += 'R'
        else:  # 가까운 손으로 누르기
            left_dist = abs(left_pos[0] - n_pos[0]) + abs(left_pos[1] - n_pos[1])
            right_dist = abs(right_pos[0] - n_pos[0]) + abs(right_pos[1] - n_pos[1])
            if left_dist < right_dist:
                left_pos = n_pos
                answer += 'L'
            elif right_dist < left_dist:
                right_pos = n_pos
                answer += 'R'
            else:  # 왼손잡이는 왼손, 오른손잡이는 오른손
                if hand == 'left':
                    left_pos = n_pos
                    answer += 'L'
                else:
                    right_pos = n_pos
                    answer += 'R'

    return answer