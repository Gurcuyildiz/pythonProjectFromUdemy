#1- Reverse the string 'hello' using slicing
s = 'hello'
print(s[::-1])

#2- Given the string 'hello', give two methods of producing the letter 'o' using indexing
print(s[4])
print(s[4:])
print(s[-1])

#3-Build this list [0,0,0] two seperate ways
my_list =[0]*3
print(my_list)
mylist= [0,0,0,]
print(mylist)
mylist1 =[]
mylist1.append(0)
mylist1.append(0)
mylist1.append(0)
print(mylist1)

#4-Reassign 'hello' in this nested list to say 'goodbye' instead
list = [1,2,[3,4,'hello']]
list[2][2] = 'goodbye'
print(list)

#5- Sort the list below with two method
liste = [5,3,4,6,1]
liste.sort()#a
sorted(liste)#b
print(liste)

#6- Using keys and indexing, grab the 'hello' from the following dictionaries
d= {'simple_key':'hello'}
print(d.values())
print(d['simple_key'])

d1= {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])

d2 ={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])

d3 ={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])

#7- Use a set to find the unique values of the list below
list2 =[1,2,2,33,4,4,11,22,3,3,2]
print(set(list2))

