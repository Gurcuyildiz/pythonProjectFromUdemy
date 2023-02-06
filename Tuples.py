
#Tuples are very similar to lists but they are immutable.
#Once an element is assigned to a tuple, it cant be changed
#Tuples uses paranthesis (1,2,3)

t =(1,2,3)
my_list = [1,2,3]

print(type(t))#<class 'tuple'>
print(type(my_list))#<class 'list'>

print(len(t))#3
print(len(my_list))#3

#Tuples accept mixed of data types
t1 =( 1, 'oranges', 2,21)
print(t1)#(1, 'oranges', 2, 21)

###Tuples can be sliced and indexed
print(t1[0])#1

##To see how many an element exist
t3 =('a','a','b','a')
print(t3.count('a'))#3
#will return the index of the first occurance
print(t3.index('a'))#0

##TypeError: 'tuple' object does not support item assignment
#t3[0] = 'New'
#print(t3)
