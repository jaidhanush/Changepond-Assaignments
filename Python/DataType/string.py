

statement1='Good Afternoon'


print(len(statement1))

for i in range(1,7):
    print(statement1[i])

print(statement1[-10:-1])

# using different quotes in single element
timing='it"s 12.12pm'
print('using different quotes in single element: ',timing)

# using same quotes in same element
timing='it\'s 12.12pm'
print('using different quotes in single element: ',timing)

name='mayank'
age=45
print(name+" "+str(age))

print(f'my name is {name} {age} years old')