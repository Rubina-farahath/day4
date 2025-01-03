class Vehicle:
    def __init__(self):
        print("hey! I'm the vehicle class constructor........")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("hey! I'm the bike class constructor........")
class SuperBike(Bike):
    def __init__(self):
        print("hey..! I'm the super bike class constructor...")
S1=SuperBike()
    
        