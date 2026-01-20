import time
import asyncio

async def func1():
    await time.sleep(10)
    await print("Func 1 ended")


async def func2():
    await time.sleep(10)
    await print("Func 2 ended")

while True:
    choice = input()
    if choice == '1':
        func1()
        continue
    elif choice == '2':
        func2()
        continue