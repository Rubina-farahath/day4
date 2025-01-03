class engineer:
    def __init__(self):
        print("i'm the engineer class constructor")
E1=engineer()
print("---------------------------------------------")
class softwareengineer(engineer):
    def __init__(self):
        super().__init__()
        print("I'm the software emgineer class constructor")
se1=softwareengineer()
print("--------------------------------------")
class civilengineer(engineer):
    def __init__(self):
        super().__init__()
        print("I 'm the civil engineering class constructor")
c1=civilengineer()
print("-------------------------------------------------")
class mechanicaleng(engineer):
    def __init__(self):
        super().__init__()
        print("i ;m the mech enginering.....")
e1=mechanicaleng()