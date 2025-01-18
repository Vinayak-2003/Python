import monkey_patch2
def monkey_f():
    print("monkey_f() is called")
    
monkey_patch2.A.func = monkey_f
obj = monkey_patch2.A

obj.func()