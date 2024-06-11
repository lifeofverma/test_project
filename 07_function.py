#function is a user defined piece of code. it works only when its called by user. it helps in reusablity of code and helps in reducing errors in your code. example print , range, etc.
'''
def func() :
    #docstring is a additonal information that you can provide by defining a functions

    print ("aman")


#parameters and arguments

def func(name) : #this is called parameter
    #docstring is a additonal information that you can provide by defining a functions

    print ("how are you", name)

func("aman") #here it is called an argument


def add (a , b):
    c = a + b    
    print (c)

add (2 , 15)
'''
#return statement, print statement does'nt return any type but return() does

'''

def add (a , b):
    c = a + b
    return c

b = add (3, 5 )
print (b, type(b))



#using return after that nothing works in the code
def func():
    print ("hi")
    return "aman"
    print ("i am not working")

func()

#returing multiple values

def intro (name, age, hobby):
    return name  , age, hobby

a, b, c, = intro("aman" , "25" , "coding")
print (a , b, c )


x = intro("aman" , "25" , "coding")
print (x , type(x))

#scope of a variable global and local

a = "aman" #globalvariable

def aman ():
    a = "verma" #local variable
    print (a)

print (a)
aman()


#lambda function

print ((lambda q , w : q + w )(3,4)) 


example = (lambda q , w : q + w )(3,4)

print (example)

def larger (a, b):
    if a > b :
        return a
    else:
        return b
    
r = (lambda e , r : e if e > r else r) (4, 3 )

print (r)

larger(4,3)
'''

#positional arguments

def intro (name , hobby):
    print ("hey my name is " , name )
    print ("hey my hobby is " , hobby)

intro ("aman", "coding") #positional argument you have to give argument as per postition

#default arguments

def intro (name , hobby = "None"):
    print ("hey my name is " , name )
    print ("hey my hobby is " , hobby)

intro ("aman") 

def intro (name , hobby = "Reading"):
    print ("hey my name is " , name )
    print ("hey my hobby is " , hobby)

intro ("aman") 

def intro (name , hobby = "Reading"):
    print ("hey my name is " , name )
    print ("hey my hobby is " , hobby)

intro ("aman" , "gaming") 

#this is how default argument works

#arbitary arguments when number of values you want to pass is not known store the data in tuple format

def test (*args):
    print (args)
    print (args, type(args))
test("aman", 344, 54, 767, 435, 23)


#keyword arguments stores the data in dict format, variable number of key word arguments

def intro (**kwargs):
    print (kwargs)
    print (type(kwargs))


    for key, values in kwargs.items():
        print (key , values, sep =  ":")

intro (name = "aman" , age = 356 , hobbies = ["swimming" , "read" , "cycle"])


def mix (a,b,c, age = 24, *args,**kwargs):
    print (a,b,c)
    print (age)
    print (args)
    print (kwargs)

mix (2,4,5 , 43 , 6,8,5, name = "aman" , hobbie = "swimming")
























































