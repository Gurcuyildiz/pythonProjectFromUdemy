

class Dog():

    species = 'Mammal'

    def __int__(self, breed, name, spots):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name


    #Operations/Actions -----> Methods
    def bark(self):#we need to pass self here in order to get access to the above attributes that attached to self keyword
        print('WOOF! My name  is {}'.format(self.name))# we have to refer by self.name,
        # if we just use name then we wont accees to attributes of that class


     # we can give any argument here outside of class too, if it is outside of class no need of self keyword
    #as it is not connected to self keyword
    def bark1(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))