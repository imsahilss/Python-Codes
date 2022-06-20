class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

x = Node(10)
y = Node(20)
z = Node(50)
print(x)
print(y)
print(z)
x.next=y

print(x.next)
print(y.next)
print(y.data)
print(y.next)
print(x.data)
print(x.next.data)
print(y.next.data)
