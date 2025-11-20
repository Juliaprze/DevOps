from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Dockerized Python World!"

@app.route('/about')
def about():
    return "To jest prosty endpoint /about w aplikacji Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
