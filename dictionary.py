myDict = {
    "fruit1": "cherry",
    "fruit2": "banana",
    "fruit3": "apple",
    "fruit4": "kiwi",
    "fruit4": "mango",
    "numbers": [1, 3, 5, 7],
    "bool": True
}
# print(myDict["fruit1"])
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
#     print(x, y)
    

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
# print(myDict.keys())
myDict["food"] = "lunch"
# print(myDict)
key = frozenset(myDict)
myDict["food"] = "dinner"
# print(myDict)
# print(key)




#------------------------------------------------------------
name = {
    "name": "\'abc\' \'abc \\d \d \n \r \t '''HELLO''' "
}

# print(name['name'])


# -----------------------------------------------------------

# Convert the following two lists into a dictionary:
keys = ["name", "age", "grade"]
values = ["Bob", 22, "B"]
data = {}
for i in range(len(keys)):
    data.update({keys[i] : values[i]})
    
# print(data)


# Merge these two dictionaries:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
# print(dict1)


# Filter out all key-value pairs where the value is less than 50:
scores = {"Alice": 45, "Bob": 67, "Charlie": 30, "Dave": 89}
remove = []
for x,y in scores.items():
    if y < 50:
        remove.append(x)
    
for i in remove:
    scores.pop(i)
        
# print(scores)


# Double all the values in the following dictionary:            **
data = {"apple": 2, "banana": 3, "cherry": 5}
data = {key: value*2 for key,value in data.items()}
    
# print(data)


# Combine the following list of dictionaries into a single dictionary:
dict_list = [{"a": 1}, {"b": 2}, {"c": 3}]
data = {}
for i in range(len(dict_list)):
    data.update(dict_list[i])
    
# print(data)


# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.
square = {}
for i in range(1,6):
    square.update({i : i*i})
    
# print(square)


# Find the top 2 highest values in the dictionary.
scores = {"Charlie": 30,  "Dave": 89, "Alice": 45, "Bob": 67}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2])

print(sorted_scores)