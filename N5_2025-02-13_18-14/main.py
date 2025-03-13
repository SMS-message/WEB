import requests


def find_info(toponym_to_find: str):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        return

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coordinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")
    upper_corner_coordinates = tuple(map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split(" ")))
    lower_corner_coordinates = tuple(map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" ")))

    toponym_longitude_delta = abs(upper_corner_coordinates[0] - lower_corner_coordinates[0])
    toponym_lattitude_delta = abs(upper_corner_coordinates[1] - lower_corner_coordinates[1])

    return toponym_longitude, toponym_lattitude, toponym_longitude_delta, toponym_lattitude_delta


def main() -> None:
    from io import BytesIO
    from PIL import Image
    from argparse import ArgumentParser

    # !python notes.py Москва

    parser = ArgumentParser()

    parser.add_argument("location", type=str, metavar="Географический объект")

    args = parser.parse_args()

    tp_lng, tp_lat, tp_lng_delta, tp_lat_delta = find_info(args.location)

    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    address_ll = ",".join((tp_lng, tp_lat))

    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    organization = json_response["features"][0]
    point = organization["geometry"]["coordinates"]

    center = abs(float(tp_lng) - point[0]), abs(float(tp_lat) - point[1])

    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    map_params = {
        "ll": ",".join(map(str, center)),
        "apikey": apikey,
        "spn": ",".join(map(str, (tp_lng_delta, tp_lat_delta))),
        "pt": ",".join([tp_lng, tp_lat]) + "," + "pm2" + "rd" + "l"

    }

    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()


if __name__ == '__main__':
    main()
