a = 5
<<<<<<< HEAD
b = 0
=======
b = 2
>>>>>>> origin/main

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

<<<<<<< HEAD
# except ZeroDivisionError:
#     print("Hey, division is not possible with 0")

# except ValueError:
#     print("Invalid Value")
    
except Exception as e:
    print("Something went wrong...")
    def pr():
        return "Something went wrong..."
    pr()
=======
except ZeroDivisionError:
    print("Hey, division is not possible with 0")

except ValueError:
    print("Invalid Value")
    
except Exception as e:
    print("Something went wrong...")
>>>>>>> origin/main
    
else:
    print("NEW EXCEPTION")

finally:
    print("Resource closed")
    
<<<<<<< HEAD
print("Process done")



# num = 2
# assert (num < 5), ("the number should not exceed by 5")
# print(num)

=======
print("Process done")
>>>>>>> origin/main
