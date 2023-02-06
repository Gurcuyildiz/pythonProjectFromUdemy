

######     MAP   #########
# it expect a function, you pass

def square(num):
    return num**2

my_nums = [1,2,3,4,5]
#one way of iterating over the list is
for item in map(square, my_nums):
    print(item)
#1
# 4
# 9
# 16
# 25

#another way is map
#map apply the square function in each elemnt of my_nums list
print(list(map(square,my_nums))) #[1, 4, 9, 16, 25]

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['andy', 'Sam', 'Rob']
#we dont put method paranthesis when passing function in to map
print(list(map(splicer,names)))#['EVEN', 'S', 'R']


###########   FILTER       ########
#we can put fulter function in to a list
def check_even(num):
     return num %2 == 0

mynums = [1,2,3,4,5,6]

#filter function will filter based on the function(method0 we will pass
print(filter(check_even, mynums))#<filter object at 0x000001BA3F7BBA00>, will not work as didnt transform into a list
print(list(filter(check_even,mynums)))#[2, 4, 6]


#or we can put filter function into a loop
for n in filter(check_even,mynums):
    print(n)
# 2
# 4
# 6
# we will turn the follow in to a function
def square(num):
    result = num **2
    return result
print(square(3))#9



######################     LAMBDA    #######

# this is lamda expression
lambda num: num ** 2
#we can assign to a variable
square1 = lambda num : num ** 2
print(square1(4))#16

#lambda in a filter function then cast into a list
men= list(map(lambda num:num**2, mynums))
print(men)#[1, 4, 9, 16, 25, 36]


#lambda in a filter funtion and cast into a list
women = list(filter(lambda num:num%2==0, mynums))
print(women)#[2, 4, 6]

#grab the first character of the list
print(list(map(lambda x:x[0],names)))#['a', 'S', 'R']
#reverse the list
print(list(map(lambda x:x[::-1],names)))#['ydna', 'maS', 'boR']