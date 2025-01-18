from multiprocessing import Process, Pool, cpu_count

# creating process using Process class

def print_hello(name):
    print(f"hello {name}!")
    
if __name__ == "__main__":
    process1 = Process(target=print_hello, args=("Vinayak",))
    process2 = Process(target=print_hello, args=("Aman",))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()


# creating process using Pool
def square(x):
    return x*x

# if __name__ == "__main__":
#     data = [1,2,3,4,5]
#     with Pool() as pool:
#         results = pool.map(square, data)
#     print(f"Squares: {results}")
    
    
print("____CPU counts____", cpu_count())