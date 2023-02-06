def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]


def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))


import time
# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time



# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time




import timeit

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

stmt = 'func_one(100)'

timeit.timeit(stmt,setup,number=100000)

#Now let try running func_two 10,000 times and compare the length of time it took.

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'
timeit.timeit(stmt2,setup2,number=100000)

#It looks like func_two is more efficient.
# You can specify more number of runs if you want to clarify the different for fast performing functions.

timeit.timeit(stmt,setup,number=1000000)#13.129837899999984
timeit.timeit(stmt2,setup2,number=1000000)#10.894090699999992
