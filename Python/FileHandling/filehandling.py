import os

def Createfile(filename):
    if(os.path.exists(filename)):
        print('File is Already Exists')
    else:
        file = open(filename,"w")
        
        
def main():
    print('Enter File YOu want to create')
    file_name=input()
    Createfile(file_name)
    
    
if __name__=="__main__":
     main()
    