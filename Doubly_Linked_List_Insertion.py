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
    def insertAtBeginning(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def inseerAtGivenPosition(self,i,data):
        newNode = Node(data)
        n = self.lengthofLinkedList()
        if (i==0):
            self.insertAtBeginning(data)
            return
        if(i==n):
            self.insertAtEnd(data)
            return
        if i>n:
            print('Invalid Position')
            return
        c = 0
        temp = self.head
        while(temp.next is not None and c != (i-1)):
            c += 1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode


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
    d = Doubly_Linked_List()
    arr = list(map(int,input().split()))

    for i in range(len(arr)):
        d.insertAtEnd(arr[i])
    print(d.lengthofLinkedList())

        #d.insertAtBeginning(arr[i])
    d.inseerAtGivenPosition(6,100)

    d.printDoublyLinkList()



if __name__ == '__main__':
    main()

