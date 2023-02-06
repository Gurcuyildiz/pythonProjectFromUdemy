
#instead of printing each time
print([1,2,3])
print([4,5,6])
print([7,8,9])
print([10,11,13])

#we can put the same function into a method parameter
#Display info
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
example_row = [1,2,3]
print(display(example_row,example_row,example_row))
'''[1, 2, 3]
   [1, 2, 3]
   [1, 2, 3]'''

#or differentaite parameter
row1 = ['  ',' ',' ']
row2 =['  ',' ',' ']
row3 =['  ',' ',' ']
print(display(row1,row2,row3))
# ['  ', ' ', ' ']
# ['  ', ' ', ' ']
# ['  ', ' ', ' ']

row2[1] = 'X'
print(display(row1,row2,row3))
# ['  ', ' ', ' ']
# ['  ', 'X', ' ']
# ['  ', ' ', ' ']

