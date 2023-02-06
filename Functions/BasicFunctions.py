

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


def add_num(num1, num2):
    return num1 + num2

result = add_num(3,5)
print(result)#8

#as python is strongly typed so we dont need to specify return type, but it may result in bugs
add_num('10','20') #1020