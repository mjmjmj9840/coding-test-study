# 양방향 연결 리스트의 노드
class Node:
    # 바로 위와 아래 행 정보를 가지고 초기화
    def __init__(self, id, before, next):
        self.id = id
        self.before = before
        self.next = next
        self.deleted = False  # 행이 삭제되었는지 여부


def solution(n, k, cmd):
    answer = ''
    cur = k  # 현재 행의 위치
    linkedList = []  # 표의 정보를 저장하는 연결 리스트
    deletedStack = []  # 지워진 행을 저장하는 스택
    for i in range(n):
        linkedList.append(Node(i, i - 1, i + 1))
    linkedList.append(Node(-1, -1, -1))  # 연결 리스트의 마지막에 더미 노드 삽입
    
    for c in cmd:
        op = c[0]  # 수행할 명령
        if op == 'U':
            x = int(c[2:])  # 위로 이동할 칸의 수
            for i in range(x):
                cur = linkedList[cur].before
        elif op == 'D':
            x = int(c[2:])  # 아래로 이동할 칸의 수
            for i in range(x):
                cur = linkedList[cur].next
        elif op == 'C':
            # 현재 행 삭제
            deletedStack.append(linkedList[cur].id)
            linkedList[cur].deleted = True
            # 삭제된 행의 위와 아래 노드 연결
            linkedList[linkedList[cur].before].next = linkedList[cur].next
            linkedList[linkedList[cur].next].before = linkedList[cur].before
            # 삭제 된 행이 가장 마지막 행인 경우 바로 윗 행 선택
            if linkedList[cur].next == n:
                cur = linkedList[cur].before
            # 그외의 경의 바로 아래 행 선택
            else:
                cur = linkedList[cur].next
        else:
            # 가장 최근에 삭제된 행 복구
            restore = deletedStack.pop()
            linkedList[restore].deleted = False
            linkedList[linkedList[restore].before].next = restore
            linkedList[linkedList[restore].next].before = restore
    
    # 삭제된 행 확인
    for i in range(n):
        if linkedList[i].deleted:
            answer += 'X'
        else:
            answer += 'O'
    
    return answer