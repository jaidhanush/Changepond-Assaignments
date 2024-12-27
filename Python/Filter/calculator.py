import arithamatic


print('Enter the opearator')
select=int(input())

def main():
    num1=int(input('Enter First Number: '))
    num2=int(input('Enter Second Number: '))
    
    if(select==1):
        ans=arithamatic.Addition(num1,num2)
        print(f'{num1}+{num2}={ans}')
    elif(select==2):
        ans=arithamatic.Subtraction(num1,num2)
        print(f'{num1}+{num2}={ans}')
    elif(select==3):
        ans=arithamatic.Multiplication(num1,num2)
        print(f'{num1}+{num2}={ans}')
    else:
        print('enter valid Operator')
   
    
if __name__=="__main__":
    main()