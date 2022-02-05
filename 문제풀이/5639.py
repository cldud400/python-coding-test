import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, value):
        self.head = Node(value)

    #부모노드보다 작으면 왼쪽, 크면 오른쪽 노드로 추가
    def addNode(self, value):
        node = self.head  #최상위 노드
        newNode = Node(value)
        while True:
            if value < node.value:    #값이 현재 노드보다 작으면 왼쪽에 추가
                if node.left != None:   #왼쪽에 자식 노드가 있으면, 자식 노드를 검사
                    node = node.left
                else: # 왼쪽에 자식 노드가 없으면 그냥 추가하면 된다
                    node.left = newNode
                    break
            else:  #값이 현재 노드보다 크면 오른쪽에 추가
                if node.right != None:
                    node = node.right
                else:
                    node.right = newNode
                    break

    def postorder(self, node):
        if node == None:  return  #기저 조건
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)

sys.setrecursionlimit(100000)
input_list = list(map(int, sys.stdin.read().rstrip().split()))  #한번에 입력 처리하기
tree = Tree(input_list[0])
for x in input_list[1:]:
    tree.addNode(x)
# n = int(sys.stdin.readline())
# tree = Tree(n)
# while True:    #입력 갯수가 정해지지 않음
#     try:
#         n = int(sys.stdin.readline())
#         tree.addNode(n)
#     except:
#         break
tree.postorder(tree.head)
