# Fabricated Doctor's Office Data
import sqlite3
import random
from datetime import datetime, timedelta

# open sqlite connection
con = sqlite3.connect("clinicData.db")
cur = con.cursor()

# create tables
cur.executescript("""
DROP TABLE IF EXISTS Patient;
DROP TABLE IF EXISTS Provider;
DROP TABLE IF EXISTS Appointment;
DROP TABLE IF EXISTS Bill;

CREATE TABLE Patient (
    patient_id INTEGER PRIMARY KEY,
    name TEXT,
    dob DATE,
    phone TEXT,
    address TEXT
);

CREATE TABLE Provider (
    provider_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT,
    specialty TEXT
);

CREATE TABLE Appointment (
    appt_id INTEGER PRIMARY KEY,
    appt_date DATE,
    patient_id INTEGER,
    provider_id INTEGER,
    diagnosis TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (provider_id) REFERENCES Provider(provider_id)
);

CREATE TABLE Bill (
    bill_id INTEGER PRIMARY KEY,
    date DATE,
    patient_id INTEGER,
    amount REAL,
    status TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);
""")

# create 100 rows for Patient
# fabricated values
names = [
    "Alex Smith", "Jamie Johnson", "Taylor Brown", "Jordan Davis", "Casey Miller",
    "Morgan Wilson", "Riley Moore", "Skyler Taylor", "Cameron Anderson", "Avery Thomas",
    "Harper White", "Reese Martin", "Quinn Thompson", "Emerson Garcia", "Finley Martinez",
    "Parker Robinson", "Rowan Clark", "Drew Rodriguez", "Logan Lewis", "Sawyer Lee",
    "Alex Walker", "Jamie Hall", "Taylor Allen", "Jordan Young", "Casey Hernandez",
    "Morgan King", "Riley Wright", "Skyler Lopez", "Cameron Hill", "Avery Scott",
    "Harper Green", "Reese Adams", "Quinn Baker", "Emerson Nelson", "Finley Carter",
    "Parker Mitchell", "Rowan Perez", "Drew Roberts", "Logan Turner", "Sawyer Phillips",
    "Alex Campbell", "Jamie Parker", "Taylor Evans", "Jordan Edwards", "Casey Collins",
    "Morgan Stewart", "Riley Sanchez", "Skyler Morris", "Cameron Rogers", "Avery Reed",
    "Harper Cook", "Reese Morgan", "Quinn Bell", "Emerson Murphy", "Finley Bailey",
    "Parker Rivera", "Rowan Cooper", "Drew Richardson", "Logan Cox", "Sawyer Howard",
    "Alex Ward", "Jamie Torres", "Taylor Peterson", "Jordan Gray", "Casey Ramirez",
    "Morgan James", "Riley Watson", "Skyler Brooks", "Cameron Kelly", "Avery Sanders",
    "Harper Price", "Reese Bennett", "Quinn Wood", "Emerson Barnes", "Finley Ross",
    "Parker Henderson", "Rowan Coleman", "Drew Jenkins", "Logan Perry", "Sawyer Powell",
    "Alex Long", "Jamie Patterson", "Taylor Hughes", "Jordan Flores", "Casey Washington",
    "Morgan Butler", "Riley Simmons", "Skyler Foster", "Cameron Gonzales", "Avery Bryant",
    "Harper Alexander", "Reese Russell", "Quinn Griffin", "Emerson Diaz", "Finley Hayes",
    "Parker Myers", "Rowan Ford", "Drew Hamilton", "Logan Graham", "Sawyer Sullivan"
]
street_names = [
    "Maple Street", "Oak Avenue", "Pine Lane", "Cedar Road", "Elm Drive",
    "Birch Street", "Willow Way", "Spruce Court", "Ash Boulevard", "Chestnut Circle",
    "Sycamore Street", "Magnolia Lane", "Poplar Avenue", "Hickory Road", "Redwood Drive",
    "Juniper Way", "Laurel Street", "Dogwood Court", "Beech Circle", "Alder Drive",
    "Fir Street", "Hemlock Lane", "Cypress Road", "Sequoia Boulevard", "Rowan Avenue",
    "Holly Street", "Linden Court", "Buckeye Circle", "Cottonwood Drive", "Banyan Lane",
    "Walnut Street", "Locust Avenue", "Mulberry Road", "Maplewood Drive", "Ashcroft Lane",
    "Riverbend Road", "Sunnydale Street", "Clearwater Avenue", "Brookside Court", "Meadowview Drive"
]
city_names = ["Burlington", "Colchester", "Winooski", "Essex", "Willison"]

# create list of all values
patients = []
for i in range(100):
    patient_id = i + 1
    patient_name = names[i]
    dob = (datetime(1930, 1, 1) + timedelta(days=random.randint(0, 30000))).strftime("%Y-%m-%d")
    phone = f"802{random.randint(1000000,9999999):04d}"
    address = f"{random.randint(100,999)} {random.choice(street_names)} {random.choice(city_names)} VT"
    patients.append((patient_id, patient_name, dob, phone, address))

# insert list into Patient table
cur.executemany("INSERT INTO Patient VALUES (?, ?, ?, ?, ?);", patients)

# create 20 rows for Provider
# fabricated values
provider_names = [
    "Ethan Harrison", "Maya Richards", "Liam Foster", "Zoe Turner", "Noah Walker",
    "Emma Carter", "Oliver Lewis", "Ava Mitchell", "Lucas Scott", "Sophia White",
    "Mason Clark", "Isabella Martinez", "James Harris", "Amelia King", "Benjamin Thompson",
    "Charlotte Rodriguez", "Henry Nelson", "Evelyn Adams", "Jack Davis", "Grace Young"
]
specialties = ["Pediatrics", "Cardiology", "Psychiatry", "Dermatology", "Neurology", "Oncology", "General Medicine"]
emails = [
    "ethanharrison@burlingtonhealth.com", "mayarichards@burlingtonhealth.com", "liamfoster@burlingtonhealth.com",
    "zoeturner@burlingtonhealth.com", "noahwalker@burlingtonhealth.com", "emmacarter@burlingtonhealth.com",
    "oliverlewis@burlingtonhealth.com", "avamitchell@burlingtonhealth.com", "lucasscott@burlingtonhealth.com",
    "sophiawhite@burlingtonhealth.com", "masonclark@burlingtonhealth.com", "isabellamartinez@burlingtonhealth.com",
    "jamesharris@burlingtonhealth.com", "ameliaKing@burlingtonhealth.com", "benjaminthompson@burlingtonhealth.com",
    "charlotterodriguez@burlingtonhealth.com", "henrynelson@burlingtonhealth.com", "evelynadams@burlingtonhealth.com",
    "jackdavis@burlingtonhealth.com", "graceyoung@burlingtonhealth.com"
]

# create list of all values
providers = []
for i in range(20):
    provider_id = i + 1
    provider_name = provider_names[i]
    phone = f"802656{random.randint(1000,9999):04d}"
    email = emails[i]
    specialty = random.choice(specialties)
    providers.append((provider_id, provider_name, phone, email, specialty))

# insert list into Provider table
cur.executemany("INSERT INTO Provider VALUES (?, ?, ?, ?, ?);", providers)

# create 200 rows for Appointment
# fabricated values
diagnoses = ["Flu", "Strep Throat", "Neurovirus", "UTI", "COVID-19", "Migraine", "Allergy", "Food Poisoning", "Ear Infection", "Sinus Infection"]

# create list of all values
appointments = []
for i in range(200):
    appointment_id = i + 1
    date = (datetime.now() - timedelta(days=random.randint(0, 730))).strftime("%Y-%m-%d")
    patient_id = random.choice(patients)[0]
    provider_id = random.choice(providers)[0]
    diagnosis = random.choice(diagnoses)
    appointments.append((appointment_id, date, patient_id, provider_id, diagnosis))

# insert list into Appointment table
cur.executemany("INSERT INTO Appointment VALUES (?, ?, ?, ?, ?);", appointments)

# create 100 rows for Bill
# create list of all values
statuses = ["Unpaid", "Paid", "Cancelled"]
bills = []
for i in range(100):
    bill_id = i + 1
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    patient_id = random.choice(patients)[0]
    amount = round(random.uniform(50, 1000), 2)
    status = random.choice(statuses)
    bills.append((bill_id, date, patient_id, amount, status))
cur.executemany("INSERT INTO Bill VALUES (?, ?, ?, ?, ?);", bills)

# close sqlite connection
con.commit()
con.close()