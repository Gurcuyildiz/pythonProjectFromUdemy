
''''
   Unzipping and Zipping Files
As you are probably aware, files can be compressed to a zip format.
Often people use special programs on their computer to unzip these files,
luckily for us, Python can do the same task with just a few simple lines of code.

'''

#Create Files to Compress
# slashes may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()


'''
 Zipping Files
The zipfile library is built in to Python, we can use it to compress folders or files.
 To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.
'''
import zipfile
#Create Zip file first , then write to it (the write step compresses the files.)
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()





'''
  Extracting from Zip Files
We can easily extract files with either the extractall() method to get all the files,
 or just using the extract() method to only grab individual files.
'''
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")



'''
  Using shutil library
Often you don't want to extract or archive individual files from a .zip, 
but instead archive everything at once.
The shutil library that is built in to python has easy to use commands for this:
'''
import shutil

#The shutil library can accept a format parameter,
# format is the archive format: one of "zip", "tar", "gztar", "bztar", or "xztar".

#pwd

directory_to_zip='C:\\Users\\Georgia\\ blalbal bal full path pwd ile bul buraya yapistr'

# Creating a zip archive
output_filename = 'example' # bu file adi olusacak path de
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)#
#'C:\\Users\\blabla eksik olan yerler\\example.zip'


# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here

#shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')