class Student:
    def __init__(self, f_name, l_name, Age, Roll_no):
        self.first_name = f_name
        self.last_name = l_name
        self.Age = Age
        self.Roll_no = Roll_no

    def study(self):
        print('Studying')

    def complete_assignment(self):
        print('Done')

    def bunk_class(self):
        print('Bunking')

    def coding(self):
        print('Yes')

def main():
    s1 = Student('Sahil', 'Sharma', 21, 60)
    print(s1.first_name)
    print(s1.last_name)
    print(s1.Age)
    print(s1.Roll_no)

    s1.study()
    s1.complete_assignment()
    s1.coding()
    print("\n")

    s2 = Student('Nitin', 'Suiwal', 21, 66)
    print(s2.first_name)
    print(s2.last_name)
    print(s2.Age)
    print(s2.Roll_no)
    print(setattr(s2, 'Roll_no', 29))
    getattr(s2, 'Roll_no')


    s2.study()
    s2.complete_assignment()
    s2.coding()
    s2.bunk_class()
    print("-----------------------")

    print(s1.__dict__)
    print(s1.__module__)
    print(s1.__name__)
    print(s1.__bases__)
    print(s1.__doc__)



if __name__ == '__main__':
    main()