class duck:
    def walk(self):
        print("thapak thapak thapak")
class horse:
    def walk(self):
        print("thadak thadak thadak")
def myfunction(obj):
    obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)