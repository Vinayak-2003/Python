import threading
import time

start = time.time()

def print_num2():
    for i in range(10):
        time.sleep(1)
        print(f"_________________________________Thread: {threading.current_thread().name} Number: {i}")
        

def print_num():
    for i in range(10):
        time.sleep(1)
        print(f"Thread: {threading.current_thread().name} Number: {i}")
        
# creating a thread
my_thread = threading.Thread(target=print_num)

# starting thread
my_thread.start()

your_thread = threading.Thread(target=print_num2)
your_thread.start()
        
for i in range(10):
    time.sleep(1)
    print(f"main thread, number {i}")
    
end = time.time()

print(f"end - start", (end-start))