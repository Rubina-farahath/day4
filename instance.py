class Mobile:
    def __init__(self):
        print("object is created....!")
        self.price=15000
    def show_price(self,price):
        print(self.price)
samsung=Mobile()
samsung.show_price(1000)
#instance method with parameters