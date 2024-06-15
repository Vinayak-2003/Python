a = """bdsudbwd
dhbabduhdb
jdbbdbdb"""

# print("hello")
# print(a)

x = "Banana"
# for i in x:
    # print(i)
    
# print(len(x))


txt = "Everything is free"
# print("freee" in txt)
# print("freee" not in txt)


#---------------string slicing-------------------
z = "Vinayak"
# print(z[:])
# print(z[2:5])
# print(z[2:])
# print(z[-6:-1])


#---------------string modify-------------------
z = "  Helloo oo world h j i "

# print(z.upper())
# print(z.lower())
# print(z.strip())
# print(z.split())

#---------------string foramtting-------------------
n = "V"

text = "I have " + n
# text1 = f"I have {n:.2f} dollars"
# text2 = f"I have {n * 2} dollars"
# print(text)


#---------------Escape characters-------------------
helo = "Helllloooo \"hello\" worldddd"
helo = "Helllloooo \\hello worldddd"
helo = "Helllloooo \nhello worldddd"
helo = "Helllloooo \rhello worldddd"
helo = "Helllloooo \thello worldddd"
helo = "Helllloooo \bhello worldddd"


# print(helo)

# print(helo.encode())
# print(helo.format())


#--------------------------------
s = "0123456789 638 727"
s = "   my     name is    "
# print(s[0:7:2])
# print(len(s))
# print(s.split())

j = s.split()
# print(type(j))

# print(s.lstrip())

#---------------sort string-------------------
st = "bcshbhDDAAJjsndsfnfinn dsfghjdnwkdnk jdbuehdu"
sort_st = sorted(st)
sort_st2 = ''.join(sorted(st, key=str.lower))
sort_st3 = ''.join(sorted(st.lower()))
sort_st4 = ''.join(sorted(set(st)))
sort_st5 = ''.join(filter(lambda x:x.isalpha(), sorted(st, key=str.lower)))
print(sort_st5)
print(type(sort_st4))