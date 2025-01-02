class Markerpen:
    def __init__(self,color,price,brand):
        print("object is created....")
        self.color=color
        self.price=price
        self.brand=brand
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
m2=Markerpen("black",20,"apsara")
res4=m2.show_color()
print(res4)
res5=m2.show_price()
print(res5)
res6=m2.show_brand()
print(res6)