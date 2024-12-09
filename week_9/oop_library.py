class library:
    def __init__(self):
        self.booker = []
    def add_book(self):
        while True:
            p = input("คุณต้องการใส่หนังสือไหม(ตอบ y/n) : ")
            if p == "n":
                break
            book = {}
            book["ชื่อหนังสือ "] = input("ใส่ชื่อหนังสือของคุณ : ")
            book["ชื่อผู้เเต่งหนังสือ "] = input("ใส่ชื่อผู้แต่งหนังสือของคุณ : ")
            book["จำนวนหน้าหนังสือ "] = input("ใส่จำนวนหน้าหนังสือของคุณ : ")
            book["ราคาหนังสือ"] = input("ใส่ราคาหนังสือของคุณ : ")
            self.booker.append(book)
    def show_book(self):
        print("รายชื่อหนังสือในห้องสมุดแห่งนี้")
        for library in self.booker:
            print(library)
    def find_book(self):
        book = input("ใส่ชื่อที่ต้องการหา : ")
        for library in self.booker:
            if book == library["ชื่อหนังสือ"]:
                print(library)
lib = library()
lib.add_book()
lib.show_book()
lib.find_book()


