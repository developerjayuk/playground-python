# Bad example of mutable default parameters


class Student_bad:
    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)


dave = Student_bad("Dave")
dave.add_course("Math")

paul = Student_bad("Paul")

print(dave.courses)  # Output: ['Math']
print(
    paul.courses
)  # Output: ['Math'] - This is unexpected behavior due to mutable default parameter

# Good example of mutable default parameters


class Student_good:
    def __init__(self, name, courses=None):
        self.name = name
        self.courses = courses if courses is not None else []

    def add_course(self, course):
        self.courses.append(course)


sara = Student_good("Sara")
sara.add_course("Math")

jane = Student_good("Jane")

print(sara.courses)  # Output: ['Math']
print(jane.courses)  # Output: [] - This is the expected behavior
