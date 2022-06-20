class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def printMiddle(self):

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)



    def printSinglyLinkedList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():

    t = int(input())
    while t>0:
        singlyLinkedList = LinkedList()
        n = int(input())
        arr = list(map(int, input().split()))
        for i in range(n):
            singlyLinkedList.insertAtEnd(arr[i])
        singlyLinkedList.printMiddle()
        t = t-1

if __name__ == '__main__':
    main()