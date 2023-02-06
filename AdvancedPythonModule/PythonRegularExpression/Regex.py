
'''
   Regular Expressions (sometimes called regex for short) allows a user to search for strings
   using almost any sort of rule they can come up. For example, finding all capital letters in a string,
   or finding a phone number in a document.

   Regular expressions are notorious for their seemingly strange syntax.
   This strange syntax is a byproduct of their flexibility.
   Regular expressions have to be able to filter out any string pattern you can imagine,
    which is why they have a complex string pattern format.

    Phone Num :(555)-555-5555
    Regex Pattern : r"(\d{3})-\d{3}-\d{4}


'''
text = "The person's phone number is 408-555-1234. Call soon!"

print('phone' in text) # True

#importing regular expersion module
import re

pattern = 'phone'

#this tell us phone does exist in text and also gives index of it inside the span: starting at index 13 ends at index 18
print(re.search(pattern,text))#<re.Match object; span=(13, 18), match='phone'>


pattern = "NOT IN TEXT"
#we are getting none as there is no match
print(re.search(pattern,text))#None


pattern = 'phone'

match = re.search(pattern,text)
print(match.span())#(13, 18) this will give start  and end index of the word

print(match.start())

print(match.end())


######################
#But what if the pattern occurs more than once?
text = "my phone is a new phone"
match = re.search("phone",text)
print(match.span())

#############
#Notice it only matches the first instance. If we wanted a list of all matches, we can use .findall() method:
matches = re.findall("phone",text)
print(matches)# gives all maches
print(len(matches))# gives how many are there matches


#######
#To get actual match objects, use the iterator:
for match in re.finditer("phone",text):
    print(match.span())



#####
#If you wanted the actual text that matched, you can use the .group() method.
match.group()
