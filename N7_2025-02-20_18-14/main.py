from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def root():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    lst = ["Человечество вырастает из детства.",
           "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.",
           "И начнем с Марса!",
           "Присоединяйся!",
           ]
    return "<br>".join(lst)

@app.route("/image_mars")
def image_mars():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%259C%25D0%25B0%25D1%2580%25D1%2581&psig=AOvVaw2SMtPBINy1pv16dW1P-oBj&ust=1740155997372000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMDRs7LY0osDFQAAAAAdAAAAABAE"
    return f'''<h1>Жди нас, Марс!</h1>
                <img src="{url}" alt="Тут должна быть картинка марса.">
                <p>Вот она какая, красная планета.</p>'''


app.run(port=8080, host="127.0.0.1")
