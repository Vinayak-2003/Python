myDict = {
    "fruit1": "cherry",
    "fruit2": "banana",
    "fruit3": "apple",
    "fruit4": "kiwi",
    "fruit4": "mango",
    "numbers": [1, 3, 5, 7],
    "bool": True
}
print(myDict["fruit1"])
myDict2 = dict(fruit1="cherry", fruit2="Apple", fruit3="mango", num=[1,5,7])

# print(myDict)
# print(type(myDict))
# print(len(myDict))
# print(myDict2)


#------------------Access dictionary items----------------------
# print(myDict["numbers"])
# print(myDict.get("bool"))
# print(myDict.get("bools"))
x = myDict.keys()
# print(x)
# print(type(x))
y = myDict.values()
# print(y)
# print(type(y))
z = myDict.items()
# print(z)
# print(type(z))

# if 'fruit4' in myDict:
#     print("Yes, fruit4 is present")
# else:
#     print("No, fruit4 is not present")


#------------------Add & Change dictionary items----------------------
myDict["fruit2"] = "pineapple"
myDict["fruit5"] = "lichi"
# print(myDict)

myDict.update({"vegetable1": "potato", "vegetable2": "cabbage"})
myDict.update({"[3,5,6]": "(5,4,3)"})
# print(myDict)


#------------------remove dictionary items----------------------
myDict.pop("vegetable1")
myDict.popitem()
del myDict['fruit2']
# myDict.clear()
# del myDict
# print(myDict)


#------------------Loop dictionary items----------------------

# print only keys
# for x in myDict:
#     print(x)

# print only keys
# for y in myDict.keys():
#     print(y)

# print only values   
# for x in myDict:
#     print(myDict[x])
    
# print only values   
# for x in myDict.values():
#     print(x)

# prints both key and value pairs
# for x,y in myDict.items():
    # print(x, y)
    

#------------------copy dictionary items----------------------
# myDictRef = myDict
# myDictRef['fruit1'] = 'berry'
# print(myDictRef)
# print(myDict)

# copyDict = myDict.copy()
# copyDict['fruit1'] = 'berry'

thisDict = dict(myDict)
thisDict['fruit1'] = 'berry'

# print(thisDict)
# print(myDict)


#------------------Nested dictionary items----------------------
myFamily = {
    "father": {
        "name": "Father",
        "email": "Father09@gmail.com"
    },
    "mother": {
        "name": "Mother",
        "email": "Mother08@gmail.com"
    },
    "child": {
        "name": "Child",
        "email": "Child07@gmail.com"
    }
}

# print(myFamily)
# for x,y in myFamily.items():
#     print(x,y)
    

brother = {
    "name": "Brother",
    "email": "Brother05@gmail.com"
}
sister = {
    "name": "Sister",
    "email": "Sister03@gmail.com"
}

myFamily = {
    "brother": brother,
    "sister": sister
}

# print(myFamily)
# print(myFamily["sister"]["email"])

# for x, val in myFamily.items():
#     print(x)
#     for y in val:
#         print(y + ':' ,val[y])
        
        
#------------------Use of frozen set in dictionary----------------------
print(myDict.keys())
myDict["food"] = "lunch"
print(myDict)
key = frozenset(myDict)
myDict["food"] = "dinner"
print(myDict)
print(key)