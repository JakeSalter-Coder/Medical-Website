
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', success=None)


@app.route('/submit', methods=['POST'])
def index_post():
    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    age = data.get('age')
    gender = data.get('gender')
    height = data.get('height')
    weight = data.get('weight')
    race = data.get('race')
    user_input = first_name + " " + last_name + " " + age + " " + gender + " " + height + " " + weight + " " + race
    print(user_input)
    app.logger.info(user_input)

    response = {
        'status': 'success',
        'message': 'Data received successfully',
        'received_data': data
    }
    return jsonify(response)

@app.route("/quit")
def _quit():
    exit(0)


if __name__ == '__main__':
    app.run(host='localhost', port=4560, debug=True)
