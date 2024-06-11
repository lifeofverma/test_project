#file is a container in a comupter system for storing data , data is permanently stored
#type of files text and binary

f = open("License free.txt") #open a file

print (type (f)) #type of the varable

print (f.closed) #cheack if file is closed

print (f.read()) #to read the file

f.close() #close the file

print (f.closed) #cheack if file is closed return boolean


#modes of opening a file

'''
'r' : read only
'w' : write only
'a' : appending data at the end of file
'wt' : write text
'wb' : write binary
'rb' : read binary
'rt' : read text
'''

f = open("License free.txt" , "w") #w stands for to open the file in write mode , r stands for read mode
f.write("I am writable")

#with open this is basically will close your file automatically if you forget no memory consumption will happen

with open ("License free.txt") as f : #f= open it is like that
    print (f.read())

print (f.closed)

with open("License free.txt" , "w") as f :
    f.write ("I am the best")


#creating a new file here and w is working as write mode

with open ("new.txt" , "w" ) as f:
    f.write("I am the new file")

with open ("new.txt" , "w" ) as f:
    f.write("I am updated \n"  )
    f.write("I am new line")


#reading a data from file
with open("new.txt" , "r" ) as f:
    data = f.read()
    print (data)

#reading first 4 characters
with open("new.txt" , "r" ) as f:
    data = f.read(4)
    print (data)

    #tell where your pointer is now after it goes upto 4
    print (f.tell())

    #reset your file handler

    f.seek(1) #my pointer will be now on 1


#binary files
with open("test.jpg" , "rb") as f:
    data = f.read()
    

    with open("new.jpg" , "wb") as d:
        d.write()
        
with open("new.jpg" , "rb") as bew:
    read_data = bew.read()

print(read_data)

    

#append method
with open ("new.txt" , "a" ) as f:
    f.write ("this is appended data")


print()
