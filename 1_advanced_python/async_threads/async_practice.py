import asyncio
import datetime
import random
import time
from functools import wraps



# TASK-4

def async_retry(max_attempts=3, base_delay=1):
    def wrapper(async_func):
        @wraps(async_func)
        async def inner(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    print(f"Attempt {attempt+1}: ", end='')
                    res = await async_func(*args, **kwargs)
                    print("success")
                    return res
                except Exception as e:
                    if attempt == max_attempts + 1:
                        print("No attempts more")
                        raise

                    delay = base_delay * (2**attempt) + random.uniform(0, 1)
                    print(f"Waiting {delay} sec before next attempt")
                    await asyncio.sleep(delay)
        return inner
    return wrapper

@async_retry()
async def unstable_api_call():
    chance = random.randint(1, 10)
    if 1 < chance <= 7: raise ConnectionError("Not stable connection")
    else: return  {"status":"success"}


async def main():
    events = [
        unstable_api_call() for _ in range(1, 6)
    ]

    res = await asyncio.gather(*events, return_exceptions=True)


try:
    asyncio.run(main())
except Exception as e:
    ...
    # print(e)
# TASK-3

ids_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

async def api_request():
    await asyncio.sleep(1)

sem = asyncio.Semaphore(3)

async def rate_limited_requests(req_id):

    async with sem:
        print(f"Request: {req_id} started {time.time()}")
        await api_request()
        print(f"Request: {req_id} ended {time.time()}")

async def main():
    ids = [
        rate_limited_requests(req_id) for req_id in ids_list
    ]

    await asyncio.gather(*ids)

# asyncio.run(main())

# TASK-2

id_list = [1, 2, 3, 4, 5]

async def fetch_user_data(user_id):
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    return {"id":user_id, "name": f"User_{user_id}", "delay":delay}

async def main():
    fetch_list = [
        fetch_user_data(i) for i in id_list
    ]

    reses = await asyncio.gather(*fetch_list)
    for res in reses:
        print(res)

# start = time.time()
# asyncio.run(main())
# print("took: ", time.time()-start)


# TASK-1
async def log_event(event_name: str, delay_sec: float):
    await asyncio.sleep(delay_sec)
    print(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Event: {event_name}")

async def main():
    events = [
        log_event("event1", 3),
        log_event("event2", 2),
        log_event("event3", 1.5)
    ]
    await asyncio.gather(*events)

# asyncio.run(main())