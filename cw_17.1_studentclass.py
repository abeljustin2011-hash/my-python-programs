class Student:
    name = ""
    grade = 0
    marks = 0
    def __init__(self, name, grade, marks):
        self.name = name
        self.grade = grade
        self.marks = marks
    def display_info(self):
        print("Student name:", self.name)
        print("Grade:", self.grade)
        print("Marks:", self.marks)

Alex = Student("Alex", 10, 88)
Maya = Student("Maya", 11, 92)

Alex.display_info()
Maya.display_info()