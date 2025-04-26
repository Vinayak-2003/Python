from multiprocessing import Process
import time

def daemon_worker():
    print("daemon process started")
    time.sleep(5)
    print("daemon process ended")
    
if __name__ == "__main__":
    process = Process(target=daemon_worker, daemon=True)
    process.start()
    process.join(timeout=2)
    print(f"Main process ended")