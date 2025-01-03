class Watch:
    @staticmethod
    def showtime():
        print("watch shows time....")
    @classmethod
    def showbrand(self):
        print("watch brand is rolex........!")
    def __init__(self,color):
        print("object is created...")
        self.color=color
    def get_color(self):
        print(self.color)
w1=Watch('silver')
Watch.showtime()
Watch.showbrand()
w1.get_color()
w1.showtime()
