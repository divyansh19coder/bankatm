class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("ruppes = 100")
        print("dollars = 200")
        print("yen = 300")

    def withdrawl1(self,ruppes):
        new_amount = 100 - ruppes
        print("You have withdrawn amount "+str(ruppes) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,dollars):
        new_amount = 200 - dollars
        print("You have withdrawn amount "+str(dollars) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,yen):
        new_amount = 300 - yen 
        print("You have withdrawn amount "+str(yen) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to Gringotts Bank! The wizards and witchs bank")
    Account = input("Please enter your account image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add ruppes")
        print("2. Add dollars")
        print("3. Add yens")
        choose = int(input("1. Add ruppes  2. Add dollars 3. Add yen: "))
        if (choose == 1):
           ruppes = int(input("Enter the amount:- "))
           new_user.withdrawl1(ruppes)
        if (choose == 2):
           dollars = int(input("Enter the amount:- "))
           new_user.withdrawl2(dollars)    
        if (choose == 3):
           yen = int(input("Enter the amount:- "))
           new_user.withdrawl3(yen)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()