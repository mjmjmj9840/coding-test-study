import heapq

def solution(play_time, adv_time, logs):
    answer = 0
    # 시각을 모두 초로 변환
    play_time = (int(play_time[:2]) * 60 + int(play_time[3:5])) * 60 + int(play_time[6:])
    adv_time = (int(adv_time[:2]) * 60 + int(adv_time[3:5])) * 60 + int(adv_time[6:])
    for i in range(len(logs)):
        start, end = logs[i].split('-')
        start = (int(start[:2]) * 60 + int(start[3:5])) * 60 + int(start[6:])
        end = (int(end[:2]) * 60 + int(end[3:5])) * 60 + int(end[6:])
        logs[i] = (start, end)

    logs.sort()  # 재생 기록 오름차순 정렬

    total_time = [0] * play_time  # 누적 재생시간
    i = 0  # log index
    h = []  # 시청 종료 시각 체크를 위한 heapq
    cnt = 0  # 시청자 수
    for t in range(play_time):  # 매초마다 누적 시청자 수 계산
        while i < len(logs) and logs[i][0] == t:  # 현재 시각에 시청을 시작하는 경우
            cnt += 1
            heapq.heappush(h, logs[i][1])  # 시청 종료 시각 삽입
            i += 1
        while h and h[0] == t:  # 현재 시각에 시청을 종료하는 경우
            cnt -= 1
            heapq.heappop(h)
        total_time[t] = cnt

    for t in range(1, play_time):  # 0초부터 (t + 1)초까지의 누적 재생 시간
        total_time[t] = total_time[t] + total_time[t - 1]

    max_ttime = total_time[adv_time - 1]  # 최대 누적 재생시간
    for adv_start in range(1, play_time - adv_time + 1):
        adv_end = adv_start + adv_time
        ttime = total_time[adv_end - 1] - total_time[adv_start - 1]
        if ttime > max_ttime:
            max_ttime = ttime
            answer = adv_start

    hour = str(answer // 3600).zfill(2)
    minute = str((answer // 60) % 60).zfill(2)
    second = str(answer % 60).zfill(2)

    return hour + ':' + minute + ':' + second
