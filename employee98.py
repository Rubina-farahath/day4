class employee:
    def __init__(self,name,ID,designation,salary,location,specialallowances):
        self.name=name
        self.ID=ID
        self.designation=designation
        self.salary=salary
        self.location=location
        self.specialallowances=specialallowances
def display_details(self):
    print("details of the employee:")
    print("employee name:",self.name)
    print("emp id is:",self.ID)
    print("emp designation is:",self.designation)
    print("emp salary:",self.salary)
    print("emp location:",self.location)
    print("emp allownances:",self.specialallowances)
emp2=employee("scott","emp2002","developer",24000,"mumbai","na allowances")
display_details(emp2)