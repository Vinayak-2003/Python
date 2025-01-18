# -------------------PRINT------------------
name = "Vinayak"
age = 20

# print("My name is", name, "and I am", age, "years old", sep='|')

# print("Hello world!!", end=".....")
# print("My name is",name)


# -------------------HELP------------------
# help(print)

a = 10
b = 20
def calculate(a, b):
    sum = a + b
    print(sum)
    
# help(calculate)


# -------------------RANGE------------------
rng = range(10, -10, -2)

# print(tuple(rng))


# -------------------MAP------------------
# it allow us to apply a function to every single item in an iterable object
strings = ["my", "name", "is", "something"]

def add_s(x):
    return x + "s"

# lengths = map(len, strings)
# lengths = map(lambda x: x + "s", strings)
lengths = map(add_s, strings)
# print(list(lengths))


# -------------------FILTER------------------
# it will take all items in iterable object and then pass it to comparitable function
strings = ["my", "names", "is", "something"]

def len_greater_4(strr):
    return len(strr) > 4

filtered = filter(len_greater_4, strings)
# print(list(filtered))


# -------------------SUM------------------
numbers = {1, 2.7, 5, 8, 3}

# print(sum(numbers, start=10))


# -------------------SORTED------------------
nums = [7, 1, 9, 5, 3, 2, 4]
sorted_nums = sorted(nums, reverse=True)

# print(sorted_nums)

people = [
    {"name":"Manish", "age":22},
    {"name":"Honey", "age":19},
    {"name":"Bobby", "age":20},
    {"name":"Monica", "age":21}
]

sorted_people = sorted(people, key = lambda prsn: prsn["age"])
# print(list(sorted_people))


# -------------------ENUMERATE------------------
# it iterates over the list with its indexes
tasks = ["abc", "def", "ghi", "jkl"]

# for i in range(len(tasks)):
#     task = tasks[i]
#     print(f"{i}. {task}")
    
# for i, task in enumerate(tasks):
#     print(f"{i}. {task}")

# print(list(enumerate(tasks)))


# -------------------ZIP------------------
# it combines different iterable objects and together and automatically handles when one iterable 
# object has more objects than other

names = ["a", "g", "t", "d"]
ages = [23, 19, 27, 22, 25]

# for i in range(min(len(names), len(ages))):
#     name = names[i]
#     age = ages[i]
#     print(f"{name} -> {age}")

combined = list(zip(names, ages))
print(combined)

for name, age in combined:
    print(f"{name} -> {age}")