

#we use 3 keywords
'''
  try: this is the code of block to be attempted( may lead to an error)

  except: block of code will execute in case there is an error in try block

  finally: a final block of code to be executed, regardless of an error

'''

def add(n1,n2):
    print(n1 + n2)

print(add(4,7))#will work smoothly


number1 = 10
#number2 = int('Please provide a number')

#print(number1,number2)# this will give error becaue number2 type is string as it is coming from an input function
#which always return string

#ValueError: invalid literal for int() with base 10: 'Please provide a number'

#in order not to have error that stopped the rest of execution we use try except
try:
    result = 10 + 10
except:
    print('hey, it looks like you are not adding correctly')
else:
    print('Add went well')
    print(result)






#   try except finally block
try:
    f = open('testfile', 'w')# this will open the file, if the file doesn't exist then it will create one with that name
    f.write('Write a test line')
except TypeError:
    print('there was a type error')
except OSError:
    print('Hey you have an OS error')
finally:
    print('I always run')

#
#if you dont knowthe type of error after a specified error, just write except then it will cover all error
try:
    f = open('testfile', 'w')
    f.write('Write a test line')
except TypeError:
    print('there was a type error')
except:# this will catch all other error
    print('All other exceptions')
finally:
    print('I always run')

# I always run



def ask_for_int():
    try:
        result = int(input('Please provide number : '))
    except:
        print('Whoops!, That is not a number')

    finally:
        print('End of try/except/finally')

print(ask_for_int())

#if we put this function into a while loop it will keep asking till an integer is provided
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number : '))
        except:
            print('Whoops!, That is not a number')
        else:# we can put else here too
            print('Thank you')
            break # if number is provided loop will be broken, if not, it will keep asking

        finally:
            print('I am going to ask you again')

