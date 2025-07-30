capacity = 500
class Vehicle:
    def __init__(self,fare):
        self.fare = fare
class Bus(Vehicle):
    def cost(self):
        print("we will tell the fARE soon")
a = Bus(10000)
print("Fare is ",10000+500)