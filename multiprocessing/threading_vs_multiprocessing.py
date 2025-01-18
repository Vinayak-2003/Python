import threading
import multiprocessing
import time

def cpu_bound_task():
    result = 0
    for _ in range(10**7):
        result += 1
        
# using threading
start_time = time.time()
threads = []
for _ in range(10):
    thread = threading.Thread(target=cpu_bound_task)
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
print(f"Threading: {time.time()-start_time}")

# using processing
start_time = time.time()
processes = []
for _ in range(10):
    process = multiprocessing.Process(target=cpu_bound_task)
    processes.append(process)
    process.start()

for process in processes:
    process.join()
print(f"Multiprocessing: {time.time()-start_time}")