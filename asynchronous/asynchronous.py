import multiprocessing
import asyncio

print(multiprocessing.cpu_count())

async def a():
    print("random")
    
print(a())            # here is gives an error

async def main():
    print("Started...")
    
# to execute a co-routine you need an event loop, 
# asyncio.run() automatically creates this async event loop for us
asyncio.run(main())