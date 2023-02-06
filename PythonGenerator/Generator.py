'''
   when a generator function is compiled they become an object that support an iteration procotol
   that means when they are called in your code, they dont actually return a value and then exit
'''
def create_cube(n):
    for x in range(n):
        yield x**3

print(create_cube(10))#<generator object create_cube at 0x00000266773BD630> means it is a generator object, it does
#return a value
#print(list(create_cube(10)))#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



#A- the below code is better in terms of
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

def gen_fibonacci(n):
    a=1
    b=1
    output = []
    for x in range(n):
        output.append(a)
        a,b = b,a+b
    return output

print(gen_fibonacci(10))
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

'''
  next() and iter() built-in functions
  
  A key to fully understanding generators is the next() function and the iter() function.

The next() function allows us to access the next element in a sequence. Lets check it out:
 '''
def simple_gen():
    for x in range(3):
        yield x
#what does that mean
for number in simple_gen():
    print(number)
#above function will print the below line
# 0
# 1
# 2

#let assign 'g' to a simpe_gen() instance, by doing this we are calling simple_gen()
g = simple_gen()
#when we print g, it will say it is a generator object
print(g)#<generator object simple_gen at 0x000001EFDFD9FED0>

#next() will request the next value of the yield object
print(next(g))# will give zero
print(next(g))#1, then will give the next one in the memory
print(next(g))#2
#print(next(g))# will give error of 'StopIteration'


#### Iter function
s = 'hello'
for letter in s:
    print(letter)
#will print the below line as a general function of for loop
# h
# e
# l
# l
# o

# if we want to use next() function to iterate over s,it will give error
#print(next(s))#TypeError: 'str' object is not an iterator

#first use iter function to store the letter in a new variable
s_iterable = iter(s)

print(next(s_iterable)) #h
print(next(s_iterable)) #e
