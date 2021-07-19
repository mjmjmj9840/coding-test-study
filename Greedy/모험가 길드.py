N = int(input())
data = list(map(int, input().split()))  # 공포도
data.sort()

answer = 0  # 그룹의 수
people = 0  # 현재 그룹 인원 수

for x in data:
    people += 1
    # 그룹이 여행을 떠날 수 있는 경우
    if x <= people:
        people = 0
        answer += 1

print(answer)
