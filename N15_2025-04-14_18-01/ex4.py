import sqlite3

genie = input()
db_filename = input()

con = sqlite3.connect(db_filename)
cur = con.cursor()

state_id = list(cur.execute(f"SELECT state_id FROM Genies WHERE genie='{genie}';"))
state_id = state_id[0][0]
drugs = list(cur.execute(f"SELECT drug, state_id FROM Drugs WHERE state_id='{state_id}'"))

drugs = list(map(list, drugs))

for i, item in enumerate(drugs):
    strength = list(cur.execute(f"SELECT strength FROM States WHERE id='{state_id}'"))
    item.extend(strength[0])

drugs = list(map(lambda y: y[0], filter(lambda x: len(x[0]) % 2 != x[-1] % 2, drugs)))

print(*sorted(drugs, key=lambda x: (-len(x), x)), sep="\n")
