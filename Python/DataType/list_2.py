
#list is a mutable Object
Mixed_type=['jai',21,56.34,True]

#Slicingt :[start:stop(excluded)]
print("Slicing",Mixed_type[1:4])
print("Slicing",Mixed_type[1:])

Mixed_type[3]=False
print('modifying:',Mixed_type)

Mixed_type[0:3]='adithiya',23,6.7
print('Using Slicing:',Mixed_type)

del Mixed_type[2]
print('Final List:',Mixed_type)


#List Methods :

fruits=['mango','bannana']

#append =>add an element in the last
fruits.append('Grapes')
print('append Methos:',fruits)

#insert=> add an element at the Specified Position
fruits.insert(0,'apple')
print('insert Methos:',fruits)

#extend=> add a list of element or iteratable values 
#at the current list

fruits.extend(['watermelon','apple'])
print('Extend Methos:',fruits)

fruits.extend('watermelon')
print('Extend Methos:',fruits)

# fruits.extend(True) #Error
# print('Extend Methos:',fruits)


#pop() remove element of the specific position
fruits.pop(0)
print('pop Methos:',fruits)

#remove() 
fruits.remove('watermelon')
print('Remove Methos:',fruits)

city=['mumbai','Nagpur','pune','Nagpur']
city.remove('Nagpur')
print('Remove Methos:',city)


#index()
index_method=city.index('Nagpur')
print('Index method:', index_method)

#count
count_method=city.count('Nagpur')
print('count method:', count_method)

print(city)