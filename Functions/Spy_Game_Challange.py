
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True it doesnt have to be in consecutive
#  spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(liste):
    code = [0, 0, 7, 'x']
    for num in liste:
        if num == code[0]:
            code.pop(0) # code.remove(num) also works

    return len(code) ==1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))


################ COUNT PRIME  #################

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
def count_primes(num):
    if num < 2 :
        return 0
    primes = [2]
    x = 3


#if you like the challenging problems go to this website

#https://projecteuler.net/about
