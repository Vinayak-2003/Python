# from time import sleep
# from threading import *

# class hello(Thread):
#     def run(self):
#         for i in range(7):
#             print("HELLOO")
#             sleep(1)
            
# class hi(Thread):
#     def run(self):
#         for i in range(7):
#             print("HIiii")
#             sleep(1)
            

# t1 = hello()
# t2 = hi()

# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()

# print("BYEEE")


# ----------------------------------------------------------- #
# import threading
# import time

# def func(sec):
#     print(f"Sleeping for {sec} seconds")
#     time.sleep(sec)

# time1 = time.perf_counter() 
# normal code
# func(4)
# func(1)
# func(2)

# code using threading
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[1])
# t3 = threading.Thread(target=func, args=[2])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# Calculating time
# time2 = time.perf_counter()
# print(time2-time1)