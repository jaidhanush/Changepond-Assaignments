

mixed_type={True,12,34}

#add: will add an element
mixed_type.add('apple')
print('Add Method:',mixed_type)

#remove/discard/pop
mixed_type.remove('apple')
print('Remove Method:',mixed_type)

mixed_type.discard(12)
print('Discard Method:',mixed_type)

mixed_type.pop()
print('Pop Method:',mixed_type)



company={'Cognizent','Infosys','ChangePond','TCS'}
morecompany={'TATA','Infosys','Neosoft','TCS'}

inter_method=company.intersection(morecompany)
print('Intersection Method: ',inter_method)


inter_method=company&morecompany
print('Intersection Method: ',inter_method)

#Union Method
union_method=company.union(morecompany)
print('Union Method: ',union_method)

union_method=company|morecompany
print('Union Method: ',union_method)


company={'Cognizent','Infosys','ChangePond','TCS'}
update_com={'Neosoft','Tata'}

company.update(update_com)
print('Updated company:' ,company)


#Differnce Method

fruit={'apple','banana','grapes','Mango'}
morefruit={'watermelon','apple','grapes','tomato'}

diff_method=fruit.difference(morefruit)
print('difference method: ',diff_method)

diff_method=morefruit.difference(fruit)
print('difference method: ',diff_method)
