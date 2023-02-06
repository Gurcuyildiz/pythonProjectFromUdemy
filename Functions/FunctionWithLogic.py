

print(20%20)
print(20 % 20 == 0)#True

def even_check(number):
    return number % 2 == 0


even_check(20) #no printing here dunnow why
print(even_check(21))#False

#return true if any number is even inside the list
def chech_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass# means don't do aynthing
        #  return False => is wrong to put here false statement as it will only check the first element only
        # if we still want to put 'return False' we need to put in for loop level
    return False

print(chech_even_list([1,3,5,7]))#None after putting return false in lop level we will get false here instead None
print(chech_even_list([1,2,3,4,5]))#True
print(chech_even_list([1,1,1,2]))#True


# Return all the even numbers in a list
even_numbers = [] #placeholder variables
 # for number in chech_even_list():
 #     if number % 2 == 0:
 #         even_numbers.append(number)
 #     else:
 #         pass
 #  return even_numbers






