class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if(root is None):
        return

    print(root.data,end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if(root is None):
        return

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=' ')


def inOrderTraversal(root):
    if (root is None):
        return

    inOrderTraversal(root.left)
    print(root.data, end=' ')
    inOrderTraversal(root.right)

def heightofTree(root):
    if(root is None):
        return -1
    lside = heightofTree(root.left)
    rside = heightofTree(root.right)
    if(lside>rside):
        return lside+1
    else:
        return rside+1

def sizeofBT(root):
    if(root is None):
        return 0
    #without storing values
    #return sizeofBT(root.left) + sizeofBT(root.right) + 1
    #with storing values
    lside = sizeofBT(root.left)
    rside = sizeofBT(root.right)

    return lside + rside + 1



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

    print(sizeofBT(root))


    preOrderTraversal(root)
    print()
    postOrderTraversal(root)
    print()
    inOrderTraversal(root)

if __name__=='__main__':
    main()
