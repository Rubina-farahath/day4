class engineer:
    def work(self):
        print("engineering is working...")
class software_eng(engineer):
    def work(self):
        print("software engineering.....")
class mechanical_eng(engineer):
    def work(self):
        print("mech engineering.......")
E1=engineer()
E1.work()
E2=software_eng()
E2.work()
E3=mechanical_eng()
E3.work()