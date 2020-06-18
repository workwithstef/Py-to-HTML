from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/bye")
def bye():
    return "Goodbye World!"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/airbnb")
def airbnb():
    return render_template("airbnb.html")


if __name__ == '__main__':
    app.run(debug=True)

