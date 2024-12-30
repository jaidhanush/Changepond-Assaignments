

class Bank_Account:
    
    BankName= "ICICI Bank" #class variable
    ROI=5
    def __init__(self):
        self.Name=""   #Instance Variable
        self.Amount=""
        self.Address=""
        self.AccountNo=""
        
        
        
    def CreateAccount(self):  #Instance Method
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
        
    @classmethod 
    def DisplayBankInfo(cls):
        print('----------Display Bank Info---------')
        print('Bank Name: ',cls.BankName)
        print('ROI on FD: ',cls.ROI)
     
    
    @staticmethod
    def DisplayKYCInfo():
        print('Submit Following Documents')
        print('1.Aadhar Card')
        print('2.passport size photo')
        
def main():
    Bank_Account.DisplayKYCInfo()
    Bank_Account.DisplayBankInfo()
    print('Bank Name: ',Bank_Account.BankName)
    print('Rate Of Interest: ',Bank_Account.ROI)
    User_1=Bank_Account()
    print('Creating First Account: ')
    User_1.CreateAccount()
    User_1.DisplayInformation()
    
    
if __name__=="__main__":
    main()
    
    
 #Static Method   
class student:
     @staticmethod
     def Rollnumber(y):
         print('Roll Number ',y)
         
         
#call
student.Rollnumber(101)