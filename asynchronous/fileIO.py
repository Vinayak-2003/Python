import time
import asyncio

start = time.time()

async def fetch_file():
    print("Fetching started ...")
    await asyncio.sleep(5)
    print("Fetching completed ...")
    
async def main():
    print("Main started ...")
    # await asyncio.gather(
    #     fetch_file(),
    #     fetch_file(),
    #     fetch_file()
    # )
    await fetch_file(),
    await fetch_file(),
    await fetch_file()
    print("Main ended ...")
    
asyncio.run(main())

end = time.time()
print("Total time: ", (end-start))


# for downloading a file (file handling) ----> aiofiles
# to send any kind of request / download image ----> aiohttp 