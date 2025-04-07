from time import sleep, time
from datetime import datetime as dt

RATIO = 1


def dish(num: int, prepare: int, wait: int) -> None:
    print(f"Начинаем в {dt.now().strftime('%H:%M:%S')} "
          f"готовить блюдо №{num}")
    print(f"Время подготовки: {prepare} мин.")
    sleep(RATIO * prepare)
    print(f"Блюдо отправляется в печь. Время {dt.now().strftime('%H:%M:%S')}.")
    print(f"Ждём готовности. Осталось {wait} мин.")
    sleep(RATIO * wait)
    print(f"!! Блюдо №{num} готово !!")


def main() -> None:
    dish(1, 2, 3)
    dish(2, 5, 10)
    dish(3, 3, 5)


if __name__ == '__main__':
    t0 = time()
    main()
    delta = int(time() - t0) / RATIO
    print(f"Всё готово в {dt.now().strftime('%H:%M:%S')} "
          f"Всего потрачено {delta} мин.")
