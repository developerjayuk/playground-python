class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student = Student("Alice", 20)
student.add_grade(85)
student.add_grade(90)
student.display_info()
print(f"Average Grade: {student.calculate_average()}")
