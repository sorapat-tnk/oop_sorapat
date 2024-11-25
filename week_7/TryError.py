try:
    cost = int(input("กรุณาใส่ยอดของลูกค้า : "))
    if cost == 0:
        raise ZeroDivisionError
    elif cost < 0:
        raise Exception
    
    if cost >= 5000:
        print(f"{cost*0.2}")
    elif 2000 <= cost < 4999:
        print(f"{cost*0.1}")
    else:
        print("คุณไม่ได้รับส่วนลดใดๆ")
except ValueError:
    print("ห้ามใส่ตัวอักษร")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")