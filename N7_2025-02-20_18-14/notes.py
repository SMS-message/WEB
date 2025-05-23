def http() -> None:
    from http.server import HTTPServer, CGIHTTPRequestHandler
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


def flask() -> None:
    from flask import Flask, url_for, request

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

    i = 0

    @app.route("/show_i")
    def show_i() -> str:
        nonlocal i
        i += 1
        return f"Посещение: {i}"

    @app.route("/parameters/<username>/<int:n>")
    def parameters(username, n) -> str:
        return f"Привет, {username}. Твоё любимое число - {n}."

    @app.route('/form_sample', methods=['POST', 'GET'])
    def form_sample():
        if request.method == 'GET':
            return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Форма для регистрации в суперсекретной системе</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                        <div class="form-group">
                                            <label for="classSelect">В каком вы классе</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>7</option>
                                              <option>8</option>
                                              <option>9</option>
                                              <option>10</option>
                                              <option>11</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="about">Немного о себе</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
        elif request.method == 'POST':
            print(request.form['email'])
            print(request.form['password'])
            print(request.form['class'])
            print(request.form['file'])
            print(request.form['about'])
            print(request.form['accept'])
            print(request.form['sex'])
            return "Форма отправлена"

    app.run(port=8080, host="localhost")

if __name__ == '__main__':
    flask()
