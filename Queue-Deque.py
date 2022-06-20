class Deque():
    def __init__(self):
        self._dq = []

    def isEmpty(self):
        return self._dq==[]

    def insertRear(self,data):
        self._dq.append(data)

    def insertFront(self,data):
        self._dq.insert(0,data)

    def deleteRear(self):
        self._dq.pop()

    def deleteFront(self):
        self._dq.pop(0)

    def size(self):
        return len(self._dq)

    def frontele(self):
        return self._dq[0]

    def rearele(self):
        return self._dq[self.size()-1]

    def printDeque(self):
        for ele in self._dq:
            print(ele, end=' ')
        print()

def main():
    deque = Deque()
    deque.insertFront(5)
    deque.printDeque()
    deque.insertFront(10)
    deque.printDeque()
    deque.insertRear(1)
    deque.printDeque()
    deque.insertRear(12)
    deque.printDeque()

    print('-----------------')

    print(deque.frontele())
    print(deque.rearele())
    print(deque.size())

    print('-----------------')

    deque.deleteRear()
    deque.printDeque()
    deque.deleteFront()
    deque.printDeque()

    print('-----------------')

    print(deque.frontele())
    print(deque.rearele())
    print(deque.size())


if __name__ == '__main__':
    main()