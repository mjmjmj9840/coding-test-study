from collections import defaultdict

def solution(record):
    answer = []
    user_info = defaultdict(str)
    
    for r in record:
        r = r.split()  # record를 공백으로 구분
        # 채팅방 입장
        if r[0] == "Enter":
            user_info[r[1]] = r[2]  # 유저 아이디: 닉네임 저장
            answer.append(r[1] + "님이 들어왔습니다.")
        # 채팅방 퇴장
        elif r[0] == "Leave":
            answer.append(r[1] + "님이 나갔습니다.")
        # 닉네임 변경
        else:
            user_info[r[1]] = r[2]  # 유저 아이디: 닉네임 변경
    
    # 유저 아이디를 최종 닉네임으로 변경
    for i in range(len(answer)):
        idx = answer[i].index("님")
        uid = answer[i][:idx]
        answer[i] = answer[i].replace(uid, user_info[uid])
    
    return answer