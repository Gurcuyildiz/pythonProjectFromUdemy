
'''1- Write a function that checks whether a number is in a given range (inclusive of high and low)'''
import StringDataType

# def ran_check(num, low, high):
#     return f'{num} is the range between {low} and {high}'
#
# print(ran_check(5,2,7))

#2nd way
def run_check(num, low, high):
    return num in range(low, high+1)



'''2- Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()
If you feel ambitious, explore the Collections module to solve this problem!'''

# def up_low(mystring):
#     countup = 0
#     countdown = 0
#     for letter in mystring:
#         if letter.isupper():
#         #there is no increment /decrement operator in python like ++,--, instead we use below one
#             countup =countup+1
#         elif letter.islower():
#             countdown = countdown+1
#         else:
#             pass
#
#     print(f'No. of lower case chars : {countdown}')
#     print(f'No of upper case chars : {countup}')
#
# print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

#2nd way with dictionary
def uplow(senten):
    #instead of two variable we put those variable into a dictionary
    d = {'upper':0, 'lower': 0}
    for c in senten:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", senten)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])



'''3- Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''
# def unique_list(liste):
#     return list(set(liste))
#
# print(unique_list([1,2,3,3,2,1,4,4]))

#2nd way
def uniqe(lst):
    seen_num = []
    for num in lst:
        if num not in seen_num:
            seen_num.append(num)
    return seen_num


'''4- Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24'''
def multiply_list(mylist):
    new_value = 1
    for num in mylist:
        new_value = new_value * num
        print(new_value)
    return new_value

print(multiply_list([1,2,3,-4]))


'''5- Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
 e.g., madam,kayak,racecar, or a phrase "nurses run". 
 Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
 Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.'''
def palindrome(word):# this works without space
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome('helleh'))

def palondromee(s):
    s = s.replace(' ',  '')
    return s == s[::-1]




'''6- Write a Python function to check whether a string is pangram or not. 
(Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons'''
import StringDataType
def ispangram(str1,  alphabet=string.ascii_lowercase):
    for char in str1:
        #Create a set of entire alphabet
        alphaset = set(alphabet)

        # Remove th spaces from the input
        str1 = str1.replace(' ', '')

        #Convert into all lowercase
        str1 = str1.lower()

        #Grab all unique letters from the string set()
        str1 = set(str1)

        #alphabet set == string set input
        return str1 == alphaset

