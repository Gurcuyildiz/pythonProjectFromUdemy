
#dictionaries are unordered mapping for storing object
#dictionary uses key and value pair object
#object are retrieved by key name and they cant be sorted

#difference between key and list is list object is retrieved by index(location) and ordered sequence can be
#indexed or sliced

my_dictionary = {
    'key1': 'value1', 'key2': 'value2'
}
print(my_dictionary['key1'])#value1

price_loopup = {
    'apple': 2.99, 'oranges': 1.99,'milk': 5.80 }
print(price_loopup['milk'])
print(price_loopup['apple'])
print(price_loopup['oranges'])

d = { 'k1':123,'k2':[1,2,3],'k3':{'insideKey': 100 }}
print(d['k2'][2])#3
print(d['k3']['insideKey'])#100

d1= {'key1': ['a','b','c']}
my_list = d1['key1']#we turned it into a list
print(my_list)#['a', 'b', 'c']

letter =my_list[2]#grabbed one of the elemnt
print(letter)#c
print(letter.upper())#C

#####can be done this way to
print(d1['key1'][2].upper())#C

#####Adding a new value to the dictoinary
d2 ={ 'k1':30,'k2':200,}
d2['k3']= 300
print(d2)#{'k1': 30, 'k2': 200, 'k3': 300}

#####Overwrite the existing value
d2['k1']= 566
print(d2)#{'k1': 566, 'k2': 200, 'k3': 300}

######To see all dictionary keys and values
print(d.keys())#dict_keys(['k1', 'k2', 'k3'])

print(d2.values())#dict_values([566, 200, 300])

###To print all items in dic
print(d2.items())#dict_items([('k1', 566), ('k2', 200), ('k3', 300)])