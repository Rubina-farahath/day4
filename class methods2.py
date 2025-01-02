class Mobiles:
    @classmethod                                        #decorator
    def show_model(cls):                                 #class method
        print("realme X")
realme=Mobiles()
Mobiles.show_model()                                   #intializing class method
print("--------------------------")
class mobile:
    fp='yes'
    @classmethod
    def show_model(cls):
        print("finger print scanner:",cls.fp)
realme=mobile()
mobile.show_model()