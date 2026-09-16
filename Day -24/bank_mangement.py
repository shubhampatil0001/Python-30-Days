# Bank Management System

class BankAccount:
    
    bank_name = "SBI BANK"
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def show_balance(self):
        print("BALANCE :",self.balance)
    
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Amonut Deposited:", amount)
    
    def withdraw(self,amount):
        if amount <= self.balance :
            self.balance = self.balance - amount
            print("WITHDRAW AMOUNT :",amount)
        else:
            print("INSUFFICIENT BALANCE ")
            
    @classmethod
    def show_bank_name(cls):
       print("BANK NAME :",cls.bank_name)               
        
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

BankAccount.show_bank_name()            


Account1 = BankAccount("Shubham",10000)
Account1.show_balance()
Account1.deposit(1000)
Account1.withdraw(2000)
Account1.show_balance()
print(BankAccount.is_valid_amount(200)
