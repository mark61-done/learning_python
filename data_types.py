#String data type

#literal assignment
first = 'Marko'
last = 'Oloo'

print(type(first))
print(type(first)==str)
print(isinstance(first, str))

#constructor function
pizza = str('peperoni')
print(type(pizza))
print(type(pizza)==str)
print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I like rock music from the ' + decade + 's. '
print(statement)

# Multiple lines
multiline = '''
Hey how are you?  

I was just checking in.  

                        All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\nWhere\'s this at\\located'
print(sentence)

# String methods
print(first)
print(first.lower()) #.lower() method is used to chenge the whole sentence to be at lower case.
print(first.upper()) #.upper() method is used to chenge the whole sentence to be at upper case.
print(first)

print(multiline.title()) #.title() method is used to change the first letter of every word to upper case.
print(multiline.replace('good','ok')) #.replace() method is used to replace a certain word with another word.
print(multiline)

print(len(multiline))
multiline += "                               "
multiline = "                   " + multiline
print(len(multiline)) #len() method is used to check the length of a string.
print(len(multiline.strip())) #.strip() method is used to remove white spaces.
print(len(multiline.lstrip())) #.lstrip() method is used to remove white spaces from the left side.
print(len(multiline.rstrip())) #.rstrip() method is used to remove white spaces from the right side.

print(" ")

#Build a menu
title = "menu".upper()
print(title.center(20, "=")) #This centers our value and the = sign covers space in both left and right (not the 20 means 20 characters)
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$2".rjust(4))
print("Cheesecake".ljust(16, '.') + "$4".rjust(4))

print("")

#some methods return boolean data
print(first.startswith("M")) # This will return true because it is true that the value of the variable (first) it starts with letter M.
print(first.startswith("Z")) # This will return false because it is true that the value of the variable (first) it does not end with letter Z.

#Boolean data type
myvalue = True
x = bool(False) #this is a constractor function
print(type(x))
print(isinstance(myvalue, bool))

print("")

#Numeric data types

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.4)
print(type(gpa))
print(isinstance(y, float))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built-in function for numbers
print(abs(gpa))

print(round(gpa))

print(round(gpa, 1))

import math #this import should be on top of the file but ill just be using it here for practise purposes

print(math.pi) #this checks the pi
print(math.sqrt(64)) #this checks the square root
print(math.ceil(gpa)) #this rounds up to the nearest integer
print(math.floor(gpa)) #this rounds down to the nearest integer

#casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#You can get an error if you attempt to cast incorrect data
# zip_value = int("New York")