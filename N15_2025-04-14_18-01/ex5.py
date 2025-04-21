from flask import Flask, jsonify
import csv
import sqlite3

app = Flask(__name__)


@app.route("/ranking/<genie>")
def ranking(genie):
    with open('dignity.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        data = [list(map(lambda x: int(x) if x.isdigit() else x, i)) for i in reader][1:]
        for row in data:
            if genie in row:
                con = sqlite3.connect("honor.db")
                cur = con.cursor()
                req = f"SELECT liter FROM Liters WHERE id in (SELECT liter_id FROM Ranks WHERE id='{row[3]}')"
                g_lit = list(cur.execute(req))[0]
                g_place = row[2]
                g_level = row[4]

    data = list(filter(lambda x: x[2] != g_place, data))

    ans = []

    for item in data:
        i, name, place, rank, level = item
        req = f"SELECT liter FROM Liters WHERE id in (SELECT liter_id FROM Ranks WHERE id='{rank}')"
        lit = list(cur.execute(req))[0]
        if lit > g_lit or level < g_level:
            ans.append((name, level))

    return jsonify(list(map(lambda y: y[0], sorted(ans, key=lambda x: (x[1], x[0]))))[:5])


app.run(host="127.0.0.1", port=8080)
