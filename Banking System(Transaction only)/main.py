class IciciBank:
    balance=10000
    def __init__(self):
        print("your account is created")
    def withdrawl(self,amountWithdrawl):
        if (amountWithdrawl<self.balance):
            self.balance=self.balance-amountWithdrawl
            print("your updated balance is",self.balance)
        else: print("Insufficient Fund")
    def deposit(self,amountDeposit):
        self.balance=self.balance+amountDeposit
        print("your updated balance is", self.balance)

obj=IciciBank()
accNo= int(input("enter your account number: "))
accName=input("enter your account name: ")
print("press 1 for withdrawal")
print("press 2 for deposit")
print("press 0 to exit")
while(True):
    choice=int(input("please enter the choice: 1/2/3 :\n"))
    if (choice==1):
        amountWithdrawl=float(input("please enter the withdrawl amount: "))
        obj.withdrawl(amountWithdrawl)
    elif (choice==2):
        amountDeposit=float(input("please enter the deposit amount: "))
        obj.deposit(amountDeposit)
    elif (choice==0):
        break
    else:
        print("invalid code")
    


