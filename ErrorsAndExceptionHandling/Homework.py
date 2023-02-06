
'''1- Handle the exception thrown by the code below by using try and except blocks.

for i in ['a','b','c']:
    print(i**2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int' '''

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('Please provide an int')



'''2- Handle the exception thrown by the code below by using try and except blocks.
 Then use a finally block to print 'All Done.'

x = 5
y = 0

z = x/y
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero'''
try:
    x = 5
    y = 0

    z = x/y
except:
    print('there is a mistake with your calculation')

finally:
    print('all done')


'''3- Write a function that asks for an integer and prints the square of it.
 Use a while loop with a try, except, else block to account for incorrect inputs.'''
def ask():
    while True:
        try:
            number = int(input('Input an integer'))
            number = number **2
        except:
            print('An error occured. Please try again')
            continue
        else:
           # print(input(f'Thank you! your number is squared is :  {number}'))
            break
    print(input(f'Thank you! your number is squared is :  {number}'))

print(ask())
