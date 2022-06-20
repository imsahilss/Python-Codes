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

    def deletionAtEnd(self):
        if (self.head is None):
            print('Linked List is Empty')
            return
        temp = self.tail.prev
        temp.next = None
        self.tail.prev = None
        self.tail = temp

    def deletionAtBeginning(self):
        if(self.head is None):
            print('Linked List is Empty')
            return
        temp = self.head.next
        if temp is None:
            self.head = None
            return
        self.head.next = None
        temp.prev = None
        self.head = temp

    def deletionAtGivenPosition(self,i):
        n = self.lengthofLinkedList()
        if (i>=n):
            print('Invalid Position')
            return
        if (i==0):
            self.deletionAtBeginning()
            return
        if (i==n-1):
            self.deletionAtEnd()
            return
        c = 0
        temp = self.head
        while(temp is not None and c is not i):
            c = c+1
            temp = temp.next
        temp1 = temp.prev
        temp2 = temp.next
        temp.prev = None
        temp.next = None
        temp1.next = temp2
        temp2.prev = temp1



    def printDoublyLinkList(self):
        temp = self.head
        while (temp is not None):
            #print(temp.prev, end=' ')
            print(temp.data, end=' ')
            #print(temp,end=' ')
            #print(temp.next)
            temp = temp.next
        print()

    def lengthofLinkedList(self):
        temp = self.head
        c = 0
        while (temp is not None):
            c += 1
            temp = temp.next
        return c

def main():
    d = Doubly_Linked_List()
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        d.insertAtEnd(arr[i])
    #print(d.lengthofLinkedList())
    d.deletionAtGivenPosition(2)
    # d.deletionAtEnd()
    d.printDoublyLinkList()
    d.deletionAtGivenPosition(0)
    # d.deletionAtBeginning()
    d.printDoublyLinkList()
    d.deletionAtGivenPosition(d.lengthofLinkedList() - 1)
    d.printDoublyLinkList()


if __name__ == '__main__':
    main()