import json


def example():
    try:
        with open("data.json") as data_file:
            f = data_file.read()
            data = json.loads(f)

        for user in data:  # Вывод объекта
            for key, value in user.items():
                print(f"{key.upper()}: {value.__str__().upper()}")
            print()
    except FileNotFoundError:
        pass
    finally:
        user_data = [
            {
                "name": "John",
                "age": 26,
                "status": "user"
            },
            {
                "name": "newCEO",
                "age": 30,
                "status": "admin"
            }
        ]

        with open("user_data.json", mode="w") as data_file:  # Запись в .json файл
            sort_keys = input("Сортировать ключи? [Y]/[N]: ").upper() == "Y"
            json.dump(user_data, data_file, indent=2,
                      sort_keys=sort_keys)  # indent отвечает за отступы в выходном файле


def ex1():
    import json
    with open("ex1.json", encoding="utf-8") as f:
        data = json.load(f)

    print(data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
              "GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]["SubAdministrativeArea"][
              "SubAdministrativeAreaName"])


def ex2():
    import os
    print(f"{os.name = }")
    # print(dir(os))
    print(f"{os.getcwd() = }")  # Путь до текущей директории
    os.mkdir("files")
    os.chdir("files"), print(f"{os.getcwd() = }")
    os.chdir(".."), print(f"{os.getcwd() = }")
    print(f"{os.access('files', os.F_OK) = }")  # Директория существует
    print(f"{os.access('files', os.W_OK) = }")  # В директории можно писать
    print(f"{os.access('files', os.R_OK) = }")  # Директорию можно читать


def dir_tree():
    ex3()


def ex3():
    import os

    print(f"{os.listdir('data') = }")

    walk = os.walk('data')
    # print(*walk)

    for cur_dir, dirs, files in walk:
        spaces = "\t" * cur_dir.count("/")
        print(spaces + "📁 " + str(cur_dir.split("/")[-1]))
        if files:
            for f in files:
                print(spaces + "  - " + f)


def ex4():
    import shutil
    run = False
    if run:
        shutil.copy('data/3/Описание.txt', "data/Описание - копия.txt")  # Копирование файла
        shutil.rmtree('data/3/files')  # Удаление директории
        shutil.move("data/1", "data/3/")  # Перемещение директории
    root_dir = 'data'  # Архивируемая папка
    name = root_dir + " archive"  # Название архива
    shutil.make_archive(name, 'zip', root_dir=root_dir)


def ex5():
    from zipfile import ZipFile

    with ZipFile("data archive.zip") as myzip:
        myzip.printdir()
        print(f"\n{myzip.namelist() = }")
        with myzip.open('3/Описание.txt', mode='r') as f:
            print(f.read().decode("utf-8"))
    with ZipFile("data archive.zip", mode='a') as myzip:
        myzip.write("ex1.json")
        print(f"\n{myzip.namelist() = }")


def ex6():
    from zipfile import ZipFile

    with ZipFile("data archive.zip") as myzip:
        myzip.extractall(path='extracted data archive',
                         members=None,
                         pwd=None)


def main() -> None:
    ex4()


if __name__ == '__main__':
    main()
