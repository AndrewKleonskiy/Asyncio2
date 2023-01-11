import asyncio
from utils.async_timer import async_timed
from utils.delay_functions import delay

@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]
asyncio.run(main())