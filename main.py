
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    height = request.form['height']
    weight = request.form['weight']
    race = request.form['race']
    user_input = name + " " + age + " " + gender + " " + height + " " + weight + " " + race
    print(user_input)
    return '/'


@app.route("/quit")
def _quit():
    exit(0)


if __name__ == '__main__':
    app.run(host='localhost', port=4560, debug=True)
