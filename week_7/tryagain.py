ena = 0
try:
    while True:
        mi = input("ใส่ราคาสินค้า :")
        if mi == "exit":
            break
        mi = int(mi)
        if mi == 0:
            raise ZeroDivisionError
        elif mi < 0:
            raise Exception
        ena += mi
    print(f"ราคาสินค้าทั้งหมด{ena}")
except ValueError:
    print("กรุณาใส่ตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ราคาสินค้าต้องมากกว่า 0")
except:
    print("ราคาสินค้าไม่มีติดลบ")