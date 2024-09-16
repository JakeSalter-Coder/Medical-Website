import pandas as pd
import random

# Define possible values for each category
races = ['White', 'African American', 'Asian', 'Native American', 'Hispanic']
genders = ['Male', 'Female']
diseases = ['Hypertension', 'Diabetes', 'Heart Disease', 'Asthma', 'Cancer', 'Depression', 'Arthritis', 'Chronic Kidney Disease', 'Obesity', 'Anxiety']
first_names_male = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas',
 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua',
 'George', 'Kenneth', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan',
 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon',
 'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry',
 'Tyler', 'Aaron', 'Henry', 'Douglas', 'Peter', 'Adam', 'Nathan', 'Zachary', 'Walter', 'Kyle',
 'Carl', 'Arthur', 'Gerald', 'Roger', 'Keith', 'Jeremy', 'Terry', 'Lawrence', 'Sean', 'Christian',
 'Albert', 'Joe', 'Ethan', 'Austin', 'Jesse', 'Willie', 'Billy', 'Bruce', 'Bryan', 'Jordan',
 'Ralph', 'Roy', 'Noah', 'Dylan', 'Eugene', 'Wayne', 'Alan', 'Juan', 'Louis', 'Russell',
 'Elijah', 'Vincent', 'Bobby', 'Philip', 'Logan', 'Derek', 'Randy', 'Howard', 'Jared', 'Shawn']

first_names_females = ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
 'Nancy', 'Lisa', 'Margaret', 'Betty', 'Sandra', 'Ashley', 'Dorothy', 'Kimberly', 'Emily', 'Donna',
 'Michelle', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Laura', 'Sharon', 'Cynthia',
 'Kathleen', 'Amy', 'Angela', 'Shirley', 'Anna', 'Brenda', 'Pamela', 'Emma', 'Nicole', 'Helen', 'Samantha',
 'Katherine', 'Christine', 'Debra', 'Rachel', 'Carolyn', 'Janet', 'Catherine', 'Maria', 'Heather', 'Diane',
 'Virginia', 'Julie', 'Joyce', 'Victoria', 'Kelly', 'Christina', 'Lauren', 'Joan', 'Evelyn', 'Olivia',
 'Judith', 'Megan', 'Cheryl', 'Andrea', 'Hannah', 'Martha', 'Jacqueline', 'Frances', 'Gloria', 'Ann',
 'Teresa', 'Kathryn', 'Sara', 'Janice', 'Jean', 'Alice', 'Madison', 'Doris', 'Abigail', 'Julia',
 'Judy', 'Grace', 'Denise', 'Amber', 'Marilyn', 'Beverly', 'Danielle', 'Theresa', 'Sophia', 'Marie',
 'Diana', 'Brittany', 'Natalie', 'Isabella', 'Charlotte', 'Rose', 'Alexis', 'Kayla', 'Lillian', 'Victoria']

last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright',
 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Gonzalez',
 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards',
 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy',
 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Peterson', 'Gray', 'Ramirez',
 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross',
 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington',
 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes',
 'Myers', 'Ford', 'Hamilton', 'Graham', 'Sullivan', 'Wallace', 'Woods', 'Cole', 'West', 'Jordan',
 'Owens', 'Reynolds', 'Fisher', 'Ellis', 'Harrison', 'Gibson', 'McDonald', 'Cruz', 'Marshall', 'Ortiz',
 'Gomez', 'Murray', 'Freeman', 'Wells', 'Webb', 'Simpson', 'Stevens', 'Tucker', 'Porter', 'Hunter',
 'Hicks', 'Crawford', 'Henry', 'Boyd', 'Mason', 'Morales', 'Kennedy', 'Warren', 'Dixon', 'Ramos',
 'Reyes', 'Burns', 'Gordon', 'Shaw', 'Holmes', 'Rice', 'Robertson', 'Hunt', 'Black', 'Daniels',
 'Palmer', 'Mills', 'Nichols', 'Grant', 'Knight', 'Ferguson', 'Rose', 'Stone', 'Hawkins', 'Dunn',
 'Perkins', 'Hudson', 'Spencer', 'Gardner', 'Stephens', 'Payne', 'Pierce', 'Berry', 'Matthews', 'Arnold',
 'Wagner', 'Willis', 'Ray', 'Watkins', 'Olson', 'Carroll', 'Duncan', 'Snyder', 'Hart', 'Cunningham',
 'Bradley', 'Lane', 'Andrews', 'Ruiz', 'Harper', 'Fox', 'Riley', 'Armstrong', 'Carpenter', 'Weaver',
 'Greene', 'Lawrence', 'Elliott', 'Chavez', 'Sims', 'Austin', 'Peters', 'Kelley', 'Franklin', 'Lawson']

# Create a list to store mock data
data = []

# Function to generate random weight based on age and gender
def generate_weight(age, gender):
    if age < 18:
        return random.randint(30,200 )  # Child/Teen weight range
    if gender == 'Male':
        return random.randint(160, 600)  # Adult male weight range
    elif gender == 'Female':
        return random.randint(120, 400)  # Adult female weight range
    else:
        return random.randint(120, 500)  # Other genders weight range

# Function to generate random height based on gender
def generate_height(gender):
    if gender == 'Male':
        return round(random.uniform(4, 7), 1)  # Male height range in ft
    elif gender == 'Female':
        return round(random.uniform(4, 7), 1)  # Female height range in ft
    else:
        return round(random.uniform(4, 7), 1)  # Other genders height range in ft

# Generate 1000 mock people
for i in range(1000):
    id = i
    age = random.randint(1, 100)  # Age range from 1 to 100
    gender = random.choice(genders)
    race = random.choice(races)
    weight = generate_weight(age, gender)
    height = generate_height(gender)
    disease = random.choice(diseases)
    if gender == 'Male':
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_females)
    last_name = random.choice(last_names)
    
    # Append the generated data as a row in the dataset
    data.append([id, first_name, last_name, race, age, gender, weight, height, disease])

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['ID', 'First_Name', 'Last_Name','Race', 'Age', 'Gender', 'Weight', 'Height', 'Disease'])

# Save the dataset to a CSV file
df.to_csv('mock_people_data.csv', index=False)

# Show the first 5 rows of the dataset
df.head()
