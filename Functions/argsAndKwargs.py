
#These are two functional parameter
# A- one star which is args
# B- two stars which is kwargs

def myfunc(a,b):# a, b are positional argument, a is the 1st, b is the 2nd
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05# sum method here is a built in function

myfunc(40,60)
print(myfunc(40,60))#5.0

def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(40,60))# yukaridaki ile ayni sonucu verecek cunku obur parametlerin 0 a esitlenmis
#it gives us the flexibility of adding more value when calling function
print(myfunc(40,60,10,20,30))# we can put 5 or just 3 argument
#if we put more than 5 then it will give error




#################### * ARGS in Function     ####################

# args
# means arbitrary number of arguments
#in order not to deal with the all above problem, we use * args as parameter to the function then we can pass
#as many argument we want to the function when called
#we can use any keyword in there instead of args but by convention it is used args, the important point is *
# * args returns a tuple
def myfunc1(*args):
    return sum((args)) * 0.05



print(myfunc1(10,20,30,40,50,60,70))





##################     ** KWARGS (Key word argument)    ##################

#kwards return a dictionary
#we can use any word instead of kwargs but it by default conventional to use it
def myfunc2(** kwargs):
    print(kwargs)#{'fruit': 'apple', 'veggie': 'lettuce'}
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didn\'t find any fruit here')

print(myfunc2(fruit='apple', veggie='lettuce'))


def myfunc3(*args, ** kwargs):
    print(args)#(10, 20, 30)
    print(kwargs)#{'fruit': 'orange', 'food': 'eggs', 'animal': 'dogs'}
    print('I would like {} {}'.format(args[0], kwargs['food']))#I would like 10 eggs

#as args is the first parameter, we have to give at the beginning of function
#then give kwargs argument, if we place such as 100 after dogs, it will give error
print(myfunc3(10,20,30,fruit='orange', food='eggs',animal='dogs'))



def myfun(*args):
   liste = [x for x in args if x % 2 == 0]
   print(liste)
   return liste

print(myfun(1,2,3,4,5,6))#[2, 4, 6]