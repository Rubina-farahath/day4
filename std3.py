class Student:
    def __init__(self,name,age):
        print("object is created:")
        self.name=name
        self.age=age
std1=Student("Krishna",20)
print("student name is:",std1.name)
print("student age is :",std1.age)