class QueueUsingList:
    def __init__(self):
        self.que = []
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        self.que.append(data)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        if(self.isEmpty()):
            print('Queue is Empty')
            return

        temp = self.que[self.front]
        self.front += 1
        self.size -= 1
        return temp

    def frontele(self):
        if(self.isEmpty()):
            print('Queue is Empty')
            return
        return self.que[self.front]

    def printQueue(self):
        if (self.isEmpty()):
            print('Queue is Empty')
            return

        for i in range(self.size):
            print(self.que[self.front + i], end = ' ')
        print()

def main():
    q = QueueUsingList()
    for ele in input().split():
        q.enqueue(int(ele))
    q.printQueue()
    n = 3
    while n>0:
        print(q.frontele())
        q.dequeue()
        n = n-1
    q.printQueue()
    q.enqueue(100)
    q.printQueue()
    q.enqueue(101)
    q.printQueue()
    q.enqueue(102)
    q.printQueue()
    q.enqueue(103)
    q.printQueue()

if __name__ == '__main__':
    main()