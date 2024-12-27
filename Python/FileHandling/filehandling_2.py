import os

def Readfile(filename):
    if(os.path.exists(filename)):
        fd=open(filename,'r')
        Data=fd.read()
        
        Createfile(Data)
        fd.close()
    else:
        print('file not exists')
        
def Createfile(Data):
    fd=open('demo.txt','w')
    fd.write(Data)
    print('Content copy susscessfully')
    fd.close()
        
def main():
    print('Enter the file you want to copy')
    file_name=input()
    Readfile(file_name)
    
    
if __name__=="__main__":
     main()
    