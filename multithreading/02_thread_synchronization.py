import threading
import time

start = time.time()

shared_resource = 0

lock = threading.Lock()


semaphore = threading.Semaphore(1)

# ensures that only one thread can execute the critical section
def increment_shared_resource():
    start = time.time()
    global shared_resource
    print("_______________________________shared_resource_before", shared_resource)
    for _ in range(100000):
        with lock:
            shared_resource += 1
    print("_______________________________shared_resource_after", shared_resource)
    end = time.time()
    print("end - start", end-start)



# def increment_shared_resource():
#     global shared_resource
#     print("_______________________________shared_resource_before", shared_resource)
#     for _ in range(100000):
#         with semaphore:
#             shared_resource += 1
#     print("_______________________________shared_resource_after", shared_resource)
        

thread_1 = threading.Thread(target=increment_shared_resource)
thread_2 = threading.Thread(target=increment_shared_resource)


thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"Final value of shared resource: {shared_resource}")
# print(f"end - start", (end-start))