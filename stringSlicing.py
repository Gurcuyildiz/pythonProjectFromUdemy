mystring = "abcdefghijk"

#from index 2 till the end
mystring[2:]

#from beginning till index 3 but not including the char in index 3
mystring[:3]

#from index 3 till index 6 but not including 6th characher
mystring[3:6]

#all the way from beginning to end
#abcdefghijk
mystring[::]

#skipping one and taking the other
#abcdefghijk
mystring[::2]# means acegik will be taken bdfhj will be ommited

#skipping each two then including one
#abcdefghijk
mystring[::3] #means adgj

#start from index 2 till index 7 by skipping one of each
#abcdefghijk
mystring[2:7:2] #ceg

#reverse your string
#abcdefghijk
mystring[::-1]#kjihgfedcba
