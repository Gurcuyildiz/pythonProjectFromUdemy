

#
s = 'Hello word'
print(s.capitalize())
print(s.lower())
print(s.upper())

#how many times are there o letter
print(s.count('o'))

#to find index of o
print(s.find('o'))#4

#center the hello word between z letter with 20 length
print(s.center(20,'z'))#zzzzhello wordzzzzz

#will function as tab
print('hello\thi'.expandtabs())#hello   hi

#if it is alpha numeric
print(s.isalpha())
#if it is
print(s.isalnum())

print(s.isspace())

print(s.istitle())

print(s.isupper())

print(s.endswith('o'))

print(s[-1:] == '0')



##############  Regular Expresion ########
#will split in every instance
print(s.split('e'))#['H', 'llo word']

s1= 'hiihiiihhhhiiihihih'
print(s1.split('i'))#['h', '', 'h', '', '', 'hhhh', '', '', 'h', 'h', 'h']

#will split only for the first instance
print(s1.partition('i'))#('h', 'i', 'ihiiihhhhiiihihih')