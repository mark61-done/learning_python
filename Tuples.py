#Tuples are much like list but now the data in tuples does not change and the order the data is in will not change.

mytuple = tuple(("Mark", 100, True)) #Here we have created a tuple with a constactor.

anothertuple = (1,2,3,4,1,1) #Here we have created a tuple without a constractor also this is called packing a tuple


print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

#We should keep in mind that tuple can not change which means you can not add something inside a tuple.
#But now here is a way you can add something in a tuple using list.
newlist = list(mytuple)
newlist.append("John")
newtuple = tuple(newlist)
print(newtuple)

#As we assign value to a tuple also called packing a tuple just like we did using the variable anothertuple we can also unpack a tuple and we can unpack it to new variable names
(one, two, *hey) = anothertuple
print(one) #this will print (1) as it was the first value in our tuple anothertuple = (1,2,3,4) 
print(two) #this will print 2
print(hey) #this will print a list of [3,4]

#we only have two methods on tuples and they are .count() and .index()

print(anothertuple.count(1)) #This will count the number of times 1 has repeated in our tuple

print(mytuple.index("Mark")) #This will check the index of Mark in the tuple and in this case it will print 0 bacause Mark is at index 0


