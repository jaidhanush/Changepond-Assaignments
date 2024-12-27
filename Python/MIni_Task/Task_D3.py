

#Task 1
# Menu_Card=['Dosa','Idly','Biriyani']
# print(Menu_Card)  

# def show():
#       print(Menu_Card)  
      
      
# def add():                  
#         dish=input('Which dish you Want to Add: ')
#         Menu_Card.append(dish)
#         print(Menu_Card)
        
# def update():
#         dish1=input('Which dish you Want to update: ')
#         dish2=input('Which dish you Want to replace: ')
#         for i in range(len(Menu_Card)):
#          if Menu_Card[i] == dish1:
#             Menu_Card[i] = dish2
#         print(Menu_Card)
        
        
# def remove():
#         dish=input('Which dish you Want to Remove')
#         Menu_Card.remove(dish)
#         print(Menu_Card )

# def main():
    
#     in_put=int(input('Print 1 for display \n Print 2 for add \n Print 3 for update \n Print 4 for delete \n '))

    
#     if(in_put==1):
#        show()
    
#     elif(in_put==2):
#         add()
       
#     elif(in_put==3):
#         update()
       
#     elif(in_put==4):
#         remove()
      
        
#     else:
#         print('You Selected Invalid Term')



# if __name__=="__main__":
#     main()
    
    
    
#Task 2

# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."

# Function for floor division
def floor_divide(num1, num2):
    return num1 // num2

# Function for exponentiation
def exponentiate(num1, num2):
    return num1 ** num2


def calci():
   
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Floor Division (//)")
    print("6. Exponentiation (**)")
    
    
    choice = input("Enter choice (1/2/3/4/5/6): ")

    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
    elif choice == '6':
        print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
    else:
        print("Invalid input!")


calci()





