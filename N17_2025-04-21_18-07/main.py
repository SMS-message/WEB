from os import getenv
from time import sleep
from typing import Tuple
from pprint import pprint
from dotenv import load_dotenv
from vk_api import Captcha, VkApi
from vk_api.vk_api import VkApiMethod
from requests import get
from io import BytesIO
from PIL import Image

load_dotenv()

LOGIN = getenv("LOGIN")


def auth_handler() -> Tuple[str, bool]:
    code = input("Требуется ввести код двухфакторной аутентификации: ")
    return code, True


def captcha_handler(captcha: Captcha):
    im = Image.open(captcha.get_url())
    im.show()
    key = input(f"Требуется ввести капчу: ")

    return captcha.try_again(key)

def task():
    vk_session = VkApi(LOGIN, auth_handler=auth_handler, captcha_handler=captcha_handler)
    vk_session.auth()

    vk: VkApiMethod = vk_session.get_api()

    friends = vk.friends.get(fields=("bdate",))["items"]

    list_of_friends = []
    for friend in friends:
        # У некоторых пользователей нельзя получить день рождения, т.к. они его скрыли.
        # Поэтому чтобы программа не выдала ошибку, то надо поставить "заглушки" для таких друзей.
        if "bdate" in friend:
            b_date = friend["bdate"]
        else:
            b_date = None
        list_of_friends.append((friend["last_name"], friend["first_name"], b_date))
    list_of_friends = sorted(list_of_friends, key=lambda x: x[0])
    for friend in list_of_friends:
        print(f"{friend[0]}, {friend[1]}, {friend[-1]}")


def main() -> None:
    while True:
        task()
        sleep(2)


if __name__ == '__main__':
    main()
