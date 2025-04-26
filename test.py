myDict = {
    "fruit1": "cherry",
    "fruit2": "banana",
    "fruit3": "apple",
    "fruit4": "kiwi"}

# output = di = {"fruit1": "cherry", "fruit2": "banana", "fruit3": "apple", "fruit4": "kiwi"}

li=["cherry", "banana", "apple", "apple", "cherry", "cherry", "cherry"]
# output = di = {"cherry": 3, "banana": 1, "apple": 2}
# print(myDict)

cntCherry = 0
cntApple = 0
cntBanana = 0
for x in li:
    if x == 'cherry':
        cntCherry+=1
    elif x == 'apple':
        cntApple+=1
    else:
        cntBanana+=1

myDict2 = {
    "cherry": cntCherry,
    "apple": cntApple,
    "banana": cntBanana
}

# print(myDict2)


di = {}
for i in li:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1
        
# print(di)


a=[]
lix = [x for x in li]
# print(lix)


a = "hello"
# print(a[::-1])


import time

# time.sleep()


# -----------------------------------------

s = "hello my name"
# c = s[4]
# print(c)

c = s
# print(new_s)
# print(s)


val = "vinayak"
print(int(val[-1]))