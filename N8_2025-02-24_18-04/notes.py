import json
from flask import Flask, render_template, request, redirect


def main() -> None:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "xcb%h&jk^tx%ds5cfjhkl65t;r4desw'qw\ertyh]gf[dxcs!!!d!r3tr-8004"

    @app.route("/")
    def index():
        params = {
            "title": "Сайтик :0",
            "username": "Егор",
        }
        return render_template("index.html", **params)

    @app.route("/odd_even")
    def odd_even():
        params = {
            "title": "Сайтик :0",
            "username": "Егор",
            "number": 1501
        }
        return render_template("odd_even.html", **params)

    @app.route("/news")
    def news():
        params = {
            "title": "Сайтик :0",
            "username": "Егор",
        }
        with open("files/news.json", mode="r", encoding="utf-8") as json_file:
            news_list = json.loads(json_file.read())
        print(news_list)
        return render_template("news.html", **params, news=news_list)

    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    print("http://localhost:8080/")
    main()
