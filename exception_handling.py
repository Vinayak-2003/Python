a = 5
b = 0

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

# except ZeroDivisionError:
#     print("Hey, division is not possible with 0")

# except ValueError:
#     print("Invalid Value")
    
except Exception as e:
    print("Something went wrong...")
    def pr():
        return "Something went wrong..."
    pr()
    
else:
    print("NEW EXCEPTION")

finally:
    print("Resource closed")
    
print("Process done")



# num = 2
# assert (num < 5), ("the number should not exceed by 5")
# print(num)

