class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100 :
            self.__balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
    def check(self):
        return self.balance

id1 = Bank(1,"mizuki",5000)
id1.withdraw(1000)
id1.deposit(500)
print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
