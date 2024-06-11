#lists is a order collection of data. we can add a lot of data inside the list. it is a data structure

l = list()
print (type(l))

l1 = [1 , 2, 3]
print (l1)
print (type(l1))
print (l1[0])

#mutablity

l1[0] = 5
print (l1)
print (id(l1))

for i in l1 :
    print (l1)

#list slicing

x = [1,3,5,7,9,1,1]

print (x [0 : 4])

'''
list operations
count
index
pop
remove
sort
insert
append
extend


'''

print (x.count(1)) #return the count of the object present in the list
print (x.index(1)) #return the index of the object present in the list
print (x.pop()) #delete the last object present in the list
print(x)
print (x.remove(7)) #remove the particular object you will enter
print(x)
print(x.sort()) #this will sort the list 
print (x.insert( 0 , 43))  #this will insert the object you want to, 1st parameter put the index you want to add on and then the object you want to add on
print (x)


print (x.append("aman")) #adds the object in the end of the list
print (x)


aman = ["emma" , "code" , "TD" , "Practice"]

print (x.append(aman))
print (x)

print (x.extend(aman)) #extend the list
print (x)
