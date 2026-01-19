users = ["Marko", "Julias", "Mary"]

data = ["Marko", 100, True]

emptylist = []

print("Marko" in users) #This will return boolean data true since it is checking if Marko exists in the list of users.

print(users[0]) #This will print the value in index 0 on the list.

print(users.index('Julias')) #This checks the index of the value in the list.

print(users[0:2]) #This will print Marko and Julias it will not include Mary.

print(users[0:]) #This will print all values in the users list.

print(len(data)) #This will print the length of the list of data.

users.append("Brian") #This will add brian to the users list.
print(users)

users += ["James"] #This will also add James to the users list.
print(users)

users.extend(["Celestine", "Tasha"]) #This is also another method of adding items in a list.
print(users)

users.extend(data) #Here we have passed a existing list in to the users list.
print(users)

users.insert(0, "Bob") #This will insert the name Bob into the list as the first value because it is index 0.
print(users)

users[2:2] = ["Eddie", "Alex"] #This will add eddie on the second position of the users list it wil not replace values
print(users)

users[1:3] = ["Max", "Liam"] #this will replace position 1 and 2 values in the list.
print(users)

users.remove("Bob") #This will remove Bob from the list.
print(users)

users.pop() #This removes the last user in the list
print(users)

del users[-1] #We can also use the del key word to delete a user from the list.
print(users)

# del data # del key word can also be used to delete a complete list this will bring an error since the moment we have printed now the data is not defined because it is deleted
# print(data)

data.clear() #This now will emty the data list not compleatly deleating the data but now the list will be empty but thedata variable will still stand out it will not bring an error because it is not deleated
print (data)

users.sort() #This will sort the list in alphabetical order using the first letter of the list but when their is a word in your list thet is all lowercase, the lowercase word will come last
print(users)

users.sort(key=str.lower) #This will sort the list in alphabetical order using the first letter of the list but when their is a word in your list thet is all lowercase, the lowercase word will come first.
print(users)

nums = [35.6,73,8,83,0,73] #This has reversed our list since our list began with 35.6 and ended with 73 but now it will reverse and start with 73 and end with 35.6
nums.reverse()
print(nums)

# nums.sort() #This will sort the numbers from the smallest to the largest
# print(nums)

# nums.sort(reverse=True) #This will sort the numbers from the largest to the smallest
# print(nums)

print(sorted(nums, reverse=True)) #This is a gloabal aproach or a gloabal function that will sort the list in decending order but now when we will print nums again it will display the original list before it was sorted.

print(nums) #After the gloabal aproach when we print nums now it will go back to how the list was before it was modified with the gloabal aproach






