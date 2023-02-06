

class Dog():


    species = 'Mammal'


    def __int__(self,breed, name, spots):# this is a special method
        self.breed = breed
        self.name = name
        self.spots = spots

my_sample = Dog()# this is  an instance of Dog class
print(type(my_sample))#<class '__main__.Dog'>


my_dog = Dog(breed='Lab', name='Sammy',spots=False)# this should be accepted but not working here why
my_dog.breed = 'Lab' # assign value is working in that way
print(my_dog.breed)#Lab

print(my_dog.species)