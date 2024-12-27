# The Arguments that are given after the name of the program in the command line shell of the operating system

from sys import* 
def Addition(value1,value2):
    ans=value1+value2
    return ans

def main():
    # print('Application Name: ',argv[0])
    # print('Argument Name1: ',argv[1])
    # print('Argument Name1: ',argv[2])
    
    if(len(argv)==2):
        if(argv[1]=='--U'):
            print('Pass Arguments: Application_Name First')
            exit()
    
        if(argv[1]=='--H'):
            print('Pass Arguments: Application used to add two numbers')
            exit()
            
    if(len(argv)!=3):
        print('Invalid number of arguments')
        print('please use --U flag to get usage')
        print('please use --H flag to get usage')
        exit()
        
        
        
    Ret=Addition(int(argv[1]),int(argv[2]))
    print('Addition: ',Ret)
    
    
    
if __name__=="__main__":
    main()