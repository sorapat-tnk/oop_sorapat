def mizuki(num1,num2):
    c = []
    for i in range(num1,num2+1):
        if i%3 != 0 :
            c.append(i)
    return c