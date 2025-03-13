from flask import Flask, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '123kjg13231j83b3oi3=-9a[sf'


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
    return f'''<h1>Жди нас, Марс!</h1>
                <img src="{url_for("static", filename="img/mars.png")}" alt="Тут должна быть картинка марса.">
                <p>Вот она какая, красная планета.</p>'''

@app.route("/promotion_image")
def promotion_image():
    res = f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="static/css/style1.css">
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for("static", filename="img/mars.png")}" alt="Тут должна быть картинка марса.">
'''

    lst = ["Человечество вырастает из детства.",
           "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.",
           "И начнем с Марса!",
           "Присоединяйся!",
           ]
    for i in lst:
        res += f"\n<p>{i}</p>"
    res += '''
                </body>
                </html>'''
    return res

@app.route("/choice/<planet_name>")
def choice(planet_name):
    res = f'''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <link rel="stylesheet" href="{url_for("static", filename="css/style2.css")}">
                    </head>
                    <body>
                        <h1>Моё предложение: {planet_name}</h1>
    '''

    lst = ["Эта планета близка к Земле;",
           "На ней много необходимых ресурсов;",
           "На ней есть вода и атмосфера;",
           "На ней есть небольшое магнитное поле;",
           "Наконец, она просто красива!",
           ]
    for i in lst:
        res += f"\n<p>{i}</p>"
    res += '''
                    </body>
                    </html>'''
    return res

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    res = f'''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <link rel="stylesheet" href="{url_for("static", filename="css/style3.css")}">
                        </head>
                        <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие в миссии {nickname}:</h2>
        '''
    lst = [f"Поздравляем! Ваш рейтинг после {level} этапа отбора",
           f"составляет {rating}",
           "Желаем удачи!",
           ]
    for i in lst:
        res += f"\n<p>{i}</p>"
    res += '''
                        </body>
                        </html>'''
    return res
app.run(port=8080, host="127.0.0.1")
