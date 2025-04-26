from multiprocessing import Process, Queue, Pipe

# communication using pipe
def worker(conn):
    conn.send("Hello from the worker process")
    print("send_____")
    message = conn.recv()
    print("message_____")
    print(f"Worker received message: {message}")
    print("print_____")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker , args=(child_conn,))
    print("process_____")
    p.start()
    print("start_____")
    print(f"Main process received message: {parent_conn.recv()}")
    parent_conn.send("Hello from the main process")
    
    p.join()


# communication using Queue
def worker(q):
    # Queue.put() is used to insert data to queue
    q.put("hello from the worker process")
    
if __name__ == "__main__":
    my_queue = Queue()
    p = Process(target=worker, args=(my_queue,))
    p.start()
    p.join()
    
    # Queue.get() is used to receive data to queue
    message = my_queue.get()
    print(f"Main process received message: {message}")