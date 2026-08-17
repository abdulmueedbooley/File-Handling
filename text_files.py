#1) WHAT IS FILE HANDLING? 
# File handling allows programs to store data permanently in files such as student records, messages, reoprts and logs

#* 2.) OPENING A FILE 
open('filename.txt', 'mode')

#* 3.) WRITING TO A FILE 
file = open('filename.txt', 'w')
file.write('My name is Abdul - Mueed Booley')
file.close()

#* 4.) READING FROM A FILE 
file = open('filename.txt', 'r')
content = file.read()
print(content)
file.close()

#* 5.) APPENDING A FILE 
file = open('filename.txt', 'a')
file.write('Example')
file.close()

#* NOTE : The difference between WRITE and APPEND 
#* Write adds contents to a file by erasing any existing content on that text file 
#* However APPEND moves the cursor at the end of the file, this results in existing content by not being erased 
# AND if the textfil does not EXIST append will automatically create that 'so-called' file for you 

#* 6.) USING THE WITH STATEMENT 
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
#? make use of the with statement if log files are much smaller
#? this method is quick and convenient when memory isnt a concern 

#* 7.) READING LINE BY LINE
with open('filename.txt', 'r') as file: 
    for line in file: 
        print(line)
#? this method is crucial when working with large multi Gbs textfiles when MEMORY is a CONCERN 

