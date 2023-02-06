

#define a list
#integer
my_list = [1,2,3,4]
#mixed
lists = ["String", 10.4, 34, ]
print(len(lists))#3

#accessing element of list
my_list = ['one', 'two', 'three']
print(my_list[0])

another_list =['four', 'five']

#combine two list(will add another list at the end of mylist)
print(my_list+another_list)#['one', 'two', 'three', 'four', 'five']

new_list = my_list+another_list
print(new_list)#['one', 'two', 'three', 'four', 'five']

#can change the element of list
new_list[0] = 'Caps'
print(new_list)#['Caps', 'two', 'three', 'four', 'five']

#add element to the end of list with append method
new_list.append('six')
print(new_list)#['Caps', 'two', 'three', 'four', 'five', 'six']

#removing element from the list
new_list.pop()#remove the last element
print(new_list)#['Caps', 'two', 'three', 'four', 'five']

poped_item =new_list.pop()
print(poped_item)#five

new_list.pop(-1)#this also removes the last element
print(new_list)#['Caps', 'two', 'three']

new_list.pop(0)
print(new_list)#['two', 'three']
new_list.pop(1)
print(new_list)#['two']


###Sort() method
string_list = ['a','x','h','d','b']
string_list.sort()#this will sorted all the list, it doesnt have a return type so no need to save into a variable
#even if it does, will return/print nothing
print(string_list)#['a', 'b', 'd', 'h', 'x']

sorted_list =string_list.sort()
print(type(sorted_list))#<class 'NoneType'> means doesnt have any object

#if we want to assign
string_list.sort()
new_string_list =string_list
print(new_string_list)#['a', 'b', 'd', 'h', 'x']

num_list = [2,6,4,9,0]
print(num_list.sort())#None
num_list.sort()
print(num_list)#[0, 2, 4, 6, 9]



####Reverse() Method
num_list.reverse()
print(num_list)#[9, 6, 4, 2, 0]
string_list.reverse()
print(string_list)#['x', 'h', 'd', 'b', 'a']