from time import time
from datetime import datetime as dt
import asyncio
import os

RATIO = 1


async def dish(num: int, prepare: int, wait: int) -> None:
    print(f"Начинаем в {dt.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num}")
    print(f"Время подготовки: {prepare} мин.")
    await asyncio.sleep(RATIO * prepare)
    print(f"Блюдо отправляется в печь. Время {dt.now().strftime('%H:%M:%S')}.")
    print(f"Ждём готовности. Осталось {wait} мин.")
    await asyncio.sleep(RATIO * wait)
    print(f"!! Блюдо №{num} готово !!")


async def main() -> None:

    task = [
        asyncio.create_task(dish(1, 2, 3)),
        asyncio.create_task(dish(2, 5, 10)),
        asyncio.create_task(dish(3, 3, 5)),
    ]
    await asyncio.gather(*task)


if __name__ == '__main__':
    t0 = time()
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
    delta = int(time() - t0) / RATIO
    print(f"Всё готово в {dt.now().strftime('%H:%M:%S')} "
          f"Всего потрачено {delta} мин.")
