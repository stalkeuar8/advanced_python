import asyncio
import random
from pathlib import Path
import datetime
import aiofiles

class OpenFile:
    def __init__(self, filename: str):
        self.filename = filename

    async def __aenter__(self):
        try:
            path = Path(self.filename)
            path.touch(exist_ok=True)
            self.file = await aiofiles.open(path, 'a')
            return self.file
        except Exception as e:
            print(f"ERROR Occurred while opening file. {e}")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.file.close()
        if exc_type is None:
            print(f"Success, file '{self.filename}' closed.")
        else:
            print(f"Error: {exc_type} occurred. File '{self.filename}' closed. ")

        return True

async def text_generator(n):
    for _ in range(n):
        num = random.randint(0, 100)
        if num % 2 == 0:
            await asyncio.sleep(0.3)
            yield num
        else:
            yield num
            await asyncio.sleep(0.1)

filter_num = lambda x: x > 80


async def main():
    filepath = 'my_file.txt'
    anomaly = []
    async with OpenFile(filepath) as file:
        start = datetime.datetime.now()
        async for num in text_generator(100):
            if not filter_num(num):
                await file.write(f'{str(num)}\n')
                print(f"Num {num} been written to file")
            else:
                anomaly.append(num)
        time_spent = datetime.datetime.now() - start
        print(f"\nTime spent: {time_spent}")
    print("\nAnomaly nums ignored:")
    for log in anomaly:
        print(log)
    del anomaly

asyncio.run(main())



