class animal:
    def init(self,name,age,color):
        self.name  = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี{self.color}"
#animal1 = animal("ปีเตอร์",10,"ดำ")
#print(f"สัตว์ตัวหนึ่งมี{animal1.showinfo()}")
class Dog(animal):
    def init(self, name, age, color,race):
        super().init(name, age, color)
        self.race = race
    def showdog(self):
        return f"หมาพันธุ์ {self.race} มี {super().showinfo()}"
dog1 = Dog("ปีเตอร์",5,"ดำ","หลังอาน")
print(dog1.showdog())
