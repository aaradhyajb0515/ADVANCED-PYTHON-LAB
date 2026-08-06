class creditcard:
    def pay(self,amount):
        print(f"Paid {amount}rupee using credit card")
class Upi:
    def pay(self,amount):
        print(f"Paid {amount}rupee using upi")
class cash:
    def pay(self,amount):
        print(f"Paid {amount}rupee using cash")
class moneytransfer:
    def pay(self,amount):
        print(f"Paid {amount}rupee  using money tranfer")

class Paymentt:
    def __init__(self,method):
        self.method=method
    def make_payment(self,amount):
        self.method.pay(amount)


choice=input("Enter payment method(creditcard,upi,cash,moneytranfer=")
amount=int(input("Enter the amount:"))

if choice.lower()=="creditcard":
    method=creditcard()
elif choice.lower()=="upi":
    method=Upi()
elif choice.lower()=="cash":
    method=cash()
elif choice.lower()=="moneytransfer":
    method=moneytransfer()
else:
    print("Invalid input")


payment=Paymentt(method)
payment.make_payment(amount)
