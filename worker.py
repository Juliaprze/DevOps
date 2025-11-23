from flask import Flask

app = Flask(__name__)

@app.route("/task")
def task():
    return "Worker działa OK!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
