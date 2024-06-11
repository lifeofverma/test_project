'''while something is true
i = 1

while i <= 10 :
    print (i)
    i += 1
'''



'''range function allows users to geneerate series of number
it is iterable as well
range()
start, end, jump (these are the 3 parameter range func asks)
'''

'''
n = 5
print (range(n))
print (list(range(n)))
print (list(range( 1, 5) )) #here I have assinged start and end parameter so first parameter is called start and last is called as end, and at the end basically it is going to end
print (list(range( 1, 20 , 2) )) # same comment as above same functioning but the last number here is defininf the jump parameter works with -2 as well
'''

'''iterator, iterable and iteration'''

'''
table = 5

for i in range (1 , 11) :
    print (i* table)
'''

#unnested for loop printing pattern for simply understanding the for loop inside the for loop
'''
for i in range (4):
    for i in range (4):
        print ("#" , end = " ")
    print ()
'''

'''
#break
for i in range (1, 10):
    if i == 5 :
        break
    print (i)
'''

'''
#pass
for i in range (1, 10):
    if i == 4
        pass 

#now if we going to run this code we will see a error which is a syntax error so that pass statement is not covering it but pass statement will pass on once the logical error is there
'''


'''
#continue
for i in range (1, 10):
    if i == 5:
        continue
    print (i)

'''


