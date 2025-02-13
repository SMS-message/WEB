class RequestError(Exception):
    ...


def get_coord(address: str) -> float:
    import requests
    geo_request: str = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json"

    response = requests.get(geo_request)
    if response:
        json_response: dict = response.json()
        res = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    else:
        raise RequestError(f"Ошибка запроса, {geo_request}\nHTTP-status: {response.status_code}; {response.reason}")
    return float(res.split()[1])


def run():
    inp = dict((get_coord(city.capitalize()), city.capitalize()) for city in
               input("Введите название городов через запятую: ").split(", "))
    # print(inp)
    print("Самый южный город из введённых:", inp[min(inp)])
    print()


def main() -> None:
    print("Добро пожаловать в программу-определитель самого южного города!")
    running = True
    while running:
        run()
        print('Чтобы выйти из программы напишите "q"')
        if input() == "q":
            running = False

    quit()


if __name__ == '__main__':
    main()
