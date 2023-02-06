

class Animal():

    def __init__(self, name):
        self.name = name


    def speak(self):
        raise NotImplementedError('Sub class must implement this abstract method')



class Dog(Animal):

     def speak(self):
        return self.name + ' says woof'



class Cat(Animal):

    def speak(self):
        return self.name + 'says meow'


fido = Dog('Turbo')
isis = Cat('Minos')
print(fido.speak())
print(isis.speak())