
#Problem 1: Convert 1024 to binary and hexadecimal representation

print(hex(1024))


#Problem 2: Round 5.23222 to two decimal places
print(round(5.23222,2))


#Problem 3: Check if every letter in the string s is lower case
s = 'hello'
print([x.islower() for x in s])#[True, True, True, True, True]



#Problem 4: How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))#12



#Problem 5: Find the elements in set1 that are not in set2:
set1 = {1,2,3,5}
set2 = {1,2,4}
print(set1.difference(set2))#{3, 5}




#Problem 6: Find all elements that are in either set:
print(set1.union(set2))#{1, 2, 3, 4, 5}




#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.

print({x: x**3 for x in range(5) })#{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}




#Problem 8: Reverse the list below:
list1 = [1,2,3,4]
list1.reverse()
print(list1)#[4, 3, 2, 1]


#Problem 9: Sort the list below:
list1.sort()
print(list1)#[1, 2, 3, 4]