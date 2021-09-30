from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return 'У меня работает! Что то ты делаешь не так.'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)