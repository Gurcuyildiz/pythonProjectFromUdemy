
'''
   1- Create a generator that generates the squares of numbers up to some number N.
'''



def square_num(x):
    for num in range(x):
       yield num**2

for y in square_num(6):
      print(y)


'''
 2- Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:

import random

random.randint(1,10)
'''
###this is not working, correct it #######################################################
# import random
# range.randint(1,10)
#
# def rand_num(low, high,n):
#     for num in range(n):
#          yield random.randint(high,low)
#
# for each in rand_num(1,10,12):
#     print(each)


'''
 3- Use the iter() function to convert the string below into an iterator:
'''
str = 'hello'
str_itered = iter(str)
print(next(str_itered)) #h

# for letter in str_itered:
#     print(letter)

#print(next(str_itered))#StopIteration error is given, coz nothing is left in memory


'''
  4- Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
4
5
Hint: Google generator comprehension!
'''