
#1-LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a<b:
            return a
        elif b<a :
            return b
    elif a % 2 != 0 or b % 2 != 0:
        if a > b :
            return a
        elif b> a:
            return b

#2nd way
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))#2
print(lesser_of_two_evens(2,5))#5


#2- ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def animalcrakers(mystring):
    #first I need to grab the word by spliting them into a list
    wordlist = mystring.split()
    print(type(wordlist))#list
    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False

#2nd way
def animalcrakers(text):
    wordslist = text.lower().split()
    return wordslist[0][0] == wordslist[1][0]

print(animalcrakers('crazy cangroo'))




#3- MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(a,b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False

#2nd way
def makes_twenty(a,b):
    return (a + b) == 20 or a == 20 or b == 20

print(makes_twenty(3,2))


#4- OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
    firt_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return firt_letter.upper() +in_between +fourth_letter.upper() +rest

#2nd way
def old_macdonald(name):
    #kelimeyi ikiye ayir
    first_half = name[: 3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()



print(old_macdonald('aysegul'))#AysEgul


#5- MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoga(sentence):
    wordlist = sentence.split()
    reversed_list = wordlist[::-1]
    return ' '.join(reversed_list)

print(master_yoga('I am home'))#['home', 'am', 'I']# without join method it return a list
                              #home am I  # with join method



#6-ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n ) <= 10)
#abs is absolute value
print(almost_there(104))#True
print(almost_there(150))#False



#7- Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(nums):
    for a in range(0,len(nums)-1):
        if nums[a] == 3 or nums[a+1] == 3:
            return True
    return False

print(has_33([1,3,3,1]))#True
print(has_33([1,3,1,3]))#True => this should be false but I am receiving true
print(has_33([3,1,3]))#True   => this also should be false but I am receiving true

#2nd way
def has_33(nums):
    for a in range(0,len(nums)-1):
        if nums[a:a+2] == [3,3]:
            return True
    return False
print(has_33([3,1,3]))# false



#8-PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result
print(paper_doll('Hello'))#HHHeeellllllooo



#9- BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a,b,c):
    if a+b+c <=21:
        return a+b+c
    elif a+b+c>21 and (a == 11 or b == 11 or c == 11):
        result = (a + b + c) - 10
        return result
    else:
        return 'Bust'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

#2nd way
def black_jack(a,b,c):
    if sum([a,b,c]) <=21:
        return sum(([a,b,c]))
    elif 11 in [a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return 'Bust'

print(black_jack(9,9,9))


#10- SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69[2,1,6,9,11])


