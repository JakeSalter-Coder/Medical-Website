
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)


@app.route("/quit")
def _quit():
    exit(0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3240)
