
#Iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary

#Syntac for  loop
mylist = [1,2,3,4,5,6,7,8,9,10]

for eachItem in mylist:
    print(eachItem)


for jelly in mylist:
    #this will print hello for each of number in iteration
    print('Hello')

for num in mylist:
    #check for even
    if num %2 ==0:
        print(num)
    else:
        print(f'Odd Number: {num}')



list_sum = 0
for num in mylist:
    list_sum = list_sum +num
    print(list_sum)
#print ouside of for loop for result
print(list_sum)

my_string = 'Hello world'
for letter in my_string:
    print(letter)

#same with above
for letter in 'Hello World':
    print(letter)

#or if you dont want to use a variable name in for loop underscore is used
for _ in 'Hello world':
    print('cool')

#Tuples
tup =(1,2,3,4)
for item in tup:
    print(item)

#Tuples inside the list called tuple packing
myliste = [(1,2),(2,3),(4,5),(6,7)]
print(len(myliste))
for item in myliste:
    print(item)
# (1, 2)
# (2, 3)
# (4, 5)
# (6, 7)

#this is called unpacking tuple
for (a,b) in myliste: # can be  for a,b in myliste : or for a in myliste:
    print(a)
    print(b)
# 1
# 2
# 2
# 3
# 4
# 5
# 6
# 7
myliste1 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myliste1:
    print(b)# 2 5 8


#Dictionaries: iteration is happening through keys by default
d= {'k1': 1,'k2': 2,'k3':3}
for item in d:
    print(item)#k1 k2 k3

#if you want item pairs we use d.items()
for item in d.items():
    print(item)#('k1', 1)
               #('k2', 2)
               #('k3', 3)
    #or
for key, value in d.items():
    print(value)
    print(key)

#if want to get just values
for value in d.values():
    print(value)#1 2 3



## For loop in a print statement

items = [1,2,3,4]
for item in items:
    print(item)

# 1
# 2
# 3
# 4



#the same way of above
print('Item in the items list :',*items)#Item in the items list : 1 2 3 4

#if you want number to be in a new line
print('Item in the items list :',*items, sep='\n')
# Item in the items list :
# 1
# 2
# 3
# 4
