# Function:
    
#     -> A Function is a Block of code that performs a specific Task.
   
#     -> functions are reusable pieces of programs.
    
#     -> they allow you to give a name to a block of statement, allowing you to run that block using specified
#        name anywhere in your program and any number of times this is known as calling the function.
    
#     -> the names given in the function definition are called parameters whereas the value you supply
#        in the function call are arguments.
       
#     -> you define a function with def keyword, then write identifier(name) followed
#        by paranthases and a colon.
       
#     -> used to exit from a function and go back to the function caller and return the specified value 
#        or data item to the cellular.



def demo():
    print('inside Demo')
    
def demo_1(value):
    print('inside Demo_1: ',value)

def demo_2(value1,value2):
    print('inside Demo_2: ',value1,value2)
    print('Addition: ',value1+value2)
    
def demo_3(value1,value2):
    print('inside Demo_3: ',value1,value2)
    add=value1+value2
    sub=value1-value2
    return add,sub
    # print( add)
    # print(sub) 
    
    
def main():
    demo()
    print('-'*50)
    demo_1(12)
    print('-'*50)
    demo_2(12,23)
    print('-'*50)
    ans1,ans2=demo_3(23,12)
    print(ans1)
    print(ans2)
    
if __name__=="__main__":
    main()