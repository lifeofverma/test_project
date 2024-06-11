#finding encoding scheme of chracters. what are the values associated with the characters
'''   
print (ord ("A"))
print (chr (65))
'''

#indexing in string, accessing character through indexing

'''
name = "Aman Verma"
print (name [3])
print (len (name))
'''

#String slicing
'''
name = "Aman Verma"
print (name [0:5])
'''

#we can use jump as well for example [1 : 3 : 1] here 1 is start 3 is end and 1 is jump

'''
string methods

capitalize
title
upper
lower
find
count
index
replace
spilit
islower
isupper
isnumeric
isalpha


'''

name = "aman verma"
name1 = "AMAN VERMA"

print (name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.islower())
print(name.isupper())
print(name.find("m")) #this is gonna find the index for you
print(name.count("a")) #this is gonna count the number of particular alphabet how many are there
print(name.replace("a" , "A"))
print(name.split())
print(name.split("a"))
print(name.isnumeric())
print(name.isalpha()) 
print(name.index("v"))



'''
#string formating

name = "aman"
age = 36

print ("hey my name is " , name , "my age is " , age )

print ("hey my name is {} ,  my age is {}" .format(name , age))
print (f"hey my name is {name} ,  my age is {age}")

#string concatenation

print ("2" + "a")
print (2 * "a")
'''


