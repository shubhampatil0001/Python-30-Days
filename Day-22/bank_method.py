class BankAccount:
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
       self.balance = self.balance + amount 
        
    def show_balance(self):
        print("Balance :",self.balance)
         
account = BankAccount("Shubham",10000)
account.deposit(5000)
account.show_balance()
