if __name__ == '__main__':
    def find_second_lowest_grade_students():
        num_students = int(input())
        students = []
    for _ in range(num_students):
        name = input()
        grade = float(input())
        students.append((name,grade))
    unique_grades = sorted((students[1]for student in students))
    second_lowest_grade = unique_grades[1]
    second_lowest_students = [student[0] for student in students if student[1]== second_lowest_grade]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)
find_second_lowest_grade_students()