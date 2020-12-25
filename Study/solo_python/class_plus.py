class Student:
    def __init__(self):
        pass

student = Student()
print(isinstance(student, Student))

class Student:
    def study(self):
        print("공부를 합니다.")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for p in classroom:
    if isinstance(p, Student):
        p.study()
    elif isinstance(p, Teacher):
        p.teach()

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

    def get_sum(self):
        return self.korean + self.english +\
            self.math + self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def __str__(self, student):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(student),
            self.get_average(student))

    def __eq__(self, value):
        return self.get_average() == value
    def __ne__(self, value):
        return self.get_average() != value
    def __gt__(self, value):
        return self.get_average() > value
    def __ge__(self, value):
        return self.get_average() >= value
    def __lt__(self, value):
        return self.get_average() < value
    def __le__(self, value):
        return self.get_average() <= value

students = [
    Student("윤인성", 80, 83, 32, 26),
    Student("오병옥", 80, 83, 69, 26),
    Student("김일성", 80, 83, 32, 90),
    Student("문재인", 80, 83, 32, 26),
    Student("양만춘", 80, 83, 32, 26),
    Student("조세호", 80, 83, 32, 26),
]

test = Student("A", 90, 90, 90, 90)
student_a = Student("윤인성", 80, 83, 32, 26),
student_b = Student("오병옥", 80, 83, 69, 26),

print("student_a == student_b", test == 90)
print("student_a == student_b", test <= 90)
print("student_a == student_b", test >= 90)
print("student_a == student_b", test < 90)
print("student_a == student_b", test > 90)
print("student_a == student_b", test != 90)




