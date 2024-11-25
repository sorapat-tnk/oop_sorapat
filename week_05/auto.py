a = int(input("ป้อนจำนวนคน :"))
n = {}
for i in range(a):
    print(f"กรอกคนที่{i+1}")
    name = input("กรุณากรอกชื่อ ")
    n["nickname"] = name
    study = input("กรุณากรอกเลขที่ ")
    n["study"] = study
    hobby = input("กรุณากรอกงานอดิเรก")
    n["hobby"] = hobby
    color = input("กรุณากรอกสีที่ชอบ")
    n["color"] = color
    print(n)

