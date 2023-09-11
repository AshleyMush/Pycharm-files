class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100

    def get_grade(self):
        return  self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


    def get_average_grade(self):
        pass

s1 = Student("Ash", 25, 99)
s2 = Student("Anna", 37 , 100)
s3 = Student("Bill", 29, 70)

course = Course("Science", 2)
course.add_student(s1)

print(s1.name)