import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, value):
        self.head = Node(value)

    def preorder(self, node): #재귀함수
        if node == None:  return  #기저 조건
        print(node.value, end='')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):  #재귀함수
        if node == None:  return  #기저 조건
        self.inorder(node.left)
        print(node.value, end='')
        self.inorder(node.right)

    def postorder(self, node):
        if node == None:  return  #기저 조건
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end='')

    def search(self, node, value):
        if node == None:  return  #기저 조건
        if node.value == value:
            global find_node
            find_node = node
            return node
        self.search(node.left, value)
        self.search(node.right, value)


tree = Tree('A')
find_node = None
n = int(sys.stdin.readline())

for _ in range(n):
    node, lNode, rNode = sys.stdin.readline().rstrip().split()
    tree.search(tree.head, node)
    if lNode != '.':
        find_node.left = Node(lNode)

    if rNode != '.':
        find_node.right = Node(rNode)

tree.preorder(tree.head); print()
tree.inorder(tree.head); print()
tree.postorder(tree.head); print()