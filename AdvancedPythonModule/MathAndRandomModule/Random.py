import random
#by passing 0 to 100, it will give us a random umber between those two number
#each time when you run the same code it will give different result
print(random.randint(0,100))


'''
  Setting a seed allows us to start from a seeded psuedorandom number generator,
   which means the same random numbers will show up in a series. Note, you need the seed to be in the same cell
    if your using jupyter to guarantee the same results each time.
     Getting a same set of random numbers can be important in situations where you will be trying different variations of functions and want to compare their performance on random values, but want to do it fairly (so you need the same set of random numbers each time).
'''
#if you put the seed and raninit at the same cell then you will receive the same result each time run contrary to above
print(random.seed(101),random.randint(0,100))# 74, it will always give 74


# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)# as I set the seed, the following will give same result
print(random.randint(0,100))#74
print(random.randint(0,100))#24
print(random.randint(0,100))#69
print(random.randint(0,100))#45
print(random.randint(0,100))#59


#Grab a random item from a list

mylist = list(range(0,20))
print(mylist)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(random.choice(mylist))#1

print(mylist)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


'''
 Sample with Replacement
 Take a sample size, allowing picking elements more than once.
  Imagine a bag of numbered lottery balls, you reach in to grab a random lotto ball, 
  then after marking down the number, you place it back in the bag, then continue picking another one.
'''
print(random.choices(population=mylist,k=10))# there can be duplicated number
#[13, 4, 4, 5, 13, 4, 19, 1, 3, 1]



'''
  Sample without Replacement
Once an item has been randomly picked, it can't be picked again. 
Imagine a bag of numbered lottery balls, you reach in to grab a random lotto ball, 
then after marking down the number, you leave it out of the bag, then continue picking another one.
'''
print(random.sample(population=mylist, k=10))
#[17, 11, 6, 15, 10, 3, 16, 12, 19, 18]

random.shuffle(mylist)
print(mylist)#[18, 8, 0, 11, 17, 16, 7, 19, 4, 5, 12, 15, 10, 1, 3, 9, 14, 13, 2, 6]


#will pick any number between a and b, not just integer, it can be any number double floating
print(random.uniform(a=0, b=100))#74.44690143237648

