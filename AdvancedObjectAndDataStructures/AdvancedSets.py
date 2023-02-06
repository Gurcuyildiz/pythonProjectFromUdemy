
#set only accept unique number no duplicate

#first start with building set
s = set()

#add element
s.add(1)
s.add(2)
s.add(2)# thi will not be added

s.clear()# will delete all element


s ={1,2,3}

#will copy the set but the original will stay same
sc = s.copy()

s.add(4)

s.difference(sc)

s2 = {1,2,3}
s3 = {1,4,5}
print(s2.difference_update(s3))

#if this element is exist then will discard it if not then , no changes
print(s.discard(12))


#intersection
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))#{1, 2}


## is this joint ortak ozelligi/element yoksa true verir , varsa False verir
print(s1.isdisjoint(s2))


# if s1 contain s2
print(s1.issubset(s2))

#issubset in tersi
print(s1.issuperset(s2))

#hangi element farkli onu bulur
print(s1.symmetric_difference(s2))


# union => will return union of two set
#her iki set tin butun elementleri birlestiir sadece unique olani alir, no duplicate
print(s.union(s2))


#update
#
