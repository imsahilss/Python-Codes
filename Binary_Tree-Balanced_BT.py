class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right  = None

def preOrderTraversal(root):
    if(root is None):
        return

    print(root.data,end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def heightofTree(root):
    if(root is None):
        return -1
    lside = heightofTree(root.left)
    rside = heightofTree(root.right)
    if(lside>rside):
        return lside+1
    else:
        return rside+1

def isBalanced(root):
    if(root is None):
        return True
    lh = heightofTree(root.left)
    rh = heightofTree(root.right)
    if(abs(lh-rh)>1):
        return False

    lside = isBalanced(root.left)
    rside = isBalanced(root.right)

    if (lside and rside):
        return True
    else:
        return False

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.left.right.left = Node(9)
    root.left.left.right.left.left = Node(10)
    print(heightofTree(root))
    print(isBalanced(root))

if __name__=='__main__':
    main()
