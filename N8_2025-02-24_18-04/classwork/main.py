from flask import Flask, render_template, url_for


def main():
    app = Flask(__name__)


    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("base.html", title="Заготовка")

    @app.route("/training/<prof>")
    def training(prof):
        file = "engineer_practice.jpg" if "строитель" in prof or "инженер" in prof else "science_simulators.png"
        params = {
            "title": "Симуляторы и тренажёры",
            "prof": prof,
            "source": url_for("static", filename=f"img/{file}")
        }
        return render_template("training.html", **params)

    app.run(port=2003, host="127.0.0.1")

if __name__ == '__main__':
    main()
