a = int(input("ต้องการป้อนตัวเลขทั้งหมดกี่ตัว :"))
number = []
for i in range(a):
    number.append(int(input("กรุณาใส่ตัวเลขของคุณ :")))
s = sum(number)
avg = s/len(number)
print("หาค่าเฉลี่ยของ"+str(number)+"="+str(avg))