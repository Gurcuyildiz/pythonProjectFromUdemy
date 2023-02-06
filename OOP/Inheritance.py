
#this is our base class
class Animal():

    def __int__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


myaniml = Animal()
print(myaniml)# no printing , showing object index at animal class<__main__.Animal object at 0x000001CEDC961550>
print(myaniml.__int__())# this will print 'Animal created'  string
print(myaniml.eat()) #I am eating


#in order to inherite the function from animal class, we put Animal class name into the paranthesis of Dog class
class Dog(Animal):
    def __int__(self):
        #in order to call method from Animal class, we use below line
        Animal.__int__(self)
        print(' Dog created')
    def who_am_i(self):# this overwrite the method in animal class
        print('I am an dog')

    def bark(self):
        print('I am barking')

    def eat(self):
        print('I am eating and I am a dog')


myaniml1 = Animal()
print(myaniml1.__int__())#this will still print 'Animal created'

mydog = Dog()
print(mydog.__int__())# Dog created