txt = "Hello My Name Is PETER"
new_text = ""

# print(txt.swapcase())

for i in txt:
    if i == " ":
        new_text += " "
        
    elif ord(i)>=97 and ord(i)<=122:             # small to uppen
        diff = ord(i) - 97
        new = 65 + diff
        new_text += chr(new)
    
    elif ord(i)>=65 and ord(i)<=90:           # capital to small
        diff = ord(i) - 65
        new = 97 + diff
        new_text += chr(new)

print(new_text)