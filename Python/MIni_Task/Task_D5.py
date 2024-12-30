# class Menu:
    
#     def __init__(self):
#         self.Menu_Card=['Dosa','Idly','Biriyani']
        
        
#     def show(self):
#        print(self.Menu_Card) 
       
       
#     def add(self):                  
#         dish=input('Which dish you Want to Add: ')
#         self.Menu_Card.append(dish)
#         print(self.Menu_Card)
        
        
#     def update(self):
#         dish1=input('Which dish you Want to update: ')
#         dish2=input('Which dish you Want to replace: ')
#         for i in range(len(self.Menu_Card)):
#          if self.Menu_Card[i] == dish1:
#             self.Menu_Card[i] = dish2
#         print(self.Menu_Card)
        
        
#     def remove(self):
#         dish=input('Which dish you Want to Remove')
#         self.Menu_Card.remove(dish)
#         print(self.Menu_Card )
       
       
# def main():
#     card=Menu()
#     in_put=int(input('Print 1 for display \n Print 2 for add \n Print 3 for update \n Print 4 for delete \n '))

    
#     if(in_put==1):
#        card.show()
    
#     elif(in_put==2):
#         card.add()
       
#     elif(in_put==3):
#         card.update()
       
#     elif(in_put==4):
#         card.remove()
      
        
#     else:
#         print('You Selected Invalid Term')
    
    
# if __name__=='__main__':
#     main()

# ========================================================================================================


# class Bank_Account:
    
#     BankName= "ICICI Bank" 
#     ROI=5
#     def __init__(self):
#         self.Name="jai"  
#         self.Amount=500
#         self.Address="chennai"
#         self.AccountNo=234751554
        
        
#     def Withdraw(self):
#         amount=int(input('How Much you want to Withdraw: '))
#         if(amount<self.Amount):
#          print('your withdrawal money is :',amount)
#         else:
#             print('not sufficiant Balance')
            
#     def Balance(self):
#         print('Your Curreent Balance is',self.Amount)
        
#     def Deposite(self):
#         amount=int(input('How Much you want to deposite: '))
#         self.Amount=amount+self.Amount
#         print('your Deposite money is :',amount)
        
        
        
        
# def main():
    
#     print('Bank Name: ',Bank_Account.BankName)
#     print('Rate Of Interest: ',Bank_Account.ROI)
#     Bank=Bank_Account()
#     in_put=int(input('press 1 for Balance \n Press 2 for Check Withdraw \n Press 3 for Deposite  '))

    
#     if(in_put==1):
#        Bank.Balance()
    
#     elif(in_put==2):
#         Bank.Withdraw()
       
#     elif(in_put==3):
#         Bank.Deposite()
       
        
#     else:
#         print('You Selected Invalid Term')
    
    
    
# if __name__=="__main__":
#     main()


# ============================================================================================

#Calculator Using Dictionary



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def floor_divide(num1, num2):
    return num1 // num2

def exponentiate(num1, num2):
    return num1 ** num2

def calculator():
   
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '%': floor_divide,
        '^': exponentiate
    }

    print("Simple Calculator")
    print("Available operations: +, -, *, /, //, **")

    # Get user input for the operation
    operation = input("Enter operation (+, -, *, /, //, **): ")

    if operation not in operations:
        print("Invalid operation!")
        
    else:

    
     num1 = float(input("Enter first number: "))
     num2 = float(input("Enter second number: "))
    
    # Perform the operation using the dictionary
    result = operations[operation](num1, num2)

    # Output the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Run the calculator
calculator()
