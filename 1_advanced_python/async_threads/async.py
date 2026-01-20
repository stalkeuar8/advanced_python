import asyncio
import threading

def multiply(a, b):
    return a*b

def generator(a, b):
    while True:
        yield a*b
        a *= 2


async def my_as_func(a):
    while True:
        await asyncio.sleep(10)
        print("async worked")

def sync_func():
    print("sync worked")

async def main():
    await my_as_func(1)
    sync_func()




async def first():
    print(1)

async def second():
    await asyncio.sleep(10)
    print(2)

async def third():
    print(3)

async def do(sec):
    await asyncio.sleep(sec)
    print("res:", sec)

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)
    await do(sec)

async def main():
    ...
    # async with asyncio.TaskGroup() as tg:
    #     for i in range(1, 16):
    #         tg.create_task(print1(i))
    # tasks = []
    # task1 = asyncio.create_task(first())
    # task2 = asyncio.create_task(second())
    # task3 = asyncio.create_task(third())
    # await asyncio.gather(*tasks)

asyncio.run(main())