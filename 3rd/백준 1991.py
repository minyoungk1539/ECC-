#첫번째 인자는 루트 두번째 인자는 왼쪽자식 세번째 인자는 오른쪽 자식-> 루트 찾기 -> 현재 트리에 없으면 루트, 자식 생성 있으면 자식만 생성
#전위순회, 중위순회, 후위순회 차례로 출력
class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

N = int(input()) #노드개수
nodes = {}

for i in range(1, N+1):
    root, left, right = input().split()  # 루트, 왼쪽자식, 오른쪽자식 묶음

    # root 노드가 없으면 생성
    if root not in nodes:
        V = BTNode(root)
        nodes[root] = V
    else:
        V = nodes[root]

    # 왼쪽 자식
    if left == '.':
        L = None
    else:
        if left not in nodes:
            nodes[left] = BTNode(left)
        L = nodes[left]

    # 오른쪽 자식
    if right == '.':
        R = None
    else:
        if right not in nodes:
            nodes[right] = BTNode(right)
        R = nodes[right]

    # 연결
    V.left = L
    V.right = R

    if V.data == 'A':
        Root = V


# 전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end='')
        preorder(n.left)
        preorder(n.right)

# 중위순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end='')
        inorder(n.right)

# 후위순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end='')

preorder(Root)
print()
inorder(Root)
print()
postorder(Root)