class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.addNode(self.root, data)

    def addNode(self,node,data):
        if(node is None):
            #newNode = Node(data)
            return Node(data)

        if(data < node.data):
            node.left = self.addNode(node.left, data)

        else:
            node.right = self.addNode(node.right, data)

        return node

    def preOrder(self, node):
        if(node is None):
            return

        print(node.data, end = " ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if (node is None):
            return

        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)

    def search(self,node,data):
        if(node is None or node.data==data):
            return node

        if(data<node.data):
            return self.search(node.left,data)
        else:
            return self.search(node.right,data)


def main():
    arr = list(map(int, input().split()))
    bst = BST()
    for ele in arr:
        bst.insert(ele)

    bst.preOrder(bst.root)
    print()
    bst.inOrder(bst.root)
    print()
    ele = int(input())
    if(bst.search(bst.root,ele)==None):
        print('Search ele is not present')
    else:
        print('Search ele is present')

if __name__ == '__main__':
    main()