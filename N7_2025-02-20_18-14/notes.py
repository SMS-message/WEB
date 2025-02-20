def ex1() -> None:
    from http.server import HTTPServer, CGIHTTPRequestHandler
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


def ex2() -> None:
    from flask import Flask, url_for

    app = Flask(__name__)
    @app.route("/")
    def index() -> str:
        with open("index.html", mode="r", encoding="utf-8") as html:
            return html.read()

    @app.route("/countdown")
    def countdown() -> str:
        countdown_list = [str(i) for i in range(10, 0, -1)]
        countdown_list.append("Пуск!")
        return "<br>".join(countdown_list)

    @app.route("/image")
    def image() -> str:
        return f"""<img src='{url_for('static', filename='/img/image.png')}'
                    alt='Тут должен быть котц!'>"""

    app.run(port=8080, host="localhost")


if __name__ == '__main__':
    ex2()
