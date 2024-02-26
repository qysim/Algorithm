def preorder(key):

    # 루트노드 출력
    print(key, end='')

    # 왼쪽 자식이 있으면
    if tree[key][0] != '.':
        preorder(tree[key][0])

    # 오른쪽 자식이 있으면
    if tree[key][1] != '.':
        preorder(tree[key][1])


def inorder(key):

    # 왼쪽 자식이 있으면
    if tree[key][0] != '.':
        preorder(tree[key][0])

    # 루트노드 출력
    print(key, end='')

    # 오른쪽 자식이 있으면
    if tree[key][1] != '.':
        preorder(tree[key][1])


def postorder(key):

    # 왼쪽 자식이 있으면
    if tree[key][0] != '.':
        preorder(tree[key][0])

    # 오른쪽 자식이 있으면
    if tree[key][1] != '.':
        preorder(tree[key][1])

    # 루트노드 출력
    print(key, end='')


for tc in range(2):
    # 이진트리의 노드의 개수
    N = int(input())

    tree = {}

    for i in range(N):
        # 노드이름, 왼쪽자식노드, 오른쪽자식노드
        node, left, right = input().split()
        tree[node] = [left, right]

    # print(tree)

    preorder('A')
    print()

    inorder('A')
    print()

    postorder('A')
