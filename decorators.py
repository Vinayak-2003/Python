# def print_msg(message):
#     greeting = "Hello,"
    
#     def print_it():
#         print(greeting, message)
    
#     print_it()
<<<<<<< HEAD

=======
>>>>>>> origin/main
# print_msg("Python is Great")



# def decorator_1(func1):
#     def execute():
#         print("Executing it now!!")
#         func1()
#         print("Executed the function!!")
#     return execute

# def human():
#     print("We are the coolest living being....")

# who_are_we = decorator_1(human)
# who_are_we()



<<<<<<< HEAD
# def display_this(function):

=======
# def printe():
#     print("Hey Everyone")

# def display_this(function):
    
>>>>>>> origin/main
#     def inside():
#         print("Executing", function.__name__, "function")
#         function()
#         print("finished Execution")
        
#     return inside

<<<<<<< HEAD
# def printe():
#     print("Hey Everyone")

=======
>>>>>>> origin/main
# decorated_function = display_this(printe)
# decorated_function()


def display_this(function):
<<<<<<< HEAD
    print("==========================")
=======
    
>>>>>>> origin/main
    def inside():
        print("Executing", function.__name__, "function")
        function()
        print("finished Execution")
<<<<<<< HEAD
    print("_________________________")
=======
        
>>>>>>> origin/main
    return inside

@display_this
def printe():
    print("Hey Everyone")

printe()