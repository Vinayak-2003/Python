from multiprocessing import Process, current_process
import time

def lifecycle():
    print(f"{current_process().name} is created")
    print(f"{current_process().name} is running")
    time.sleep(5)
    print(f"{current_process().name} is terminated")

if __name__ == "__main__":
    process = Process(target=lifecycle)
    process.start()
    process.join()