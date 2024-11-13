import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define lists of names and attributes
first_names_male = [
    "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
    "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
    "Luke", "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln",
    "Anthony", "Hudson", "Dylan", "Ezra", "Thomas", "Charles", "Christopher", "Jaxon", "Maverick", "Josiah",
    "Isaiah", "Andrew", "Elias", "Joshua", "Nathan", "Caleb", "Ryan", "Adrian", "Miles", "Eli",
    "Nolan", "Christian", "Aaron", "Cameron", "Ezekiel", "Colton", "Luca", "Landon", "Hunter", "Jonathan",
    "Santiago", "Axel", "Easton", "Cooper", "Jeremiah", "Angel", "Roman", "Connor", "Jameson", "Robert",
    "Greyson", "Jordan", "Ian", "Carson", "Jaxson", "Leonardo", "Nicholas", "Dominic", "Austin", "Everett",
    "Brooks", "Xavier", "Kai", "Jose", "Parker", "Adam", "Jace", "Wesley", "Kayden", "Silas",
    "Bennett", "Declan", "Waylon", "Weston", "Evan", "Emmett", "Micah", "Ryder", "Beau", "Damian",
    "Brayden", "Gael", "Rowan", "Harrison", "Bryson", "Sawyer", "Amir", "King", "Jason", "Giovanni",
    "Vincent", "Ayden", "Chase", "Myles", "Diego", "Nathaniel", "Legend", "Jonah", "River", "Tyler",
    "Cole", "Braxton", "George", "Milo", "Zachary", "Ashton", "Luis", "Jasper", "Kaiden", "Adriel",
    "Gavin", "Bentley", "Calvin", "Zion", "Juan", "Maxwell", "Max", "Ryker", "Carlos", "Emmanuel"
]
first_names_female = [
    "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Charlotte", "Amelia", "Mia", "Harper", "Evelyn",
    "Abigail", "Emily", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila", "Aria",
    "Scarlett", "Penelope", "Layla", "Chloe", "Victoria", "Madison", "Eleanor", "Grace", "Nora", "Riley",
    "Zoey", "Hannah", "Hazel", "Lily", "Ellie", "Violet", "Lillian", "Zoe", "Stella", "Aurora",
    "Natalie", "Emilia", "Everly", "Leah", "Aubrey", "Willow", "Addison", "Lucy", "Audrey", "Bella",
    "Nova", "Brooklyn", "Paisley", "Savannah", "Claire", "Skylar", "Isla", "Genesis", "Naomi", "Elena",
    "Caroline", "Eliana", "Anna", "Maya", "Valentina", "Ruby", "Kennedy", "Ivy", "Ariana", "Aaliyah",
    "Cora", "Madelyn", "Alice", "Kinsley", "Hailey", "Gabriella", "Allison", "Gianna", "Serenity", "Samantha",
    "Sarah", "Autumn", "Quinn", "Eva", "Piper", "Sophie", "Sadie", "Delilah", "Josephine", "Nevaeh",
    "Adeline", "Arya", "Emery", "Lydia", "Clara", "Vivian", "Madeline", "Peyton", "Julia", "Rylee",
    "Brielle", "Reagan", "Natalia", "Jade", "Athena", "Maria", "Leilani", "Everleigh", "Liliana", "Melanie",
    "Mackenzie", "Hadley", "Raelynn", "Kaylee", "Rose", "Arianna", "Isabelle", "Melody", "Eliza", "Lyla",
    "Katherine", "Aubree", "Adalynn", "Kylie", "Faith", "Mary", "Margaret", "Ximena", "Iris", "Alexandra",
    "Jasmine", "Charlie", "Amaya", "Taylor", "Isabel", "Ashley", "Khloe", "Ryleigh", "Alexa", "Amara",
    "Valeria", "Andrea", "Parker", "Norah", "Eden", "Elliana", "Brianna", "Emersyn", "Valerie", "Anastasia"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
    "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
    "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
    "Harrison", "Fernandez", "McDonald", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen",
    "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter",
    "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks",
    "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox",
    "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens",
    "Soto", "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins",
    "Arnold", "Pierce", "Vazquez", "Hansen", "Peters", "Santos", "Hart", "Bradley", "Knight", "Elliott",
    "Cunningham", "Duncan", "Armstrong", "Hudson", "Carroll", "Lane", "Riley", "Andrews", "Alvarado", "Ray",
    "Delgado", "Berry", "Perkins", "Hoffman", "Johnston", "Matthews", "Pena", "Richards", "Contreras", "Willis",
    "Carpenter", "Lawrence", "Sandoval", "Guerrero", "George", "Chapman", "Rios", "Estrada", "Ortega", "Watkins",
    "Greene", "Nunez", "Wheeler", "Valdez", "Harper", "Burke", "Larson", "Santiago", "Maldonado", "Morrison",
    "Franklin", "Carlson", "Austin", "Dominguez", "Carr", "Lawson", "Jacobs", "O'Brien", "Lynch", "Singh",
    "Vega", "Bishop", "Montgomery", "Oliver", "Jensen", "Harvey", "Williamson", "Gilbert", "Dean", "Sims",
    "Espinoza", "Howell", "Li", "Wong", "Reid", "Hanson", "Le", "McCoy", "Garrett", "Burton",
    "Fuller", "Wang", "Weber", "Welch", "Rojas", "Lucas", "Marquez", "Fields", "Park", "Yang",
    "Little", "Banks", "Padilla", "Day", "Walsh", "Bowman", "Schultz", "Luna", "Fowler", "Mejia",
    "Davidson", "Acosta", "Brewer", "May", "Holland", "Juarez", "Newman", "Pearson", "Curtis", "Cortez",
    "Douglas", "Schneider", "Joseph", "Barrett", "Navarro", "Figueroa", "Keller", "Avila", "Wade", "Molina",
    "Stanley", "Hopkins", "Campos", "Barnett", "Bates", "Chambers", "Caldwell", "Beck", "Lambert", "Miranda",
    "Byrd", "Craig", "Ayala", "Lowe", "Frazier", "Powers", "Neal", "Leonard", "Gregory", "Carrillo",
    "Sutton", "Fleming", "Rhodes", "Shelton", "Schwartz", "Norris", "Jennings", "Watts", "Duran", "Walters",
    "Cohen", "McDaniel", "Moran", "Parks", "Steele", "Vaughn", "Becker", "Holt", "DeLeon", "Barker",
    "Terry", "Hale", "Leon", "Hail", "Benson", "Haynes", "Horton", "Miles", "Lyons", "Pham",
    "Graves", "Bush", "Thornton", "Wolfe", "Warner", "Cabrera", "McKinney", "Mann", "Zimmerman", "Dawson",
    "Lara", "Fletcher", "Page", "McCarthy", "Love", "Robles", "Cervantes", "Solis", "Erickson", "Reeves",
    "Chang", "Klein", "Salinas", "Fuentes", "Baldwin", "Daniel", "Simon", "Velasquez", "Hardy", "Higgins",
    "Aguirre", "Lin", "Cummings", "Chandler", "Sharp", "Barber", "Bowen", "Ochoa", "Dennis", "Robbins",
    "Liu", "Ramsey", "Francis", "Griffith", "Paul", "Blair", "O'Connor", "Cardenas", "Pacheco", "Cross",
    "Calderon", "Quinn", "Moss", "Swanson", "Chan", "Rivas", "Khan", "Rodgers", "Serrano", "Fitzgerald",
    "Rosales", "Stevenson", "Christensen", "Manning", "Gill", "Curry", "McLaughlin", "Harmon", "McGee", "Gross",
    "Doyle", "Garner", "Newton", "Burgess", "Reese", "Walton", "Blake", "Trujillo", "Adkins", "Brady",
    "Goodman", "Roman", "Webster", "Goodwin", "Fischer", "Huang", "Potter", "Delacruz", "Montoya", "Todd",
    "Wu", "Hines", "Mullins", "Castaneda", "Malone", "Cannon", "Tate", "Mack", "Sherman", "Hubbard"
]

# Define lists of names and attributes
races = ["White", "Black", "Asian", "Native American"]
race_map = {race: i for i, race in enumerate(races)}  
genders = ["Male", "Female"]
lifestyles = ["Smoker", "Non-Smoker", "Active", "Sedentary"]
lifestyle_map = {lifestyle: i for i, lifestyle in enumerate(lifestyles)}

# Function to calculate BMI
def calculate_bmi(weight_lbs, height_inches):
    return (weight_lbs / (height_inches ** 2)) * 703

# Generate synthetic patient data
def generate_patient(patient_id):
    gender = random.choice(genders)
    if gender == "Male":
        first_name = random.choice(first_names_male)
        weight = random.uniform(130, 265)  # lbs
        height = random.uniform(64, 79)    # inches
        #gender_id = 1
    else:
        first_name = random.choice(first_names_female)
        weight = random.uniform(110, 220)  # lbs
        height = random.uniform(59, 71)    # inches
        #gender_id = 0
    last_name = random.choice(last_names)
    race = random.choice(races)
    #race_id = race_map[race]
    age = random.randint(18, 90)  # Added Age
    lifestyle = random.choice(lifestyles)
    #lifestyle_id = lifestyle_map[lifestyle]
    return {
        'Patient ID': patient_id,
        'First_Name': first_name,
        'Last_Name': last_name,
        'Gender': gender,
        'Race': race,
        'Age': age,
        'Weight (lbs)': round(weight, 2),
        'Height (inches)': round(height, 2),
        'Lifestyle': lifestyle
    }

# Adjusted disease probability functions
def hypertension_probability(patient):
    prob = 0.10
    bmi = calculate_bmi(patient['Weight (lbs)'], patient['Height (inches)'])
    if bmi > 25:
        prob += 0.01 * (bmi - 25)
    if patient['Gender'] == 1:  # Male
        prob += 0.03
    if patient['Age'] > 50:
        prob += 0.05
    if patient['Lifestyle'] == 0:  # Smoker
        prob += 0.02
    return min(max(prob, 0), 1)

def diabetes_probability(patient):
    prob = 0.08
    bmi = calculate_bmi(patient['Weight (lbs)'], patient['Height (inches)'])
    if bmi > 30:
        prob += 0.02 * (bmi - 30)
    if patient['Age'] > 45:
        prob += 0.04
    if patient['Lifestyle'] == 3:  # Sedentary
        prob += 0.03
    return min(max(prob, 0), 1)

def heart_disease_probability(patient):
    prob = 0.07
    bmi = calculate_bmi(patient['Weight (lbs)'], patient['Height (inches)'])
    if bmi > 25:
        prob += 0.01 * (bmi - 25)
    if patient['Age'] > 50:
        prob += 0.04
    if patient['Lifestyle'] == 0:  # Smoker
        prob += 0.03
    return min(max(prob, 0), 1)

def asthma_probability(patient):
    prob = 0.05
    if patient['Race'] == race_map['Black']:
        prob += 0.03
    if patient['Lifestyle'] == 0:  # Smoker
        prob += 0.02
    return min(max(prob, 0), 1)

def cancer_probability(patient):
    prob = 0.05
    bmi = calculate_bmi(patient['Weight (lbs)'], patient['Height (inches)'])
    if bmi > 30:
        prob += 0.01 * (bmi - 30)
    if patient['Age'] > 60:
        prob += 0.03
    return min(max(prob, 0), 1)

def anxiety_probability(patient):
    prob = 0.15
    if patient['Lifestyle'] == 3:  # Sedentary
        prob += 0.03
    return min(max(prob, 0), 1)

def assign_disease(patient):
    diseases = ['Hypertension', 'Diabetes', 'Heart Disease', 'Asthma', 'Cancer', 'Anxiety', 'Healthy']
    probabilities = [
        hypertension_probability(patient),
        diabetes_probability(patient),
        heart_disease_probability(patient),
        asthma_probability(patient),
        cancer_probability(patient),
        anxiety_probability(patient)
    ]
    prob_healthy = 1 - sum(probabilities)
    prob_healthy = max(prob_healthy, 0)
    probabilities.append(prob_healthy)
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]
    disease = random.choices(diseases, weights=probabilities, k=1)[0]
    return disease

# Generate patients and assign diseases
num_patients = 10000
patient_list = []

for i in range(1, num_patients + 1):
    patient_id = "synth_" + str(i)
    patient = generate_patient(patient_id)
    patient['Disease'] = assign_disease(patient)
    bmi = calculate_bmi(patient['Weight (lbs)'], patient['Height (inches)'])
    patient['Obesity'] = 'yes' if bmi >= 30 else 'no'
    patient_list.append(patient)

# Create DataFrame
df = pd.DataFrame(patient_list)

# Convert Disease names to IDs
#Disease_dict = {
#    'Hypertension': 1, 'Diabetes': 2, 'Heart Disease': 3, 'Asthma': 4,
#    'Cancer': 5, 'Anxiety': 6, 'Healthy': 7
#}
#df['Disease ID'] = df['Disease'].map(Disease_dict)

# Finalize DataFrame with only numeric columns
df = df[['Patient ID','First_Name', 'Last_Name', 'Gender', 'Race', 'Age', 'Weight (lbs)', 'Height (inches)',
         'Lifestyle', 'Obesity', 'Disease']]

# Check distribution of diseases
#disease_counts = df['Disease ID'].value_counts(normalize=True) * 100
#print("Disease Distribution (%):")
#print(disease_counts)

# Plot the distribution
#plt.figure(figsize=(10, 6))
#sns.barplot(x=disease_counts.index, y=disease_counts.values)
#plt.xlabel('Disease ID')
#plt.ylabel('Percentage')
#plt.title('Distribution of Disease IDs in Generated Data')
#plt.show()

# Save DataFrame to CSV
df.to_csv('patients2.csv', index=False)
print("Generated dataset saved to 'patients1.csv'")
