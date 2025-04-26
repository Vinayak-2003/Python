a = "hello my name is"
b = a[::-1]
# print(b)

# for word in a:
b = a.split(" ")
rev_sen = ""
# for word in b:
    # rev = word[::-1]
    # rev_sen = rev_sen + " " + word
    
for i in range(len(b)-1, -1, -1):
    rev_sen = rev_sen + " " + b[i]

# rev_sen = " ".join(reversed(b))
    
# print(rev_sen)

# ------------ mutable vs immutable -----------
a = (1,2,3)
# print(id(a))

# a += (5,6)
# print(a)
# print(id(a))


sentence = "Never give up without even trying. Do what you can"

max_char = {}
for i in sentence:
    if i in max_char:
        max_char[i] += 1
    else:
        max_char[i] = 1

maxx = 0
ans = ""
for x,y in max_char.items():
    if y>maxx:
        maxx = y
        ans = x
        
print(ans)
