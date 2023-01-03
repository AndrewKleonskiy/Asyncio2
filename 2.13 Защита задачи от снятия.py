import asyncio
from utils.delay_functions import delay

async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Задача заняла более 5 с, скоро она закончаится!')
        result = await task
        print(result)
asyncio.run(main())