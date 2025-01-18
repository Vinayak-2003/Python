# to create our own event loop

import asyncio

# create and access a new asyncio event loop
loop = asyncio.new_event_loop()

# print(loop)

# define a task
task = asyncio.sleep(2)

# execute a task
loop.run_until_complete(task)

# completion a task
print("DONE")