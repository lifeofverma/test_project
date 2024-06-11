'''
dictionary has key value pair form of data
dict are ordered
does not support indexing
data can be accesses using key
'''

d = {}
print (type(d))

d = dict()
print (type(d))

fruits = {
    "banana" : 20 , "mango" :  433 , "apple" : 54
}

print (fruits)

#zip method

name = ["apple" , "mango" , "oranges"]
price = [ 120, 432 , 321]

fruit = dict(zip(name, price))

print (fruit)

#accessing elements in dict

print (fruits ["apple"])

print(fruit.get("apple"))

#updating dict

fruit["apple"] = {"small" : 90 , "large" : 675}
print (fruit)
       
fruit["guava"] = 54

print (fruit)

#now update with multiple values

new = {"grapes" :120 , "pineaaple" : 45 , "blueberry" : 76}

fruit.update(new)

print(fruit)

#deleting data pop, popitem, del

print(fruit)
print("apple" in fruit) #cheack if object is there in the dict

fruit.pop("apple") #remove the selected item
print (fruit)

fruit.popitem()
print (fruit) #remove the last item in the dict


del fruits #whole dict is deleted

print(fruit)

#for i in fruit:
#    print (i)

'''
for i in fruit:
    print (i, fruit[i]) did't get it


for key, value in fruit.items():
    print (key, value)
'''

#dict methods key, values, items
"""
{
    'mango': 432, 
    'oranges': 321, 
    'guava': 54, 
    'grapes': 120, 
    'pineaaple': 45
}
"""


print("-----------------------")
print(fruit)
print(fruit["mango"])

print(fruit.get("mango"))
print(fruit.get("oranges"))
print(fruit.get("guava"))
print(fruit.get("grapes"))
print(fruit.get("pineaaple"))

print("-----------------------")
for each in fruit:
    print(fruit.get(each))

# for i in fruit:
#     print(fruit[i])


















