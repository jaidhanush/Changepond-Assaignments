
# for loop are used when you have a block of code which you want to repeat a fixed number of times

food=['dosa','idly','momos','rice','dal']

for i in food :
    print(i)


# range(start,stop,step) -> number of sequence
# start by default zero 
# stop (excluded)
# step (by default 1)


for i in range(11):
    print(i)


for i in range(2,11):
    print(i)


for i in range(2,13,2):
    print(i)


for i in range(20,1,-2):
    print(i)


food=['dosa','idly','momos','rice','dal']
for i in range(len(food)):
    print(food[i])