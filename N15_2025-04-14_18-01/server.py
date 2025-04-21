import io
import logging
from contextlib import contextmanager, redirect_stdout
from json import dumps
from multiprocessing import Process
from time import sleep

from flask import Flask

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {"tale": "About Two elephants", "tags": "Animals, Adventure, Magic", "duration": 37},
        {"tale": "About a barber", "tags": "Victory, Travel", "duration": 53},
        {"tale": "About a silver jug", "tags": "Travel, Evil", "duration": 24},
        {"tale": "About three roosters", "tags": "Magic", "duration": 35},
        {"tale": "About Two camels", "tags": "Victory, Good", "duration": 51},
        {"tale": "About a donkey", "tags": "Magic, Evil", "duration": 43},
        {"tale": "About a lame son", "tags": "Evil", "duration": 32}
    ]

    server = Server('127.0.0.1', 8080, data)
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
