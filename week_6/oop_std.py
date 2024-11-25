import random
class student:
    def __init__(self,name_lastname,nickname,score):
        self.name = name_lastname
        self.nickname = nickname
        self.score = score
    def test(self):
        self.score += random.randint(1,10)
student1 = student("Akiyama Mizuki","Mizuki",0)
student2 = student("Shinonome Ena","Ena",0)
student3 = student("Hatsune Miku","Miku",0)
student4 = student("Asahina Mafuyu","Mafuyu",0)
student5 = student("Yoisaki Kanade","Kanade",0)

student1.test()
student2.test()
student3.test()
student4.test()
student5.test()
print(student1.name,student1.nickname,student1.score)
print(student2.name,student2.nickname,student2.score)
print(student3.name,student3.nickname,student3.score)
print(student4.name,student4.nickname,student4.score)
print(student5.name,student5.nickname,student5.score)

for student in [student1, student2, student3, student4, student5]:
    if student.score >= 5:
        print(f"{student.name}{student.nickname}สอบได้คะแนน {student.score} สอบผ่าน ")
    else:
        print(f"{student.name}{student.nickname}สอบได้คะแนน {student.score} สอบไม่ผ่าน ")