import requests

print(requests.get("http://127.0.0.1:8080/ranking/Hottab").json())
print(requests.get("http://127.0.0.1:8080/ranking/Phenex").json())