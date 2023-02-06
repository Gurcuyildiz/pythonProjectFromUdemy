
class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'





class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'


niko = Dog("puppy")
felix = Cat('kitty')

print(niko.speak())#niko = Dog("puppy")
print(felix.speak())#kitty says meow


# one of the way to do polymorphism
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())


#another way by passing to a method
def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))#puppy says woof!
print(pet_speak(felix))#kitty says meow