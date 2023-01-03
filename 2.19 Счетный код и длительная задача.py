import asyncio
from utils.async_timer import async_timed
from utils.delay_functions import delay

@async_timed()
async def cpu_bond_work() -> int:
    counter = 0
    for i in range(1000000):
        counter = counter + 1
    return counter

@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bond_work())
    task_two = asyncio.create_task(cpu_bond_work())
    delay_task = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await delay_task

asyncio.run(main())
