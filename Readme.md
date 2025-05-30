# 🩺 Health Tracker Application

A full-stack web application for managing patient records, built with **Python (Flask)** for the backend and **React (Vite)** for the frontend. This project was created as a hands-on exercise to **learn and apply Object-Oriented Programming (OOP)** concepts in Python while also exploring modern web development practices.

---

## 🚀 Project Overview

This application allows users to manage patient details and medical records using a RESTful API and a responsive web interface. It demonstrates key principles of software design, including modularity, reusability, and separation of concerns.

---

## 🎯 Key Objectives

- Learn and apply **OOP principles** in Python
- Understand and use **Flask** to build RESTful APIs
- Build a responsive frontend using **React** and **Vite**
- Practice full-stack integration with **Axios** and **CORS**
- Handle data persistence using **file I/O with JSON**

---

## 🧠 Python Concepts Demonstrated

### 1. Core Language Features

- **Variables & Data Types**:
  ```python
  DATA_FILE = 'patients.json'  # str
  patients = {}                # dict
  age = 30                     # int
  ```

* **Control Flow**:

  ```python
  if patient_id not in patients:
      return jsonify({"error": "Patient not found"}), 404
  ```

---

### 2. Functions & Advanced Usage

- **Function Definition & Return**:

  ```python
  def load_data():
      try:
          with open(DATA_FILE, 'r') as f:
              return json.load(f)
      except (json.JSONDecodeError, IOError):
          return {}
  ```

- **Decorators for Logging**:

  ```python
  @app.route('/patients', methods=['POST'])
  @log_action
  def add_patient():
      ...
  ```

---

### 3. Object-Oriented Programming (OOP)

- **Class Definition & Inheritance**:

  ```python
  class Person:
      def __init__(self, name, age, gender):
          self.name = name
          self.age = age
          self.gender = gender

  class Patient(Person):
      def __init__(self, patient_id, name, age, gender):
          super().__init__(name, age, gender)
          self.patient_id = patient_id
          self.records = []
  ```

- **Polymorphism (e.g., method overriding)**:

  ```python
  def to_dict(self):  # Implemented differently in each class
      ...
  ```

---

### 4. Error Handling & File I/O

- **Try/Except for Robustness**:

  ```python
  try:
      age = int(data['age'])
  except (ValueError, TypeError):
      return jsonify({"error": "Age must be a number"}), 400
  ```

- **File Operations**:

  ```python
  with open(DATA_FILE, 'w') as f:
      json.dump(data, f, indent=4)
  ```

---

### 5. Advanced Python Concepts

- **`*args` and `**kwargs` for Flexibility\*\*:

  ```python
  class VisitRecord:
      def __init__(self, symptoms, bp=None, temp=None, **extra_info):
          self.extra_info = extra_info
  ```

---

## 🧩 Frontend (React/Vite)

### 🔧 Key Features

- Tabbed navigation and responsive UI
- Patient listing and form submission
- Axios integration with Flask API
- React hooks for state and side effects

### 💡 React Code Samples

- **Hooks**:

  ```jsx
  const [patients, setPatients] = useState([]);
  useEffect(() => {
    fetchPatients();
  }, []);
  ```

- **Component-based Architecture** for modular UI design

---

## ⚙️ Project Setup

### Backend (Flask)

```bash
pip install flask flask-cors
export FLASK_APP=app.py
flask run --port=5000
```

### Frontend (React/Vite)

```bash
cd frontend
npm install
npm run dev
```

---

## ✅ Features Summary

### Backend

- CRUD for patients and medical records
- JSON file-based data persistence
- Request logging with decorators
- CORS-enabled for API access

### Frontend

- React-based UI with tabbed interface
- Patient addition and listing
- Axios communication with Flask backend

---

## 🧪 Challenges Solved

| Challenge          | Solution                                |
| ------------------ | --------------------------------------- |
| CORS Configuration | Used `Flask-CORS` middleware            |
| State Management   | Managed with `useState` and `useEffect` |
| Data Persistence   | JSON file operations with atomic writes |
| Error Handling     | Consistent error responses from API     |

---

## 🎓 Learning Outcomes

### 📌 Python & OOP

- Designed reusable classes using inheritance
- Applied polymorphism and decorators effectively
- Handled file operations and data serialization

### 🌐 Full-Stack Development

- Built and connected a React frontend to Flask backend
- Used Axios for HTTP communication
- Created responsive layouts using modern CSS

### 🛠️ DevOps & Tooling

- Used `Vite` for optimized frontend builds
- Managed dependencies via `pip` and `npm`
- Practiced project structure and environment setup

---

## 📁 Directory Structure (Simplified)

```
health-tracker-app/
├── app.py               # Flask app and routes
├── models.py            # OOP classes like Patient, VisitRecord
├── utils.py             # Logging and helper functions
├── patients.json        # Data file
├── frontend/            # React project
│   ├── src/
│   ├── public/
│   └── vite.config.js
```

---

## 📌 Final Notes

This project was a learning-focused exercise to deepen my understanding of:

- Object-oriented principles in Python
- REST API development with Flask
- Full-stack integration with React and Vite

It serves as a strong foundation for more advanced backend and full-stack applications.
