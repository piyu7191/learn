class Vehicle:
    def __init__(self):
        self.fare = None
    
    def Fare(self, fare):
        self.fare = fare

bus, car, train, truck, ship = Vehicle(), Vehicle(), Vehicle(), Vehicle(), Vehicle()
vehicles = [bus, car, train, truck, ship]
bus.Fare(15)
car.Fare(5)
train.Fare(60)
truck.Fare(50)
ship.Fare(70)

totalfare = sum([i.fare for i in vehicles])
print(totalfare)