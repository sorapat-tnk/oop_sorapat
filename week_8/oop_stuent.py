class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grader = {}
    def score(self):
        choice = input("กรุณาเลือกวิชาที่จะกรอกคะแนน : \n มีวิชาดังนี้ M T E S ")
        score = int(input("ใส่คะแนน :"))
        grade = self.grade(score)
        if choice == "M":
            self.grader["Math"] = grade
        elif choice == "T":
            self.grader["thai"] = grade
        elif choice == "E":
            self.grader["English"] = grade
        elif choice == "S":
            self.grader["Science"] = grade
    def grade(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
stu1 = Student ("mizuki",1,15)
stu2 = Student ("sop",2,15)
stu1.score()
print(stu1.grader)