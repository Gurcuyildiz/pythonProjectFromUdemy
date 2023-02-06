
#Syntax
#def is telling Python this is a function
#the rest is function name, mostly used snake casing means all lower case with underscore between word
#paranthesis is to pass argument
def name_of_function():
    #multi-line string to describe function with docstring
    print('Hello')

# to run the method, function can called/executed to see the result
name_of_function() # Hello

#one parameterized function created
def name_of_function1(name):
    print('Hello '+ name)

#function was called and executed
name_of_function1('Jose')#Jose


#Return keyword is used to send back the result of the function instead of printing
# Return allow us to assign the output of the function to a new variable
def add_function(num1, num2):
    return num1+num2
result =add_function(1,2)
print(result)#3