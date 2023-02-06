
list1 = [1,2,3]


list1.append(4)

list1.count(10)


x = [1, 2, 3]
x.append([4, 5])# add the entire element as a list to the list
print(x)#[1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5])# adding the entire element to the list individually
print(x)#[1, 2, 3, 4, 5]


print(list1.index(2))#1


# Place a letter at the index 2
#accept two argument, object and element index
list1.insert(2,'inserted')
print(list1)#[1, 2, 'inserted', 3, 4]


#by defult remove the last element
ele = list1.pop(1)  # pop the second element
print(ele)#2

list1.remove('inserted')
print(list1)#[1, 3, 4]


l = [1,2,3,4,3]
print(l.remove(3))#will remove the first occurance

print(l.sort())