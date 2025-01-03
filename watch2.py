class Student:
    @staticmethod
    def collegeName():
        print("abc college.......!")
    @classmethod
    def writeExams(self):
        print("enjoy exams....!")
    #accessor method
    def show_Name(self):
        return self.studentName
    #mutator methods
    def set_name(self):
        self.studentName="scott"
    def __init__(self,studentName,ID,Email):
        print('object is created..!')
        self.studentName= studentName
        self.ID=ID
        self.Email=Email
Student.collegeName()
Student.writeExams()
std1=Student("ki",234,'ki@gmail.com')
print(std1.show_Name())

