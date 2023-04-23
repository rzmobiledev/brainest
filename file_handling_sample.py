# file handling
'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists 
'''

'''
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images) 
'''

f = open("demofile.txt")
print(f)

f = open("demofile.txt", "rt")

# read files
f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("romeo.txt", "r")
print(f.readline())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# write/create files
'''
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content 
'''

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

''' 
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist 
'''

# delete files
import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.mkdir("myfolder")


