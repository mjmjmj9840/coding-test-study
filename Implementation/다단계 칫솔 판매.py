# 부모에게 10%씩 이윤 배분
def share_with_parent(parent, answer, x, money):
    if money < 10:  # 10%가 1원 미만인 경우
        answer[x] += money
        return

    ten_percent = int(money * 0.1)
    answer[x] += money - ten_percent
    if parent[x] == -1:  # center까지 배분한 경우
        return
    share_with_parent(parent, answer, parent[x], ten_percent)


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    member = {}  # 구성원 이름: enroll의 인덱스 딕셔너리
    parent = [-1] * len(enroll)  # 추천인 저장 -1: center

    for i in range(len(enroll)):
        member[enroll[i]] = i

    for i in range(len(referral)):
        if referral[i] != "-":
            parent[i] = member[referral[i]]

    for i in range(len(seller)):
        x = member[seller[i]]  # 판매자 인덱스
        money = amount[i] * 100  # 판매 이익
        share_with_parent(parent, answer, x, money)

    return answer

