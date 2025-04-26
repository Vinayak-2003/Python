from multiprocessing import Process, Lock, Semaphore

# allow upto 3 resources to access the resource 
sem = Semaphore(3)

def limited_resource(id):
    with sem:
        print("____sem",  sem)
        print(f"{id} is using the limited resource")
        
if __name__ == "__main__":
    processes = []
    for i in range(4):
        process = Process(target=limited_resource, args=(i,))
        processes.append(process)
        
    # print("______processes", processes)
    for p in processes:
        print("____p", p)
        p.start()
        
    for p in processes:
        p.join()

# def printe(lock, items):
#     lock.acquire()
#     print(f"Items: {items}")
#     lock.release()
    
# if __name__ == "__main__":
#     lock = Lock()
#     items = ["banana", "apple", "cherry"]
    
#     for item in items:
#         process = Process(target=printe, args=(lock, item))
#         process.start()