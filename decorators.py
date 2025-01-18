# def print_msg(message):
#     greeting = "Hello,"
    
#     def print_it():
#         print(greeting, message)
    
#     print_it()

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



# def display_this(function):

#     def inside():
#         print("Executing", function.__name__, "function")
#         function()
#         print("finished Execution")
        
#     return inside

# def printe():
#     print("Hey Everyone")

# decorated_function = display_this(printe)
# decorated_function()


def display_this(function):
    print("==========================")
    def inside():
        print("Executing", function.__name__, "function")
        function()
        print("finished Execution")
    print("_________________________")
    return inside

@display_this
def printe():
    print("Hey Everyone")

printe()