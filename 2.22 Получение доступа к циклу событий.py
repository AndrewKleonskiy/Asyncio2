import asyncio
from utils.delay_functions import delay

def call_later():
    print('Меня вызовут в ближайшее время')

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
asyncio.run(main())