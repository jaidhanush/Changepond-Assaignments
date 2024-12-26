fruits=['mango',['fruitpulp','mixedpulp'],'banana',('apple','grapes')]


#Access Values
print(fruits[0])
print(fruits[1])
print(fruits[1][0])
print(fruits[1][1])
print(fruits[3][0])
print(fruits[3][1])

#Iterate over a for loop using range function
menu=['dal','paneer','kofta','tawa paneer','rice','roti']

for i in menu:
    print(i)


author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
for i in author_name:
    print(i)

Timing='it\'s 7.30am'

for i in Timing:
    print(i)


# Take input from user and display

name=input('Enter Employee Name: ')
salary=input('Enter Salary: ')
company=input('Enter Company: ')

print(name,salary,company)


# based on string
print("print('Hello World')")


# based on List

float
input_list=[]
size=int(input('enter a size of list: '))
for i in range(size):
    value=float(input('enter a input value')) 
    input_list.append(value)
print('user defined List:', input_list)

str
input_list=[]
size=int(input('enter a size of list: '))
for i in range(size):
    value=(input('enter a input value')) 
    input_list.append(value)
print('user defined List:', input_list,type(input_list))

# using While Loop
menu=['dal','paneer','kofta','tawa paneer','rice','roti']

i=0
while(i<len(menu)):
     print(menu[i])
     i=i+1

#using While Loop
author_name=('j k rowling','rachel aaron','hans aanrud','verna aardema')
i=0
while(i<len(author_name)):
     print(author_name[i])
     i=i+1
     
# range function for loop
for i in range(3,16,3):
    print(i)
    
for i in range(12,2,-3):
    print(i)
    
    
# range function While Loop

i=3
while i in range(13):
    print(i)
    i=i+3


i=12
while (i>2):
    print(i)
    i=i-3


menu=['dal','paneer','kofta','tawa paneer','rice','roti']

menu[3]='malai paneer'

print(menu)

menu[4:6]=('thandoori','naan')
print(menu)



# add number
value=input('enter number')
add=0
for i in range(len(value)):
    add=add+int(value[i])
    
print(add)