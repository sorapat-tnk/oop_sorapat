class animal:
    def __init__(self,name,age,color):
        self.name  = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี{self.color}"
#animal1 = animal("ปีเตอร์",10,"ดำ")
#print(f"สัตว์ตัวหนึ่งมี{animal1.showinfo()}")
class Dog(animal):
    def speak(self):
        return "โฮ่ง"
dog1 =Dog("ปีเตอร์",10,"ดำ")
print(f"หมาชื่อ {dog1.name} ร้อง {dog1.speak()}")
print(f"สัตว์ตัวหนึ่งมี{dog1.showinfo()}")