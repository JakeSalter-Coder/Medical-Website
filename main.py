from operator import truediv

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Superpie1@'
app.config['MYSQL_DB'] = 'Final_Project'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CONNECT_TIMEOUT'] = 60

mysql = MySQL(app)

def insert_new_patients(user_input):
    try:
        # Create a cursor object
        conn = mysql.connection
        if conn is None:
            print("Issue with connection")
            return
        cur = conn.cursor()
        # Grabs the number of patients logged to find the new patients ID
        cur.execute("SELECT COUNT(*) FROM User_Information")
        patient_id = f"auth_{cur.fetchone()[0]+1}"

        # Grabs disease ID from disease name
        cur.execute(f"SELECT Disease_ID FROM Disease WHERE Disease_Name='{user_input['disease']}'")
        disease_id = cur.fetchone()[0]

        # Determines if the user is obese, based on height and weight
        is_obese = check_obese(user_input["height"], user_input["weight"])

        # Converts height from inches to a formatted string in feet and inches (e.g., "5 ft 10 in").
        formatted_height = user_input["height"]
        formatted_height = f"{formatted_height // 12} ft {formatted_height % 12} in"

        # Concat values into a single list
        values = (patient_id,
                  user_input['first_name'],
                  user_input['last_name'],
                  user_input['race'],
                  user_input['weight'],
                  formatted_height,
                  user_input['gender'],
                  is_obese,
                  disease_id)

        # Insert data into the database
        insert = """INSERT INTO User_Information(Patient_ID, First_name, Last_name, 
                                                 Race, Weight, Height, Gender, Obesity, Disease_ID) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cur.execute(insert, values)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")


def check_obese(height_inches, weight_lbs):
    height_meters = height_inches * 0.0254
    weight_kilograms = weight_lbs * 0.453592
    bmi = weight_kilograms / (height_meters ** 2)
    if bmi >= 30:
        return True
    else:
        return False

@app.route('/')
def index():
    # connect to db
    conn = mysql.connection
    if conn is None:
        print("Issue with connection")
    cur = conn.cursor()
    # grab all logged diseases
    cur.execute("SELECT DISTINCT disease_name FROM Disease")
    currently_logged_diseases = cur.fetchall()
    currently_logged_diseases = [row[0] for row in currently_logged_diseases]
    return render_template('index.html', diseases=currently_logged_diseases)


@app.route('/submit', methods=['POST'])
def index_post():
    data = request.get_json()

    # grab data from json object
    user_input = {
        "first_name": data.get('first_name'),
        "last_name": data.get('last_name'),
        "age": data.get('age'),
        "gender": data.get('gender'),
        "height": data.get('height_ft') * 12 + data.get('height_in'),
        "weight": data.get('weight'),
        "race": data.get('race'),
        "disease": data.get('disease'),
        "consent": data.get('consent')
    }
    app.logger.info(user_input)
    if user_input["disease"] != "None" and user_input["consent"] == True:
        insert_new_patients(user_input)

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
