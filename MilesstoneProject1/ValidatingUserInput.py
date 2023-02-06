

def user_choice():
    #variables
    #initial
    choice = 'WRONG'
    acceptable_range =range(0,10)
    within_range = False

    ##Two conditions to check
    #digit or within_range ==False
    while choice.isdigit() == False or within_range == False:#we will keep asking till choice becomes True,
# means till user put a value you expect, that while line will keep asking if one of the condition is False
          choice = input("Please enter a number (0-10) ")
    #we can put an error mesage for user to inform
          #This is digit check
          if choice.isdigit() == False:
               print('Sorry that is not a digit')

          #Range check
          if choice.isdigit() in acceptable_range:
              within_range =True
          else:
              print("sorry, you are out of acceptable range (0-10)")
              within_range =False
    return int(choice)
#we dont know if the user will enter 0 to 10, what if it will be above
print(user_choice())






'''Arastir asagidaki basliklari
1- How can I check if a string represents an int, without using try/catch?
2- How to check if a string 
 3- python check if input is number'''

some_value = '100'
print(some_value.isdigit())#True
print(int(some_value))#100

result = 'WRONG'
acceptablrvalues = [1,2,3]
print(result in acceptablrvalues)#False
print(result not in acceptablrvalues)#True