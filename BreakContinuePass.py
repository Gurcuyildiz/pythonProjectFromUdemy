
#Break breaks out of the current closest enclosing loop

#Continue goes to the top of the closest enclosing loop

#Pass does nothing at all

x = [1,2,3]
for item in x:
    pass# is used as placeholder not to do aynthing
mystring ='sammy'
for letter in mystring:
    if letter =='a':
       continue
    print(letter)# Smmy

for letter in mystring:
    if letter =='a':
       break
    print(letter)#S

x=0

while x<5:
    if x == 2:
        break
    print(x)
    x =x+1

