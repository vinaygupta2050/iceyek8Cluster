from flask import Flask

PORT = 8000

app = Flask(__name__)


@app.route('/<string:name>/')
def hello(name):
    MESSAGE = "Hi there, "+ name +"!"
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
