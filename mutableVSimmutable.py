x = [2, 3, 6]
y = x.append(5)
# print(x)
# print(y)
# print("X: ", id(x))
# print("Y: ", id(y))
x.append(5)
# print("X: ", x)
# print("Y: ", y)


a = "hello"
b = a.replace('e', 'a')
# print("A: ", id(a))
# print("B: ", id(b))
c = a + "6"
# print("A: ", a)
# print("B: ", b)
# print("C: ", c)


# ------------------------------------------------ #
p = "HELLO world!!"
q = "HELLO World!!"
r = q.replace("LLO", "llo")
# print(p == q)
# print("P: ", id(p))
# print("Q: ", id(q))
# print(id(p) == id(q))
# print(p is q)


car1 = "CAR"
car2 = car1.replace("A", "a")
# print(id(car1), id(car1[1]))
# print(id(car2), id(car2[1]))

lst1 = [1,2,3]
lst2 = lst1.append(5)
# print(lst1, lst2)
# print(id(lst1), id(lst2))


# ----------------------------------------------------- #
lst3 = [5,6,7]
my_dict = {
    "name": "Vinayak",
    "Age": 21,
    "lst1": "List"
}

# my_dict2 = {
#     lst1: "a",
#     lst3: "b"
# }
my_dict["name"] = "John"
# print(my_dict)
# print(my_dict2)


# ----------------------------------------------------- #
my_list = [(1,1),3,4]
my_tuple = ([1,1],3,4)

print(id(my_list))
print(id(my_tuple))
print(id(my_list[0]))
print(id(my_tuple[0]))

print(my_list[0])
my_list[0][0] = "Hello"
print(my_list)