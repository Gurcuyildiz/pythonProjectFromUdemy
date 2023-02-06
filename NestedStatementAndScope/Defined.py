

x = 25# global
def printer():
    x=50# local
    print(x)

print(x)#25
print(printer())#None


############    LEGB  RULE     ########
'''L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...'''

lambda num:num**2
name = 'THIS IS A GLOBAL STRING'
def greet():
    name ='sammy'

    def hello():
        print('Hello '+name)#function will in the function anywhere this name is defined, it is found, it will be used
    print(hello())

print(greet())#Hello sammy

def greet():
    #name ='sammy'

    def hello():
        print('Hello '+name)#function will in the function anywhere this name is defined, it is found, it will be used
        #if not then it will use global defined variable
    print(hello())

print(greet())#Hello THIS IS A GLOBAL STRING



def greet():# and then this function executed
    #ENCLOSING
    name = 'Sammy'

    def hello():#then this function is called
        #LOCAL
        name ='I AM A LOCAL'
        print('Hello '+name)
    hello()#this is first executed then
print(greet())#Hello I AM A LOCAL



def greet():# and then this function executed, from this level variable name is called and printed
    #ENCLOSING
    #name = 'Sammy'

    def hello():#then this function is called
        #LOCAL
       # name ='I AM A LOCAL'
        print('Hello '+name)
    hello()#this is first executed then
print(greet())#Hello THIS IS A GLOBAL STRING



# how to print both local and global level of defined variable
x= 50
def func(x):
    print(f'C is {x}')
    x = 200#local reassignment
    print(f'I just locally changed x to {x}')

print(func(x))#C is 50
print(func(x))#I just locally changed x to 200 , we defined a local variable in the scope of function
# so it will be used, it doesn't have ability to go outside of function and used value of x which is 50

print(x)#50

x = 60
def func1():
    global x
    print(f' X is {x}')

    #Local Reassignment on a global variable
    x= 'New value'
    print(f'I just locally changed X to {x}')

print('hoho')
print(func1())#I just locally changed X to New value

#istead of using global keyword in a function, use method/function with a return sttement