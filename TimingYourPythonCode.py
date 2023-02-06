'''
  Sometimes it's important to know how long your code is taking to run,
   or at least know if a particular line of code is slowing down your entire project.
   Python has a built-in timing module to do this.
'''





#func_one and func_two is doing th same function
def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def func_two(n):
    return list(map(str,range(n)))

print(func_two(10))#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


#ww can see the differences by timing
import time

#current time before
start_time = time.time()

#run code
result = func_one(10000000)

#current time after running code
end_time = time.time()

#elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)#0.0009133815765380859 for func_one



#current time before
start_time = time.time()

#run code
result = func_two(10000000)

#current time after running code
end_time = time.time()

#elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)#0.0010352134704589844


################## TIMEIT MODuLE   #################
import timeit

stmt = '''
 func_one(100)
'''

#set up is called once before code runs
setup = '''
  def func_one(n):
    return [str(num) for num in range(n)]
'''
#this function takes a statement which should be a string, and a startup which should be string as well
#then an integer for how many times to be run
# if number is larger it will take more time to run
print(timeit.timeit(stmt,setup,number=100))



#same running for func_two to see the result of time after running code
stmt2 = '''
 func_two(100)
'''

#set up is called once before code runs
setup2 = '''
  def func_two(n):
    return list(map(str,range(n)))
'''
timeit.timeit(stmt2,setup2,number=10)