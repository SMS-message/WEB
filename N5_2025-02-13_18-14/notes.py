class RequestError(Exception):
    ...


def find_coordinates():
    import requests
    toponym_to_find = input()

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        raise RequestError(
            f"Ошибка запроса, {geocoder_api_server}\nHTTP-status: {response.status_code}; {response.reason}")

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coordinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")
    upper_corner_coordinates = toponym["boundedBy"]["Envelope"]["upperCorner"].split(" ")
    lower_corner_coordinates = toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" ")

    toponym_longitude_delta = abs(float(upper_corner_coordinates[0]) - float(lower_corner_coordinates[0]))
    toponym_lattitude_delta = abs(float(upper_corner_coordinates[1]) - float(lower_corner_coordinates[1]))

    return (toponym_longitude, toponym_lattitude), (toponym_longitude_delta, toponym_lattitude_delta)


def ex1() -> None:
    import requests

    map_request = "https://static-maps.yandex.ru/v1?ll=37.677751,55.757718&spn=0.016457,0.00619&apikey=d0ba2aa1-0869-4bce-9286-72446e3ab2c1"
    response = requests.get(map_request)
    if not response:
        print(response.reason, response.status_code)
    with open("file.png", mode="wb") as file:
        file.write(response.content)


def ex2() -> None:
    from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

    import requests
    from PIL import Image

    # Пусть наше приложение предполагает запуск:
    # python search.py Москва, ул. Ак. Королева, 12
    # Тогда запрос к геокодеру формируется следующим образом:
    (toponym_longitude, toponym_lattitude), (var1, var2) = find_coordinates()

    delta = "0.005"
    apikey = "d0ba2aa1-0869-4bce-9286-72446e3ab2c1"

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "apikey": apikey,
        "spn": ",".join((delta, delta))

    }

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    print(response.url)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()  # Создадим картинку и тут же ее покажем встроенным просмотрщиком операционной системы


def ex3() -> None:
    import requests
    from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт
    from PIL import Image

    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    address_ll = ",".join(find_coordinates())

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    if not response:
        raise RequestError(
            f"Ошибка запроса, {search_api_server}\nHTTP-status: {response.status_code}; {response.reason}")

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первую найденную организацию.
    organization = json_response["features"][0]

    # Получаем координаты ответа.
    point = organization["geometry"]["coordinates"]
    org_point = f"{point[0]},{point[1]}"
    delta = "0.015"
    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        # позиционируем карту центром на наш исходный адрес
        "ll": address_ll,
        "spn": ",".join([delta, delta]),
        "apikey": apikey,
        # добавим точку, чтобы указать найденную аптеку
        "pt": "{0},pm2dgl".format(org_point)
    }

    map_api_server = "https://static-maps.yandex.ru/v1"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()


def main() -> None:
    ex2()


if __name__ == '__main__':
    main()
