import asyncio

# Await
# should be called / executed in a coroutine only
# use to pause another coroutine

async def square(num):
    return num*num

async def main():
    x = await square(2)
    print(x)
    
    y = await square(3)
    print(y)
    
    z = x+y
    print(z)
    
asyncio.run(main()) 

# ans = await square(5)
# print(ans) 