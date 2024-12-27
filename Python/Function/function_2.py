#Position/Keyword/Default

def Full_Name(FirstName,LastName,Nationality='Indian'):
    return f'Name: {FirstName} {LastName} Nationality {Nationality}'

def circle(rad,pi=3.14):
    return pi*(rad*rad)



radius=int(input())


def main():
    # Result=Full_Name('jai','Dhanush')
    # print('positional Argument: ',Result)
    # Result=Full_Name('other','Dhanush','jai')
    # print('positional Argument Exchange: ',Result)
    # Result=Full_Name(FirstName='jai',LastName='Dhamush')
    # print('Keyword Argument: ',Result)
    # Result=Full_Name(LastName='Dhamush',Nationality='others',FirstName='jai')
    # print('positional Argument: ',Result)
    
    print(circle(radius,3.14))
    print(circle(radius))
    print(circle(pi=3.14,rad=radius))
    print(circle(rad=radius))
    
    
if __name__=="__main__":
    main()
  