class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def rotateNnode(self, N):
        temp = self.head
        count = 0
        while(temp is not None and count is not N-1):
            temp = temp.next
            count = count+1
        temp2 = temp.next
        temp.next = None
        temp2.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = temp2
        self.tail = temp




    def printDoublyLinkList(self):
        temp = self.head
        while (temp is not None):
            #print(temp.prev, end=' ')
            print(temp.data, end=' ')

            #print(temp,end=' ')
            #print(temp.next)
            temp = temp.next

    def lengthofLinkedList(self):
        temp = self.head
        c = 0
        while (temp is not None):
            c += 1
            temp = temp.next
        return c

def main():
    t = int(input())
    while(t>0):
        d = Doubly_Linked_List()
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))

        for i in range(len(arr)):
            d.insertAtEnd(arr[i])
        d.rotateNnode(k)
        d.printDoublyLinkList()
        t -= 1


if __name__ == '__main__':
    main()
