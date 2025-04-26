import multiprocessing
import time

def hello(n):
    for i in range(n):
        print("HELLLLOOOO")
        
def hi(n):
    for i in range(n):
        print("Hiiiiii")
 
        
hello(10)
hi(10)

if __name__ == "__main__":
    h1 = multiprocessing.Process(target=hello, args=[10])
    h2 = multiprocessing.Process(target=hi, args=[10])

    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("DONEEE")


# ---------------------------------------------------------------------- #

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)


time1 = time.perf_counter()
# Normal execution
# func(4)
# func(1)
# func(2)

if __name__ == "__main__":
    # Multiprocessing
    t1 = multiprocessing.Process(target=func, args=[4])
    t2 = multiprocessing.Process(target=func, args=[1])
    t3 = multiprocessing.Process(target=func, args=[2])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2-time1)