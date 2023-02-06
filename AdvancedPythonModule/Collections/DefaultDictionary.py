from collections import defaultdict
#let's first check what happens with normal dictionary
d ={ 'a': 10}
#printing all list
print(d)#{'a': 10}
#passing key here, will get value of that key
print(d['a'])#10

# if I call wrong key, will give me error saying hey there is no such key named wrong in the d dictionary
#print(d['wrong']) #KeyError: 'wrong'

# but with defaultdictionary if you pass this wrong key value, it will assign a nul value to it
#ho to create a default dictionary
d = defaultdict(lambda : 0)# we are passing lambda expression with default value of zero, means we want all default
#value to be zero

#correct as key doesnt exist in d dictionary, we are inserting
d['correct'] = 100
print(d['correct'])#100

#in normal dictionary, it will give error but this one will not give error as it is defaultdict instead it will give 0
print(d['wrong key'])#0
