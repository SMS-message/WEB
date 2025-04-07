import time
import asyncio
import os
from random import randint

ITER_NUM = 10
WORKERS_NUM = 5


def do_some_work(i: int) -> None:
    for j in range(ITER_NUM):
        print(f"{i * ' ' + chr(9608) + (WORKERS_NUM - i) * ' '}"
              f"Работник {i}. Прогресс: {j} {chr(9632) * j}")
        time.sleep(0.1 * randint(1, 10))


def main() -> None:
    for i in range(WORKERS_NUM):
        do_some_work(i)


if __name__ == '__main__':
    main()