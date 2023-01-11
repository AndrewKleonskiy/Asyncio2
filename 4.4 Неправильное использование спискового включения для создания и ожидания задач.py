import asyncio
from utils.delay_functions import delay
from utils.async_timer import async_timed

@async_timed()
async def main() -> None:
    delay_times = [3,3,3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]
asyncio.run(main())