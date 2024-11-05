
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abacab#2024'
app.config['MYSQL_DB'] = 'BOOKS_DB'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

def connect():
    try:
        # Create a cursor object
        conn = mysql.connection
        if conn == None:
            print("Issue with connection")
        cur = conn.cursor()
        
        # Insert data into the database
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", ('Derek', 'Credland'))
        
        # Commit changes
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")


@app.route('/')
def index():
    connc = mysql.connection
    if connc == None:
        print("Issue with connection")
    cur = connc.cursor()
    currently_logged_diseases = cur.execute("SELECT DISTINC disease_name FROM DISEASE")
    return render_template('index.html', )


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

    connect()
    
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
