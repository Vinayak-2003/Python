data = {"key": "value"}

def func():
    try:
        1/0
    except:
        print(f"{data["key"]}")
        
func()