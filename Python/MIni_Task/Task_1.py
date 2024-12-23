# #Swaping Two Nnumber

# num_1=int(input('Enter First Number :'))
# num_2=int(input('Enter First Number :'))

# num_1,num_2=num_2,num_1

# print(num_1,num_2)

# print("-"*50)


# #--------------------------------------------

# #Swaping Two Nnumber Without 3rd Variable

# num_1=int(input('Enter First Number :'))
# num_2=int(input('Enter First Number :'))

# value=num_2
# num_2=num_1
# num_1=value

# print(num_1,num_2)

# print("-"*50)


#--------------------------------------------

# Bill=int(input('Enter the Bill Amount :'))
# Tip=int(input('Enter How Much Tip You Want like 10%,20%, or 30 % :'))
# members=int(input('Enter Total Members:'))

# final_bill=((Bill/100*Tip)+Bill)/members

# print(final_bill)


#--------------------------------------------

# value_1=int(input('Enter The Value:'))
# print('Integer',value_1,type(value_1))

# value_2=str(input('Enter The Value:'))
# print('Integer',value_2,type(value_2))

# value_3=float(input('Enter The Value:'))
# print('Integer',value_3,type(value_3))

Food=['burger','veg pizza','momos','Chinese','garlic bread','french fries','non-veg pizza']
print('Data type of Food:',type(Food))
print('Total Food items:',len(Food))

Food.append('Kabab')
print(Food)

del Food[2:4]
print(Food)