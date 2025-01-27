import databaes
mycursor = databaes.mydb.cursor()
#--------------------------------------------------------------------------#
def selectdb(table):
    sql = f"select * from {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show

print(selectdb('products'))
#--------------------------------------------------------------------------#
def insert_product(product_id,product_name,description,price,stock):
    sql = "insert into products values (%s ,%s ,%s ,%s ,%s)"
    val_sql = (product_id,product_name,description,price,stock)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(insert_product(2,"7000jade","forEducation",400,999))
#--------------------------------------------------------------------------#
def insert_user(user_id,username,password,email,user_role):
    sql = "insert into products values (%s ,%s ,%s ,%s ,%s)"
    val_sql = (user_id,username,password,email,user_role)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(insert_user())
#--------------------------------------------------------------------------#
def insert_order(order_id,user_id,order_date,total_amount,status,product_id):
    sql = "insert into products values (%s ,%s ,%s ,%s ,%s ,%s)"
    val_sql = (order_id,user_id,order_date,total_amount,status,product_id)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(insert_order())
#--------------------------------------------------------------------------#
def insert_category(category_id,category_name):
    sql = "insert into products values (%s ,%s)"
    val_sql = (category_id,category_name)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(insert_category())
#--------------------------------------------------------------------------#
def delete(table,where,id):
    sql=f"delete from {table} where {where} = %s "
    val_sql = (id,)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(delete("users","user_id",2))
#--------------------------------------------------------------------------#
def editdb(table,column,val,idname,id):
    sql=f"update {table} set {column} = %s where {idname} = %s "
    val_sql = (val,id,)
    mycursor.execute(sql,val_sql)
    databaes.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print(editdb("users","username","ena","user_id",1))