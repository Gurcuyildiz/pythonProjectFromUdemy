
#List comprehension is a unique way of quickly creating list with Python

#if we want to put each letter of this string into a list, below is the general one
mystring = 'Hello '
mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)#['H', 'e', 'l', 'l', 'o', ' ']

# but in Python there is a more easy way

mylist2= [letter for letter in mylist]
print(mylist2)# same result as above

num =[x for x in 'abcdex']
print(num)#['a', 'b', 'c', 'd', 'e', 'x'

numList = [x for x in range(0,11)]
print(numList)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numList = [x**2 for x in range(0,11)]
print(numList)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#we can put if inside list comprehension
number =[x for x in range(0,11) if x%2==0]
print(number)#[0, 2, 4, 6, 8, 10]


celcius =[0,10,20,34.5]
fahrenheit =[((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)#[32.0, 50.0, 68.0, 94.1]
#same as the above
fahrenheit1 =[]
for temp in celcius:
    fahrenheit1.append((9/5)*temp +32)
    print(fahrenheit1)

#if clause in list comprehension
#if x divided by 2 is equal to 0 then print thar number, if not print 'ODD' instead of printing from 0 till 11
# not including 11
result = [x if x % 2 ==0 else 'ODD' for x in range(0,11)]
print(result)#[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]


#### Nested loop in list comprehension
mylis =[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylis.append(x*y)

print(mylis)#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

