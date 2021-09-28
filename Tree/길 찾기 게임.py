import sys
sys.setrecursionlimit(10**6)

class BinaryTree:
    def __init__(self, node_list):
        # 가장 큰 y값을 가진 노드가 현재 노드
        self.data = max(node_list, key=lambda x: x[0][1])
        self.left = None  # 왼쪽 서브트리
        self.right = None  # 오른쪽 서브트리
        # 현재 노드의 x값보다 작은 노드들
        left_node_list = list(filter(lambda x: x[0][0] < self.data[0][0], node_list))
        # 현재 노드의 x값보다 큰 노드들
        right_node_list = list(filter(lambda x: x[0][0] > self.data[0][0], node_list))
        
        if left_node_list:
            self.left = BinaryTree(left_node_list)
        if right_node_list:
            self.right = BinaryTree(right_node_list)


# 트리 순회 함수
def visit(binary_tree, preorder, postorder):
    preorder.append(binary_tree.data[1])
    if binary_tree.left:  # 왼쪽 자식이 있을 경우
        visit(binary_tree.left, preorder, postorder)
    if binary_tree.right:  # 오른쪽 자식이 있을 경우
        visit(binary_tree.right, preorder, postorder)
    postorder.append(binary_tree.data[1])
    

def solution(nodeinfo):
    # ([x축 좌표, y축 좌표], 노드 번호) 값을 저장하도록 변경
    for i in range(len(nodeinfo)):
        nodeinfo[i] = (nodeinfo[i], i + 1)
    
    binary_tree = BinaryTree(nodeinfo)  # 이진 트리 초기화
    preorder = []
    postorder = []
    visit(binary_tree, preorder, postorder)  # 트리 순회
    answer = [preorder, postorder]
    
    return answer