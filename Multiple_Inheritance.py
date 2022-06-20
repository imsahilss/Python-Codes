class Car:
    def __init__(self, gears, seats, maxspeed):
        self.gear = gears
        self.seat = seats
        self.maxspeed = maxspeed

    def speedup(self):
        print("Speed is Increasing")

    def apply_break(self):
        print("Speed is Decreasing")

    def movement(self):
        print("Car moves back and forth")

class Hyundai:
    def __init__(self):
        self.brandName = "Hyundai"


class Harrier(Car):
    def __init__(self, mileage, gears, seats, maxspeed):
        self.mileage = mileage
        super().__init__(gears, seats, maxspeed)
    def race_mode(self):
        print("Race mode is on")


class Verna(Car, Hyundai):
    def __init__(self, gears, seats, maxSpeed):
        Car.__init__(self, gears, seats, maxSpeed)
        Hyundai.__init__(self)

class PAL_V(Car):
    def movement(self):
        print("Car moves back, forth, up and down") #Method Overriding





# c1 = Car() #c1 = Car(4, 12, 129)
h1 = Harrier(15, 5, 4, 240)
v1 = Verna(5, 4, 180)
p1 = PAL_V(5, 2, 300)
print(h1.mileage)

print(h1.gear)
print(h1.seat)
print(h1.maxspeed)
h1.speedup()
h1.apply_break()
h1.race_mode()
p1.movement()
h1.movement()
print('------------------------------')
print(v1.brandName)
print(v1.gear)
