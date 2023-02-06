
mylist =[1,2,3]

for num in range(10):#print number all the way up to 10 not including 10
    print(num)

for num in range(3,10):#print number from 33 to 10 not including 10
    print(num)

for num in range(0,10,2):#start from 0 till 10 not inlcuding 10  by stepping one number
    print(num)#0,2,4,6,8

print(list(range(0,11,2)))# we can cast the list by using list key word
#[0, 2, 4, 6, 8, 10]


index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
# At index 0 the letter is a
# At index 0 the letter is b
# At index 0 the letter is c
# At index 0 the letter is d
# At index 0 the letter is e
#or
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1# a b c d e


###Enumerate
words = 'abcde'
for item in enumerate(words):
    print(item)
#it gives tuple
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
for index, letter in enumerate(words):
    print(index)
    print(letter)
    print('\n')
#
# 0
# a
#
#
# 1
# b
#
#
# 2
# c
#
#
# 3
# d
#
#
# 4
# e

#######   Zip funtion
myliste =[1,2,3]
myliste2 = ['a','b','c']
for items in zip(myliste,myliste2):
    print(items)
# zip two list together in tuple format
# (1, 'a')
# (2, 'b')
# (3, 'c')
#will put into list
print(list(zip(myliste,myliste2)))
#[(1, 'a'), (2, 'b'), (3, 'c')]

#### Quickly check if something is in list
print('x' in [1,2,3])#False

print(2 in [1,2,3])#True

print('a' in 'word')#True

print('mykey' in {'mykey': 345})#True

d= {'mykey': '345'}
print(345 in d.keys())

print('x' in ['x', 'y','z'])#True


###  Max Min function
mylists =[10,20,100]
print(max(mylists))#100
print(min(mylists))#10


#from random library import shuffle function
from random import shuffle

numList = [1,2,3,4,5,6,7,8,9,10]
#this is not returning aynthing, this is a inplace function but shuffle the list
shuffle(numList)
print(numList)#[10, 9, 6, 5, 2, 7, 3, 1, 8, 4]
#if you want to leanr the type of the shuffled list
random_list = shuffle(numList)
print(type(random_list))#<class 'NoneType'>


#### Grabbing a random int from random library

from random import randint
#will give any int num between 0 100
print(randint(0,100))
print(randint(0,100))

### How to take user input funcrion
result =input('Select a number between 0 to 200')
name = input('What is your name?')
print(result)
print(name)

result1 = input('Your fab num?')
print(type(result1))#str as input accept everything as string
#if we want to cast a string in to int
print(float(result1))
print(type(result1))