
##Sets are unordered collections of UNIQUE element
#THere can be only one of same object

my_set = set()
print(my_set)#set() => emtpy set
my_set.add(1)
print(my_set)#{1}
my_set.add(2)
print(my_set)#{1, 2}
#if you add the same number, it will ignore
my_set.add(2)
print(my_set)#{1, 2}

###Casting a list into a set
myList = [1,1,1,2,3,3,3,2,2,1,2]
print(set(myList))#{1, 2, 3}
