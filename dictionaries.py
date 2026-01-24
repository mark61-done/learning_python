#Dictionaries
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

#Creating a dictionary
band = {
    "vacals": "plant",
    "guiter": "page"
}

band2 = dict(vocals="plant", guiter="page") #Another way to create a dictionary

print(band) #This will print the dictionary
print(band2) #This will print the dictionary
print(type(band)) #This will print the type of the variable band which is a dictionary
print(len(band)) #This will print the length of the dictionary which is 2 since there are two key value pairs in the dictionary

#Access items in a dictionary
print(band["vacals"]) #This will print plant
print(band.get("guiter")) #This will print page

#list all keys in a dictionary
print(band.keys()) #This will print all the keys in the dictionary

#list all values in a dictionary
print(band.values()) #This will print all the values in the dictionary

#list of keys/value paires as tuples
print(band.items()) #This will print all the key value pairs in the dictionary as tuples

#Check if key exists in a dictionary
print("vacals" in band) #This will return true since vacals is a key in the dictionary band
print("drums" in band) #This will return false since drums is not a key in the dictionary band

#change values in a dictionary
band["vacals"] = "robert plant" #This will change the value of the key vacals to robert plant
print(band)

band.update({"guiter": "jimmy page"}) #This will change the value of the key guiter to jimmy page
print(band)

band.update({"drums": "john bonham"}) #This will add a new key value pair to the dictionary
print(band)

#Adding items to a dictionary
band["bass"] = "john paul jones" #This will add a new key value pair to the dictionary
print(band)

band.update({"keyboard": "john paul jones"}) #This will also add a new key value pair to the dictionary
print(band)

#Removing items from a dictionary
band.pop("keyboard") #This will remove the key value pair with the key keyboard
print(band)

band.popitem() #This will remove the last inserted key value pair and returns it as a tuple
print(band)

del band["drums"] #This will remove the key value pair with the key drums
print(band)

band.clear() #This will empty the dictionary
print(band)

del band #This will delete the dictionary
# print(band) #This will bring an error since the dictionary band is deleted

#Copying a dictionary
band = {
    "vacals": "plant",
    "guiter": "page"
}
band2 = band.copy() #This will copy the dictionary band to band2
print(band2)

band3 = dict(band) #This will also copy the dictionary band to band3
print(band3)

# #This is not a copy but a reference to the original dictionary
# band4 = band #This will not copy the dictionary band to band4 instead both band and band4 will point to the same dictionary
# print(band4)
# print(band)
# band4["drums"] = "bonham" #This will add a new key value pair to the dictionary band and since band4 points to the same dictionary as band both will be affected
# print(band4)
# print(band)

#Nested dictionaries
myband = {
    "band1": {
        "vacals": "plant",
        "guiter": "page"
    },
    "band2": {
        "vacals": "frank",
        "guiter": "eddie"
    }
}
print(myband) #This will print the nested dictionary
print(myband["band1"]) #This will print the dictionary of band1


