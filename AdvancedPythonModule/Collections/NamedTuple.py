from collections import namedtuple
#in a normal tuple function, we call any element by index
mytuple = (10, 20,30)
print(mytuple[0])#10

#what if the tuple is too big not to remember what what index is the element

#how to define a named tuple
#it accepts two parameter, type and and a list
#Dog is going to be type and the dog will have a age, breed and name
Dog = namedtuple('Dog', ['age', 'breed','name'])

#create an object Dog
sammy = Dog(age=5,breed='Hasky',name='Sam')
print(type(sammy))#<class '__main__.Dog'>
#printing sammy object
print(sammy)#Dog(age=5, breed='Hasky', name='Sam')
#can access to other element
print(sammy.age)#5
print(sammy.name)#Sam