#Payment system using abstract class and method

from abc import ABC, abstractmethod

class payment(ABC):
    
    @abstractmethod
    def pay(self,Amount):
        pass
  
print("PAYMENT SYSTEM BANKING")  
class Upipayment(payment):
    def pay(self,Amount):
        print("Payment of",Amount,"is done through UPI")
        
class Cardpayment(payment):
    def pay(self,Amount):
        print("Payment of",Amount,"is done through Card")
        
upi = Upipayment()
card = Cardpayment()

upi.pay(10000)
card.pay(5000)                    
