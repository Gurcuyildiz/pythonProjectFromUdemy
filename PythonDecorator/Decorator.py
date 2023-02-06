

'''
    Decorator allows you to decorate a function

    Python decorator allow you to tack on extra functionality to an already existing function

    They use @ operator and then are placed it on the top of the original function

    Now you can easily add on extra functionality with a decorator

    @some_decorator
    def simple_function():
       do some stuff
       return something

'''
def hello(name ='Jose'):
    print('The helo() function is being executed')

    #here we are defining a function inside another function
    def greet():
        return '\t This is the greet() function is executed'
    def welcome():
        return '\t This is the welcome() function is executed'
    #here we are calling the function we define inside hello function and printing
    # print(greet())
    # print(welcome()
    print('I am going to return a new function')
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello('Jose')
#print(my_new_func)
# The helo() function is being executed
# I am going to return a new function

print(my_new_func())
# The helo() function is being executed
# I am going to return a new function
# 	 This is the greet() function is executed


#print(hello())
# The helo() function is being executed
# 	 This is the greet() function is executed


def cool():

    def super_cool():
        return 'I am super cool'
    return super_cool


some_func = cool()
#print(some_func)# doesnt print anything as we didnt call the function in print statement
#print(some_func())#I am super cool


#we can put function as a parameter of another function
def hello():
    print('Hi Jose')

def other(some_def_func):#when passing a function here as parameter no paranthesis
    print('Other code runs here')
    #printing the function passed as parameter
    print(some_def_func())#when calling this parameterized funtion, we put paranthesis

print(hello())#Hi Jose
print(other(hello))
#Other code runs here
#Hi Jose



def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before original function')

        original_func()

        print('Some extra code after original function')
    return wrap_func


def func_need_decorator():
    print('I want to be decorated')


print(func_need_decorator())
#I want to be decorated

decorated_func = new_decorator(func_need_decorator)
print(decorated_func())
# Some extra code before original function
# I want to be decorated
# Some extra code after original function



#if i put new decorator function into @decorator then will see the same result as above
#because it means it will pass this decorator function as parameter of the func_need_decorator function
@new_decorator
def func_need_decorator():
    print('I want to be decorated')

print(func_need_decorator())
# Some extra code before original function
# I want to be decorated
# Some extra code after original function


## If you dont want to have this function just disable it
#@new_decorator
def func_need_decorator():
    print('I want to be decorated')