students = [
    {"name": "윤인성", "korean": 87, "english": 87, "math": 87, "science": 87 },
    {"name": "박진주", "korean": 52, "english": 56, "math": 57, "science": 45 },
    {"name": "윤성환", "korean": 74, "english": 97, "math": 25, "science": 46 },
    {"name": "장만옥", "korean": 51, "english": 64, "math": 66, "science": 87 },
    {"name": "월인환", "korean": 23, "english": 45, "math": 77, "science": 83 },
    {"name": "김장오", "korean": 83, "english": 35, "math": 75, "science": 72 }
]
print("이름", "총점", "평균", sep="\t")
for i in students:
    score_sum = i["korean"] + i["math"] +\
    i["english"] + i["science"]
    score_average = int(score_sum/len(students))
    print(i["name"], score_sum, score_average, sep = "\t")

def create_student(name, korean, english, math, science):
    return {
        "name": name,
        "korean": korean,
        "english": english,
        "math": math,
        "science": science
    }

students = [
    create_student("윤인성", 80, 83, 32, 26),
    create_student("오병옥", 80, 83, 69, 26),
    create_student("김일성", 80, 83, 32, 90),
    create_student("문재인", 80, 83, 32, 26),
    create_student("양만춘", 80, 83, 32, 26),
    create_student("고수", 80, 83, 32, 26),
]

print("이름", "총점", "평균", sep="\t")
for i in students:
    score_sum = i["korean"] + i["math"] +\
    i["english"] + i["science"]
    score_average = int(score_sum/len(students))
    print(i["name"], score_sum, score_average, sep = "\t")

def student_get_sum(i):
    return i["korean"] + i["math"] +\
    i["english"] + i["science"]

def student_get_average(i):
    return student_get_sum(i)/4

def student_to_string(i):
    return "{}\t{}\t{}".format(
        i["name"],
        student_get_sum(i),
        student_get_average(i))

for k in students:
    print(student_to_string(k))

class Student:
    def __init__(self, name, korean, english, math, science):
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

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(), \
            self.get_average())


students = [
    Student("윤인성", 80, 83, 32, 26),
    Student("오병옥", 80, 83, 69, 26),
    Student("김일성", 80, 83, 32, 90),
    Student("문재인", 80, 83, 32, 26),
    Student("양만춘", 80, 83, 32, 26),
    Student("조세호", 80, 83, 32, 26),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())