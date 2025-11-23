from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # Komunikacja z worker przez sieć Docker (nazwa usługi: worker)
    try:
        response = requests.get("http://worker:5001/task")
        worker_result = response.text
    except Exception as e:
        worker_result = f"Nie udało się: {e}"

    return f"Serwer App działa, odp. Worker: {worker_result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
