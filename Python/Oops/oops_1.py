class Bank_Account:
    def __init__(self):
        self.Name=""
        self.Amount=""
        self.Address=""
        self.AccountNo=""
        
        
        
    def CreateAccount(self):
        self.Name=input('Enter Your name')
        self.Amount=int(input('Enter Your amount'))
        self.Address=input('Enter Your Address')
        self.AccountNo=int(input('Enter Your Account no'))
        
        
    def DisplayInformation(self):
        print('----your account details' )
        
        print('your name: ',self.Name)
        print('your amount: ', self.Amount)
        print('your Address: ', self.Address)
        print('your Account: ', self.AccountNo)
        
        
def main():
    User_1=Bank_Account()
    print('Creating First Account: ')
    User_1.CreateAccount()
    User_1.DisplayInformation()
    
    
if __name__=="__main__":
    main()