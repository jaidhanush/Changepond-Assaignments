roll_number =(123,124,125,126,127,128)
mixed_type=('subham',123,True,78.90)

print(type(roll_number))
print(type(mixed_type))
print(len(mixed_type))

#Negative Index Slicing
print('Negative index :', mixed_type[-3:-1])



roll_number=123
print(roll_number,type(roll_number))

roll_number=(123,)
print(roll_number,type(roll_number))

# >>> exit()

employee_detail=('jai',123,'triner')
(name,jobid,jobrole)=employee_detail
print(name)

employee_detail=('jai',123,'triner','admin',123)
(name,*jobrole,jobid)=employee_detail #unpacking
print(jobrole)
print(jobid)