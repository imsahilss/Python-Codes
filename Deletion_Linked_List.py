class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def deletionAtEnd(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            sl = self.head
            while (sl.next.next is not None):
                sl = sl.next
            self.tail = sl
            sl.next = None

    def deletionAtBeginning(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next

    def deletionAtGivenPosition(self,i):
        n = self.LLR(self.head)
        if (self.head is None or i>n-1):
            return
        if i==0:
            self.deletionAtBeginning()
            return
        if (i==n-1):
            self.deletionAtEnd()
            return
        count = 0
        temp = self.head
        while(temp is not None and count!=i-1):
            count += 1
            temp = temp.next
        temp.next = temp.next.next




    def LLR(self,temp):
        if(temp is None):
            return 0
        return 1 + self.LLR(temp.next)

    def printLinkList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            #print(temp, end=' ')
            #print(temp.next)
            temp = temp.next
        print()


def main():
    l = Linked_List()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        l.insertAtEnd(arr[i])
    temp = l.head
    print(l.LLR(temp))
    l.deletionAtGivenPosition(2)
    #l.deletionAtEnd()
    #l.deletionAtBeginning()

    l.printLinkList()

if __name__=='__main__':
    main()