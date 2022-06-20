class Node:
    def __init__(self, data):
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

    def length_of_Linklist(self):
        temp = self.head
        c = 0
        while (temp is not None):
            c += 1
            temp= temp.next
        return c

    def LLR(self,temp):
        if(temp is None):
            return 0
        return 1 + self.LLR(temp.next)




    def printSinglyLinkedList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            print(temp, end=' ')
            print(temp.next)
            temp = temp.next


def main():
    SinglyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        SinglyLinkedList.insertAtEnd(arr[i])

    temp = SinglyLinkedList.head
    print(SinglyLinkedList.LLR(temp))
    print(SinglyLinkedList.length_of_Linklist())
    SinglyLinkedList.printSinglyLinkedList()


if __name__ == '__main__':
    main()