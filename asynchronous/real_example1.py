import asyncio
import time

start = time.time()

async def task1_func():
    print("Enters 1")
    await asyncio.sleep(3)
    print("Exit 1")
    print("Completed task 1...")
    
async def task2_func():
    print("Enters 2")
    await asyncio.sleep(2)
    print("Exit 2")
    print("Completed task 2...")

async def main():           # asynchronous
    task1 = asyncio.create_task(task1_func())
    task2 = asyncio.create_task(task2_func())
    await task1
    
if __name__ == '__main__':
    asyncio.run(main())

end = time.time()
print("Time: ", (end-start))