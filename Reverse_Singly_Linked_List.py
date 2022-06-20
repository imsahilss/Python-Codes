class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Reverse_Link_List:
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

    def Reverse_Iter(self):
        prev = None
        next = None
        curr = self.head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def Reverse_Recursive(self,curr,prev):
        if (curr is None):
            self.head = prev
            return
        next = curr.next
        curr.next = prev
        self.Reverse_Recursive(next,curr)

    def length_of_Linklist(self):
        temp = self.head
        c = 0
        while (temp is not None):
            c += 1
            temp= temp.next
        return c

    def printSinglyLinkedList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            #print(temp, end=' ')
            #print(temp.next)
            temp = temp.next
        print()

def main():
    o = Reverse_Link_List()
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        o.insertAtEnd(arr[i])
    o.Reverse_Recursive(o.head,None)
    #o.printSinglyLinkedList()

    o.printSinglyLinkedList()
if __name__ == '__main__':
    main()