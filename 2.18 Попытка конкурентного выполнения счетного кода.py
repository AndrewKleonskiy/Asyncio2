import asyncio
from utils.delay_functions import  delay
from utils.async_timer import async_timed

@async_timed()
async def cpu_bond_work() -> int:
    counter = 0
    for i in range(10000000):
        counter = counter + 1
    return counter

@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bond_work())
    task_two = asyncio.create_task(cpu_bond_work())
    await task_one
    await task_two
asyncio.run(main())