

#
d = {'k1': 1, 'k2': 2}
print(d.values())
print(d.items())


# this is list comprehension
print({x:x**2 for x in range(10)})#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#dictionary comprehension
print({k:v**2 for k,v in zip(['a','b'],range(2))})#{'a': 0, 'b': 1}


#dictinary can be iterated through their iter function

#itering value
for k in d.itervalues():#itervalues jupiterbotebook ta calisiyor bur da yok
    print(k)

#itering items
for x in d.iterkeys():#jupiterbotebook ta calisiyor bur da yok
    print(x)


