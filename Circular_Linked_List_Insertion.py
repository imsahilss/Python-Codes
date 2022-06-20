class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Cir_Linked_List():

    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head

    def insertAtBeginning(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        newNode.next = self.head
        self.head = newNode
        self.tail.next = self.head

    def insert_ith(self,i,data):
        newNode = Node(data)
        n = self.LLR()
        if i==0:
            self.insertAtBeginning(data)
            return
        if i==n-1:
            self.insertAtEnd(data)
            return

        count = 0
        temp = self.head
        while(temp is not None and count is not (i-1)):
            count += 1
            temp = temp.next
        if (i>count+1):
            return
        else:
            newNode.next = temp.next
            temp.next = newNode




    def LLR(self):
        temp =self.head
        count = 0
        while(temp is not None):
            count = count+1
            temp = temp.next
            if (temp==self.head):
                break
        return count

    def printCircularlist(self):
        temp = self.head
        while(True):
            #print(temp,end=' ')
            print(temp.data,end=' ')
            #print(temp.next)
            temp = temp.next
            if (temp == self.head):
                break
        print()

def main():
    c = Cir_Linked_List()
    c1 = Cir_Linked_List()
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        c.insertAtEnd(arr[i])
        c1.insertAtBeginning(arr[i])


    # c.printCircularlist()
    # c1.printCircularlist()
    # print(c.LLR())
    # print(c1.LLR())
    # c.printCircularlist()
    c.insert_ith(2,100)
    c.printCircularlist()


    #print(c.LLR())

if __name__ == '__main__':
    main()
