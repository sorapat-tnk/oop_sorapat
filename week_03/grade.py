print("โปรเเกรมตัดเกรด")
grade = int(input("ใส่คะแนนของคุณ : "))
if grade > 100:
    print("เก่งเกินคน")
elif grade >= 80 :
    print("เกรด 4 ")
elif grade >= 70 :
    print("เกรด 3 ")
elif grade >= 60 :
    print("เกรด 2 ")
elif grade >= 50 :
    print("เกรด 1 ")
elif grade < 50 :
    print("เกรด 0 ")
    print("คุณต้องการขอเเก้0ไหม")
    fixzero = int(input("ถ้าต้องการตอบ 1 ถ้าไม่ต้องการตอบ 2 \n"))
    if fixzero == 1 :
        cal = 50 - grade
        print("คุณต้องการอีก : "+str(cal)+"คะแนน")
    elif fixzero == 2:
        print("คุณก็สอบตก")
    else:
        print("กรุณาทำราการใหม่อีกครั้ง")
else:
    print("กรุณาทำราการใหม่อีกครั้ง")
