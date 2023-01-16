import asyncio
from utils.async_timer import async_timed
from utils.delay_functions import delay

async def positive_async(until: int):
    for integer in range(1,until):
        await delay(integer)
        yield integer

@async_timed()
async def main():
    async_generator = positive_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число {number}')
asyncio.run(main())