import asyncio
import os
from random import randint

ITER_NUM = 10
WORKERS_NUM = 5


async def do_some_work(i: int) -> None:
    for j in range(ITER_NUM):
        print(f"{i * ' ' + chr(9608) + (WORKERS_NUM - i) * ' '}"
              f"Работник {i}. Прогресс: {j} {chr(9632) * j}")
        await asyncio.sleep(0.1 * randint(1, 10))


async def main() -> None:
    task = []
    for i in range(WORKERS_NUM):
        task.append(asyncio.create_task(do_some_work(i)))
    await asyncio.gather(*task)


if __name__ == '__main__':
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
