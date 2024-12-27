

my_list=[1,2,3,4,2,3]


def check(val):
    for i in my_list:
        if(i==val):
            return val
        
    
# for i in my_list:
#     check(i)
        
print(check(3))