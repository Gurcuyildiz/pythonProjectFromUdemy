
#1- Use for loop and slipt() method and if to create a statement that will print out words that starts with 's'
st = 'Print only the words that starts with s in this sentence'
#converted string into list by space delimeter then accessing the element of list
newSt = list(st.split(" "))
for item in newSt:
    if item.startswith('s'):
        print(item)#starts s sentence
#2nd solution
for word in st.split():
    if word[0].lower() == 0: # or can be used as well
        print(word)


#2- Use range() to print all the even numbers from 0 to 10
#used list comprehension here
num= [x for x in range(0,11) if x%2==0]
print(num)#[0, 2, 4, 6, 8, 10]

#2nd solution
for num in range(0,11,2):
    print(num)


#3-Use a list Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
number =[x for x in range(1,50) if x%3==0]
print(number)#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]



#4- Go through the string below and  if the length of a word is even print even
mystring = 'Print every word in this sentence that has an even number of letters'
new_mystring =list(mystring.split(" "))
numo = ['Even' for x in new_mystring if x.__len__() % 2 == 0 ]
print(numo) #['Even', 'Even', 'Even', 'Even', 'Even', 'Even', 'Even', 'Even', 'Even']

#2nd solution
for word in mystring.split():
    if len(word) % 2 == 0:
        print(word + ' is even')


#5- Write a program that prints the integers from 1 to 100. But for multiples of three print 'Fizz'
#instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both
# 3 and 5 print 'FizzBuzz'
for num in range(1,101):
    if num % 3 == 0:
        print('Fizz')
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
#2nd solution
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


#6-Use List comprehension to create a list of the first letters of every word in the string below
st = 'Create a list of the first letters of every word in this string'
my_string =[x[0] for x in st.split(" ")]
print(my_string)


