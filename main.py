
import pandas as pd
import joblib
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from utils.model import train_model

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Superpie1@'
app.config['MYSQL_DB'] = 'Final_Project'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CONNECT_TIMEOUT'] = 60

mysql = MySQL(app)

disease_recs = {
    "Hypertension": "https://www.cdc.gov/high-blood-pressure/about/index.html%E2%80%8B",
    "Diabetes": "https://www.cdc.gov/diabetes/about/index.html%E2%80%8B",
    "Heart Disease": "https://www.cdc.gov/heart-disease/about/index.html%E2%80%8B",
    "Asthma": "https://www.cdc.gov/asthma/about/index.html%E2%80%8B",
    "Cancer": "https://www.cdc.gov/cancer/index.html%E2%80%8B",
    "Depression": "https://www.who.int/news-room/fact-sheets/detail/depression%E2%80%8B",
    "Arthritis": "https://www.cdc.gov/arthritis/index.html%E2%80%8B",
    "Chronic Kidney Disease": "https://www.cdc.gov/kidney-disease/index.html%E2%80%8B",
    "Anxiety": "https://medlineplus.gov/anxiety.html#:~:text=Anxiety%20is%20a%20feeling%20of,before%20making%20an%20important%20decision"
}


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
        insert = """
            INSERT INTO User_Information(Patient_ID, First_name, Last_name, 
                                         Race, Weight, Height, Gender, Obesity, Disease_ID) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
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

def get_model():
    conn = mysql.connection
    if conn is None:
        print("Issue with connection")
        return
    cur = conn.cursor()

    # Gets all user information in the database to fit Random Forest
    cur.execute("""
        SELECT Race,Weight,Gender,Obesity, Disease_ID FROM Synthetic_data
        UNION 
        SELECT Race,Weight,Gender,Obesity, Disease_ID FROM User_Information
        """)

    # Build dataframes for fitting
    patient_data = pd.DataFrame(cur.fetchall(), columns=["race", "weight", "gender", "obesity", "disease_id", "Lifestyle","Age"])
    disease_data = patient_data["disease_id"]
    patient_data = patient_data.iloc[::, :-1]
    patient_data["gender"] = patient_data["gender"].map({'Male':0, 'Female':1})
    patient_data["race"] = patient_data["race"].map({'White':0, 'Black':1, 'Asian':2, 'Hispanic':3})
     patient_data["Lifestyle"] = patient_data["Lifestyle"].map({'Smoker':0, 'Non-Smoker':1, 'Active':2, 'Sedentary':3})

    return train_model(patient_data, disease_data)

# Train and return the Random Forest model for predictions
with app.app_context():
    print("Loading model")
    try:
        model = joblib.load("models/rf_model.pkl")
    except FileNotFoundError:
        print("Model not found.\nFitting model...")
        model = get_model()
        print("Model trained.")
    print("Model loaded.")

@app.route('/')
def index():
    # Connect to db
    conn = mysql.connection
    if conn is None:
        print("Issue with connection")
    cur = conn.cursor()

    # Grab all logged diseases
    cur.execute("SELECT DISTINCT disease_name FROM Disease")
    currently_logged_diseases = cur.fetchall()
    currently_logged_diseases = [row[0] for row in currently_logged_diseases]

    return render_template('index.html', diseases=currently_logged_diseases)


@app.route('/submit', methods=['POST'])
def index_post():
    data = request.get_json()

    # Grab data from json object
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

    # Adds user data to database
    if user_input["disease"] != "None" and user_input["consent"] == True:
        insert_new_patients(user_input)

    # Convert string Race into int index
    user_race_index = -1
    if user_input["race"] == "White":
        user_race_index = 0
    elif user_input["race"] == "Black":
        user_race_index = 1
    elif user_input["race"] == "Asian":
        user_race_index = 2
    elif user_input["race"] == "Hispanic":
        user_race_index = 3

    # Convert string Gender into int index
    user_gender_index = -1
    if user_input["gender"] == "Male":
        user_gender_index = 0
    elif user_input["gender"] == "Female":
        user_gender_index = 1

    # Convert string Lifestyle into int index
    user_Lifestyle_index = -1
    if user_input["Lifestyle"] == "Smoker":
        user_Lifestyle_index = 0
    elif user_input["Lifestyle"] == "Non-Smoker":
        user_Lifestyle_index = 1
    elif user_input["Lifestyle"] == "Active":
        user_Lifestyle_index = 2
    elif user_input["Lifestyle"] == "Sedentary":
        user_Lifestyle_index = 3
    
    # Build dataframe from user data
    user_data = pd.DataFrame({
        'race': [user_race_index],
        'weight': [user_input["weight"]],
        'gender': [user_gender_index],
        'obesity': [check_obese(user_input["height"], user_input["weight"])],
        'Lifestyle': [user_Lifestyle_index]
    })

    # Prediction from model based on user data
    prediction = model.predict(user_data)[0]

    # Connect to db to gtab prediction name
    conn = mysql.connection
    if conn is None:
        print("Issue with connection")
    cur = conn.cursor()
    cur.execute(f"SELECT Disease_Name FROM Disease WHERE Disease_ID = {prediction}")
    predicted_disease = cur.fetchone()[0]

    # Return prediction to user
    response = {
        'status': 'success',
        'prediction': predicted_disease,
        'rec': disease_recs[predicted_disease]
    }
    return jsonify(response)

@app.route("/quit")
def _quit():
    exit(0)


if __name__ == '__main__':
    app.run(host='localhost', port=4560, debug=True)
