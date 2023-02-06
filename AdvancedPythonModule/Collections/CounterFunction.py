from collections import Counter
mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4]
#i want to see how many 1s how many 2s ... blabla there
print(Counter(mylist))#Counter({3: 8, 4: 5, 1: 4, 2: 4}) means there are 8 of 3, ..etc
#key is the object, value is the counter

#mixed one
mylist = ['a','a', 'a',10,10,10]
print(Counter(mylist))#Counter({'a': 3, 10: 3})

#can pass a string, will count each individual char in string
print(Counter('aaabbbbcccccddddeeeeggg'))#Counter({'c': 5, 'b': 4, 'd': 4, 'e': 4, 'a': 3, 'g': 3})

#for a long sentence to find a word occurance times
#first split the sentence int oa list
sentece = 'How many times does each word appear in this sentence with word'
print(Counter(sentece.split()))# if nothing specified, it will split based on the space
#Counter({'word': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'appear': 1, 'in': 1, 'this': 1, 'sentence': 1, 'with': 1})


letter = 'aaabbbbccccddddeee'
c= Counter(letter)
print(c)#Counter({'b': 4, 'c': 4, 'd': 4, 'a': 3, 'e': 3})

#this will give in order which one has most occurance from most to least
print(Counter(c.most_common()))
#Counter({('b', 4): 1, ('c', 4): 1, ('d', 4): 1, ('a', 3): 1, ('e', 3): 1})

print(Counter(c.most_common(3)))#en fazla tekrar edenden 3 tane goster
#Counter({('b', 4): 1, ('c', 4): 1, ('d', 4): 1})
print(Counter(c.most_common(2)))#en fazla tekrar edenden 2 tane goster
#Counter({('b', 4): 1, ('c', 4): 1})
print(Counter(c.most_common(1)))#en fazla tekrar edenden bir tane goster
#Counter({('b', 4): 1})



'''

  Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
print(list(c))#['a', 'b', 'c', 'd', 'e'], list is giving unique value of element