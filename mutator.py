class Markerpen:
    def __init__(self,color,price,brand):
        print("object is created....")
        self.color=color
        self.price=price
        self.brand=brand
    #mutator methods
    def set_color(self):
        self.color='red'
    def set_price(self):
        self.price=30
    def set_brand(self):
        self.brand='doms'

    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def show_brand(self):
        return self.brand
m1=Markerpen("pink",30,"camelin")
res1=m1.show_color()
print(res1)
res2=m1.show_price()
print(res2)
res3=m1.show_brand()
print(res3)
print("-------------")
m1.set_color()
m1.set_price()
m1.set_brand()
res1=m1.show_color()
print(res1)
res2=m1.show_price()
print(res2)
res3=m1.show_brand()
print(res3)
