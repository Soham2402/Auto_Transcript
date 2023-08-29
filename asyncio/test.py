import asyncio
import time


async def test_function():
    for i in range(3):
        print("Function 1 started going to sleep")
        time.sleep(10)
        print("Done sleeping")
# now executing this function directly will give us an ibject, this is a coroutine object 
print(test_function())
#this new object is asynchronus and allows us to write async code 

async def test_function2():
    print("Function 2 started")
    asyncio.create_task(test_function())
    print('function2 finished')
    
asyncio.run(test_function2())