class Student:
    pass

# student1 = Student()
# #Object . attribute
# student1.name = "Harry"
# # student2 = student()
#
# student1.marks = 85
#
#
# print(student1.name, student1.marks)

#Self is an argument representing the object calling it as an arguement
#Self - what ever object calling it
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
#Ceated and object student1
student1 = Student()
#Object . attribute    We added two attributes name and marks to the object
student1.name = "Harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)