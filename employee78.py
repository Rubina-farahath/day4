class employee:
    def __init__(self,name,ID,designation,salary,location,specialallowances):
        self.name=name
        self.ID=ID
        self.designation=designation
        self.salary=salary
        self.location=location
        self.specialallowances=specialallowances
emp=employee("sitha",403,"HR",7000,"Hyd",1000)
print("employee name:",emp.name)
print("emp id is:",emp.designation)
print("emp salary:",emp.ID)
print("emp location:",emp.location)
print("emp allownances:",emp.specialallowances)
print("--------------------------")
class employee:
    def __init__(self,name,ID,designation,salary,location,specialallowances):
        self.name=name
        self.ID=ID
        self.designation=designation
        self.salary=salary
        self.location=location
        self.specialallowances=specialallowances
        print("employee name:",emp.name)
        print("emp id is:",emp.ID)
        print("emp designation is:",emp.designation)
        print("emp salary:",emp.salary)
        print("emp location:",emp.location)
        print("emp allownances:",emp.specialallowances)
emp2=employee("hello",567,"developer",25000,"banglore",'travel and food')