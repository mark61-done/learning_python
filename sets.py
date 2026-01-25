#sets
#A set is a collection which is unordered, unchangeable, and unindexed. In Python sets are written with curly brackets.
#Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits) #This will print the set
print(type(fruits)) #This will print the type of the variable fruits which is a set
print(len(fruits)) #This will print the length of the set which is 3 since there are three items in the set

fruits2 = set(("apple", "banana", "cherry")) #Here we have created a set with a constructor.
print(fruits2) #This will print the set
print(type(fruits2)) #This will print the type of the variable fruits2 which is a set

#Access items in a set
for fruit in fruits:
    print(fruit) #This will print each item in the set

#Check if item exists in a set
print("banana" in fruits) #This will return true since banana is in the set
print("orange" in fruits) #This will return false since orange is not in the set

#Adding items to a set
fruits.add("orange") #This will add orange to the set
print(fruits)
fruits.update(["mango", "grape"]) #This will add multiple items to the set
print(fruits)

#Removing items from a set
fruits.remove("banana") #This will remove banana from the set, if banana is not found it will raise a KeyError
print(fruits)
fruits.discard("kiwi") #This will remove kiwi from the set if it exists, if not it will do nothing
print(fruits)
fruits.pop() #This will remove and return an arbitrary item from the set
print(fruits)
fruits.clear() #This will empty the set
print(fruits)
del fruits2 #This will delete the entire set fruits2
# print(fruits2) #This will raise an error since fruits2 has been deleted

#Set operations
setA = {"apple", "banana", "cherry"}
setB = {"cherry", "date", "fig"}
#Union
setC = setA.union(setB) #This will return a new set with all items from both sets
print(setC)
#Intersection
setD = setA.intersection(setB) #This will return a new set with only the items that are present in both sets
print(setD)
#Difference
setE = setA.difference(setB) #This will return a new set with items that are in setA but not in setB
print(setE)
#Symmetric Difference
setF = setA.symmetric_difference(setB) #This will return a new set with items that are in either setA or setB but not in both
print(setF)
#Subset
print(setD.issubset(setA)) #This will return true since setD is a subset of setA
#Superset
print(setA.issuperset(setD)) #This will return true since setA is a superset of setD    
#Disjoint
setG = {"kiwi", "mango"}
print(setA.isdisjoint(setG)) #This will return true since setA and setG have no items in common

#Copying a set
setH = setA.copy() #This will create a copy of setA
print(setH)

#note: sets do not allow duplicate values
setI = {"apple", "banana", "apple", "cherry"} #Here apple is duplicated
print(setI) #This will print {'apple', 'banana', 'cherry'} without duplicates

#note: sets are unordered, so the items may appear in a different order each time you print the set
#note: sets are unindexed, so you cannot access items in a set by index
#note: sets are mutable, so you can add or remove items from a set
#note: sets can only contain immutable (hashable) items, so you cannot have a list or dictionary as an item in a set
#However, you can have tuples as items in a set since tuples are immutable
setJ = {("apple", 1), ("banana", 2)} #Here we have tuples as items in the set
print(setJ)
#You can also have frozensets as items in a set since frozensets are immutable
frozenSet1 = frozenset({"cherry", "date"})
setK = {frozenSet1, frozenset({"fig", "grape"})} #Here we have frozensets as items in the set
print(setK)
#You cannot have a set as an item in a set since sets are mutable
#setL = {{ "apple", "banana" }} #This will raise a TypeError since sets are unhashable
#print(setL)
#True is considered as 1 and False is considered as 0 in sets
setM = {1, 2, True, False} #Here True is considered as 1 and False is considered as 0
print(setM) #This will print {0, 1, 2} without duplicates
#You can use various data types as items in a set
setN = {"apple", 1, 3.14, (1, 2), frozenset({"banana", "cherry"})}
print(setN)


#frozenset
#A frozenset is an immutable version of a set, meaning its items cannot be changed
frozenSet = frozenset({"apple", "banana", "cherry"})
print(frozenSet)
print(type(frozenSet)) #This will print the type of frozenSet which is frozenset
#frozenSet.add("orange") #This will raise an AttributeError since frozensets are immutable
#frozenSet.remove("banana") #This will also raise an AttributeError since frozensets are immutable

#You can perform set operations on frozensets just like regular sets
frozenSet2 = frozenset({"cherry", "date", "fig"})
frozenSetUnion = frozenSet.union(frozenSet2)
print(frozenSetUnion) #This will print the union of the two frozensets
frozenSetIntersection = frozenSet.intersection(frozenSet2)
print(frozenSetIntersection) #This will print the intersection between the two frozensets
frozenSetDifference = frozenSet.difference(frozenSet2)
print(frozenSetDifference) #This will print the difference between the two frozensets
frozenSetSymDiff = frozenSet.symmetric_difference(frozenSet2)
print(frozenSetSymDiff) #This will print the symmetric difference between the two frozensets
