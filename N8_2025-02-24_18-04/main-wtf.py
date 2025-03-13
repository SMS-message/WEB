import json
from flask import Flask, render_template, request, redirect


def main() -> None:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "xcb%h&jk^tx%ds5cfjhkl65t;r4desw'qw\ertyh]gf[dxcs!!!d!r3tr-8004"



    app.run(port=8080, host="127.0.0.1")


if __name__ == '__main__':
    print("http://localhost:8080/")
    main()
