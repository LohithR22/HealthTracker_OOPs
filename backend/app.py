from flask import Flask, jsonify, request
from flask_cors import CORS
from functools import wraps
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DATA_FILE = 'patients.json'

# ----------- Utilities -----------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_data(data):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError:
        print("Error saving data.")

# ----------- Decorators -----------
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# ----------- OOP Classes -----------
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, patient_id, name, age, gender):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.records = []  # List of VisitRecord

    def add_record(self, visit_record):
        self.records.append(visit_record)

    def to_dict(self):
        return {
            "patient_id": self.patient_id,  # Include patient_id
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "records": [r.to_dict() for r in self.records]
        }

class VisitRecord:
    def __init__(self, symptoms, bp=None, temp=None, date=None, **extra_info):
        self.date = date or str(datetime.now())
        self.symptoms = symptoms
        self.bp = bp
        self.temp = temp
        self.extra_info = extra_info

    def to_dict(self):
        return {
            "date": self.date,
            "symptoms": self.symptoms,
            "bp": self.bp,
            "temp": self.temp,
            **self.extra_info
        }

# ----------- Routes -----------

@app.route('/patients', methods=['POST'])
@log_action
def add_patient():
    data = request.json
    required_fields = ['patient_id', 'name', 'age', 'gender']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    patients = load_data()
    if data['patient_id'] in patients:
        return jsonify({"error": "Patient already exists"}), 400

    # Validate age is a number
    try:
        age = int(data['age'])
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a number"}), 400

    patient = Patient(data['patient_id'], data['name'], age, data['gender'])
    patients[data['patient_id']] = patient.to_dict()
    save_data(patients)
    return jsonify({"message": "Patient added successfully"})

@app.route('/patients/<patient_id>/records', methods=['POST'])
@log_action
def add_record(patient_id):
    data = request.json
    if not data or 'symptoms' not in data:
        return jsonify({"error": "Missing symptoms in request"}), 400

    patients = load_data()
    if patient_id not in patients:
        return jsonify({"error": "Patient not found"}), 404

    record = VisitRecord(
        data['symptoms'],
        bp=data.get('bp'),
        temp=data.get('temp'),
        **data.get('extra_info', {})
    )

    # Append the new record
    patients[patient_id]['records'].append(record.to_dict())
    save_data(patients)
    return jsonify({"message": "Record added successfully"})

@app.route('/patients/<patient_id>', methods=['GET'])
@log_action
def get_patient(patient_id):
    patients = load_data()
    patient = patients.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patient)

@app.route('/patients', methods=['GET'])
@log_action
def list_patients():
    patients = load_data()
    return jsonify(patients)

# ----------- Run -----------
if __name__ == '__main__':
    print("WARNING: This backend uses file-based storage and is not safe for concurrent production use.")
    app.run(debug=True)
