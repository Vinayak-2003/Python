def create_dynamic_list(n):
    dynamic_list = []
    for i in range(n):
        dynamic_list.append(i)
        print(i)
    return dynamic_list

# Runtime
n = int(input("Enter the number of elements: "))
my_list = create_dynamic_list(n)

# Compile Time
print("Length of the list: ", len(my_list))