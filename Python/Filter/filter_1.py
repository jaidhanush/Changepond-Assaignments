
# ->Syntex 
# filter(function,iterable)
# -> function: it tests if each element of a sequence True or not
# -> which needs to be filtered, it can be list,set,tuples or contains of any iterators


# -> Lambda Function(Anonymous function)-> function without the Name
# ->this function takes many number of arguments but only one Expression, which is evaluated and returned

# syntex: lambda arguments : expression


# map() function returns a map object(which is an iterator) of the results 
# after applying the given function to each item of given iterable(list,tuple,etc)
# or allows you to proccess and transform all the items in an iterable without using expolicit for loop,
# a technique known as mapping.

# syntex: map(function,iteration[iterable1,iterable2,.............])


from functools import reduce
# def CheckNumber(num): #filter
#     if(num>=70 and num<=90):
#         return True
#     return False


def IncrementNumber(num):
    return num+10

def Addition(num1,num2):
    return num1+num2


def main():
    number=[78,90,45,36,47,13] #Sequence/ Iterable
    fl_res=tuple(filter(lambda num:num>=70 and num<=90,number))
    print('filter Function: ',fl_res)
    
    
    Map_res=list(map(IncrementNumber,fl_res))
    print('Map Function: ',Map_res)
    
    Map_res=list(map(lambda num:num+10,fl_res))
    print('Lambda Map Function: ',Map_res)
    
    reduce_res=reduce(Addition,Map_res)
    print('reduce Function: ',reduce_res)
    
    reduce_res_1=reduce(lambda num1,num2:num1+num2,Map_res)
    print('Lambda reduce Function : ',reduce_res_1)
    
    
if __name__=="__main__":
    main()
    