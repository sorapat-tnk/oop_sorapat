class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name = ชื่อ
        self.age = อายุ
        self.gender = เพศ
        self.coler = สี
    def old(self):
        self.age += 1
cat1 = Cat(ชื่อ="ena",อายุ=4,เพศ="ตัวเมีย",สี="น้ำตาล")
cat2 = Cat("mizuki",3,"ไม่ระบุ","สีชมพู")
cat1.name = "loveEna" #เเก้ค่า
cat1.old()
print(cat1.name)
print(cat2.name)