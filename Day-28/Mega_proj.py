class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    school = "ABC College"

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("School:", self.school)

    @classmethod
    def show_school(cls):
        print("School:", cls.school)

    @staticmethod
    def check_result(marks):
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Shubham", 18, 85)

student1.show_info()

print("Result:", Student.check_result(student1.marks))

Student.show_school()
