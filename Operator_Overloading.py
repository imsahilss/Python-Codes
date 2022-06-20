class Student:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        ans1 = self.x + other.x
        ans2 = self.y + other.y
        return '{} {}'.format(ans1, ans2)

    def __lt__(self, other):
        ans1 = self.x + self.y
        ans2 = self.x + self.y
        if(ans1<ans2):
            return True
        else:
            return False
S1 = Student(10, 20)
S2 = Student(5, 6)
S3 = S1 + S2
print(S3)
if S1 < S2:
    print("S1 is smaller")
else:
    print("S2 is smaller")

