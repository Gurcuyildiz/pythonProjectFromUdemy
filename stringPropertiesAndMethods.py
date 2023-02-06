name = "Sam"
#changing S to P
#name[0] = "P"# we can't do this as strings are immutable, unchangable

last_letters = name[1:] #am

#String Concatenation

#can add P through concatenation
print('P'+last_letters)#Pam

#Multiplication in string
letter = 'z'
print(letter*10)#zzzzzzzzzz

x = "Hello World"
print(x.upper())# to turn into all upper case
print(x.casefold())#to turn into all lower case
print(x.isalnum())#is it alpha numeric, true or false
print(x.islower()) #checks if it is lowercase
print(x.isprintable())
print(x.lower())


print(x.split())# will split based on the space or

#the letter/word you specified by removing that specified
x = 'This is a string'
print(x.split('i'))# ['Th', 's ', 's a str', 'ng']


#Format() method takes the parameter in format emthod and put into the {}placeholder
print('This is a string {}'.format('INSERTED'))

#format() method will put everything in the same order
print('The {} {} {}'.format('fox','brown','quick'))#The fox brown quick

#format() method will put everything in the index order, fox,brown, quick in format() is index,0,1,2
print('The {2} {1} {0}'.format('fox','brown','quick'))# The quick brown fox

print('The {0} {0} {0}'.format('fox','brown', 'quick'))# The fox fox fox

#we can define with variable name like assignment
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

#below two method are the same
name = "Jose"
print('Hello, his name is {}'.format(name))#Hello, his name is Jose
#This is called F string formating in python 3.6 version
print((f'Hello, his name is {name}'))

name = "Sam"
age = 3
print(f'{name} is {age} years old')



###### join()
mylist = ['a','b', 'c']
print(' '.join(mylist))#a b c
print('--'.join(mylist))#a--b--c
print('+'.join(mylist))#a+b+c
print(''.join(mylist))#abc






