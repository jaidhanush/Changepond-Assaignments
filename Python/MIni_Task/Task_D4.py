
import sys

#Task 1

def find(my_list,rt):
 temp=0
 for i in range(len(my_list)):
        if(my_list[i]==rt):
            temp=temp+1
 return temp




def repeating(my_list):
 temp=0
 temp2=0
 for i in range(len(my_list)):
        first = find(my_list,my_list[i])

        if(first>temp):
            temp=first
            temp2=my_list[i]

 return temp,temp2


            
length=input('enter the length of the list')
my_list1=[]

for i in range(int(length)):
     my_list1.append(input('enter the data'))

result = repeating(my_list1)


print(f"Most repeating count: {result[0]}")
print(f"repetition Element: {result[1]}")
            

# ====================================================================================

#Task 2

F_name=input('What is your first name:')
S_name=input('What is your second name:')
Age=input('What is your Age:')
City=input('Enter Your City:')

print("-"*50)

print('your First name is :',F_name)
print('your Second name is :',S_name)
print('your Age is :',Age)
print('your City is :',City)


# ==============================================================================


# Task 3

length=input('enter the length of the list')
my_list=[]

for i in range(int(length)):
     my_list.append(int(input('enter the data')))

max=-sys.maxsize - 1
min=sys.maxsize
add=0
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
    if(my_list[i]<min):
        min=my_list[i]
    add=add+my_list[i]
    

print(f"Maximum Size of List:{max},Minimum Size of List: {min},Added Element: {add}")
    