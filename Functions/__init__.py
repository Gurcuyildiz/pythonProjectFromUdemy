
#Creating basic function
def say_hello():
    print('Hello')


say_hello()

def say_hello(name):
    print(f'Hello {name}')

say_hello('Jose')#Hello Jose


#Default value in function parameters
#if nothing is passed to function when calling, then it will use default value
def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello()#Hello Default


