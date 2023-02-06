
'''
 Working with CSV Files
Welcome back! Let's discuss how to work with CSV files in Python.
A file with the CSV file extension is a Comma Separated Values file.
 All CSV files are plain text, contain alphanumeric characters, and structure the data contained within them in a tabular form.
  Don't confuse Excel Files with csv files, while csv files are formatted very similarly to excel files,
  they don't have data types for their values, they are all strings with no font or color.
   They also don't have worksheets the way an excel file does.
    Python does have several libraries for working with Excel files, you can check them out here and here.

Files in the CSV format are generally used to exchange data,
usually when there's a large amount, between different applications.
Database programs, analytical software, and other applications that store massive amounts of information
(like contacts and customer data), will usually support the CSV format.

Let's explore how we can open a csv file with Python's built-in csv library.
'''

import csv
# open file,
data = open('examole.csv',encoding='utf-8')

 #csv.reader, convert it into csv data
csv_data = csv.reader(data)

 #reformat it into a python object list of lists
# Cast to a list will give an error, note the can't decode line in the error,
# this is a giveaway that we have an encoding problem!
data_lines = list(csv_data)
#
# Encoding
# Often csv files may contain characters that you can't interpret with standard python,
# this could be something like an @ symbol, or even foreign characters.
# Let's view an example of this sort of error (its pretty common, so its important to go over).


print(data_lines[0])# will give me first line in a list
print(len(data_lines))# will give how many lines are there
print(data_lines[10][3])# will give me the third element in line 10

all_email = []

for line in data_lines[1:]:
    all_email.append(line[3])


full_name = []

for line in data_lines[1:]:
    full_name.append(line[1]+ ' '+ line[2])


file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output,delimiter='')

print(csv_writer.writerow(['a','b','c']))

print(csv_writer.writerow([['1','2','3'],['4','5','6']]))

#to close thr file
file_to_output.close()

# if we dont want to overwrite the file but append something
#opening the file in append mode and add new line with emtpy string
f =open('to_save_file.csv', mode='a', newline='')
csv_writer =csv.writer(f)
csv_writer.writerow(['1','2','3'])# will write those num
f.close()# will close the file
