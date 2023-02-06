

class Circle():

    pi = 3.14

    def __int__(self, radius = 1):
        self.radius = radius
        self.area = radius *radius * Circle.pi


    #Methhod
    def get_circumfrence(self):
        return self.radius * self.pi * 2



my_circle = Circle()
my_circle.get_circumfrence()
print(my_circle.get_circumfrence())
print()

