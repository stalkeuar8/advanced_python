import asyncio
import datetime
import os
import random

# TASK-6

class SuppressExceptions:
    def __init__(self, exc_list: list):
        self.exc_list = exc_list

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if exc_type in self.exc_list:
                pass
            else:
                print(f"Error: {exc_type}")
        else:
            pass

        return True


with SuppressExceptions([KeyError, TypeError]) as _:
    raise TypeError

# TASK-5

class ConnectionPool:


    def __init__(self, conn_id, max_conns=3):
        self.sem = asyncio.Semaphore(max_conns)
        self.operations = []
        self.conn_id = conn_id


    async def __aenter__(self):
        return self


    async def acquire(self, connection):
        await asyncio.sleep(1)
        self.operations.append(connection)


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"connected. Conn id: {self.conn_id}")
        else:
            print(f"Error: {exc_val}. Conn id: {self.conn_id}")

        print(f"closing connection logic. Conn id: {self.conn_id}")

        return True

async def connect(connection, conn_id):
    async with ConnectionPool(conn_id) as conn:
        async with conn.sem:
            await conn.acquire(connection)


async def main():
    tasks = [
        connect("conn1", 1),
        connect("conn2", 2),
        connect("conn3", 3),
        connect("conn4", 4),
        connect("conn5", 5),
        connect("conn6", 6),
        connect("conn7", 7),
        connect("conn8", 8),
        connect("conn9", 9)
    ]
    await asyncio.gather(*tasks)

# asyncio.run(main())

# TASK-4

class AsyncFileDownloader:
    def __init__(self, filepath):
        self.filepath = filepath

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("success")
        else:
            print(f"Error: {exc_val}")

        print("closing logic")

        return True

    async def loader(self, wait_time):
        byte_qty = random.randint(1, 100)
        await asyncio.sleep(wait_time)
        print(f"Loaded: {byte_qty} bytes")

async def download_file(filename:str):
    async with AsyncFileDownloader(filename) as file:
        await file.loader(1)
    print("------")


async def download_file_fail(filename:str):
    async with AsyncFileDownloader(filename) as file:
        await file.loader(3)
        raise KeyError("Some error")

async def main():
    tasks = [
        download_file("some file"),
        download_file_fail("some file")
    ]

    await asyncio.gather(*tasks)

# asyncio.run(main())

# TASK-3

class Database:
    def __init__(self):
        self.operations = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("...commit logic")
        else:
            print(f"...rollback logic. Error: {exc_val}")
        return True

    def execute(self, operation):
        self.operations.append(operation)


# with Database() as db:
#     db.execute("Success operation 1...")
#     db.execute("Success operation 2...")
#     db.execute("Success operation 3...")
#
# with Database() as db:
#     db.execute("Unsuccess operation 1...")
#     raise KeyError("1 error")




# TASK-2

class ChangeDirectory:
    def __init__(self, new_dir):
        self.new_dir = new_dir

    def __enter__(self):
        return self.new_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Process ended successfully.")
        else:
            print(f"Error '{exc_val}' occurred.")

        return True

# with ChangeDirectory("/tmp") as cwd:
#     print(os.getcwd())
#
# print(os.getcwd())


# TASK-1

class OperationLogger:
    def __init__(self, process_name):
        self.processing_time = None
        self.process_name = process_name

    def __enter__(self):
        print(f"[START] {self.process_name}")
        self.processing_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"[END] NO ERRORS. {self.process_name} time: {datetime.datetime.now() - self.processing_time}")
        else:
            print(f"ERROR OCCURRED. Process: {self.process_name} | Error: {exc_val} | Traceback {exc_tb}")
        return True

# with OperationLogger("dividing") as dev_process:
#     print("Dividing 10 by 2:", 10/2)
#     print("Dividing 3 by 0:", 3/0)
