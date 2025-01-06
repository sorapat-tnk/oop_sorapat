class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__price = []
        self.__stock = stock
    def add(self):
        self.__stock += instock
    def dis(self):
        self.__stock -= instock
    def edit(self):
        inprice = int(input('ใส่ราคาสินค้า '))
        self.__price.append(inprice)
    def detail(self):
        return (f'(มีราคา {self.__price} บาท จำนวน {self.__stock} ชิ้น)')

pro1 = Product('Miku', 0)
while True:
    choice = input('กรุณาเลือกฟังก์ชัน: ต้องการเพิ่มพิมพ์ว่า add ถ้าจะลดจำนวนให้พิมพ์ dis ถ้าจะเช็ครายการสินค้าให้พิมพ์ check ถ้าต้องการแก้ไขราคาพิมพ์ว่า edit ออกพิมพ์ว่า exit: ')
    if choice == 'add':
        instock = int(input('ใส่จำนวนที่ต้องการเพิ่ม: '))
        pro1.add()
    elif choice == 'dis':
        instock = int(input('ใส่จำนวนที่ต้องการลด: '))
        pro1.dis()
    elif choice == 'check':
        print(f'รายการสินค้า {pro1.name} มีรายละเอียดดังนี้ {pro1.detail()}')
    elif choice == 'edit':
        pro1.edit()
    elif choice == 'exit':
        break
pro1.edit()
print(f'รายการสินค้า {pro1.name} มีรายละเอียดดังนี้ {pro1.detail()}')