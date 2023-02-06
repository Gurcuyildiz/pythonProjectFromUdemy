
stock_prices = [('Apple',200),('Google', 400),('Microsoft',100)]

for item in stock_prices:#loop through and access the tuples element in a list
    print(item)
# ('Apple', 200)
# ('Google', 400)
# ('Microsoft', 100)


for ticker, price in stock_prices:
     print(price + (0.1 * price))
#we are checking what pric look like with 10 percentage
# 220.0
# 440.0
# 110.0

#checking who is working the max hour
work_hours = [('Abbey', 100), ('Billy',400),('Cassie',800)]
def employ_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)

print(employ_check(work_hours))#('Cassie', 800)

# we can assing the function to a result variable
result = employ_check(work_hours)
print(result)
#it will be tuple
# ('Cassie', 800)
# ('Cassie', 800)

# or we can assign each tuple element to a variable with tuple unpacking
name, hours =employ_check(work_hours)
print(name)# this will give me Cassie
print(hours)#this will give me 800

# if we are not sure how many item are there in a tuple when assigning, first  assign into a sinle varible
#see the result then assign each elemnt to different variable

