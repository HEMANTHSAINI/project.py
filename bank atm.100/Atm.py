class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def checkBalance(self):
        print("you'r balance is 50,000")
    def withdraw(self,amount):
        newamount = 50000-amount
        print('you have withdrawn amount'+str(amount)+' your remaining amount is '+str(newamount))
def main ():
    cardnumber = input('insert your card number')
    pinnumber = input('insert your pin number')
    newuser = Atm(cardnumber,pinnumber)
    print('choose your activity')
    print('1:balance enquiry 2:Withdrawel')
    activity = int(input("enter your activity number"))
    if(activity == 1):
        newuser.checkBalance()
    elif(activity == 2):
        amount= int(input("enter your amount"))
        newuser.withdraw(amount)   
    else:
        print("enter a vaild number") 
main()        