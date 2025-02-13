

class RequestError(Exception):
    ...


def main() -> None:
    import requests
    import json
    geo_request: str = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={input()}&format=json"

    response = requests.get(geo_request)
    if response:
        print(response, type(response))
        print(response.content)
        json_response: dict = response.json()

        print(json_response)
        with open("ex1.json", mode='w', encoding='utf-8') as json_file:
            json.dump(json_response, json_file, ensure_ascii=False)
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][1]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
            print(toponym)
    else:
        raise RequestError(f"Ошибка запроса, {geo_request}\nHTTP-status: {response.status_code}; {response.reason}")
if __name__ == '__main__':
    main()
