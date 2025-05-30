import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
import './App.css';

// Patient list component
const PatientList = ({ patients }) => (
  <div>
    {patients.length > 0 ? (
      patients.map(patient => (
        <div className="card" key={patient.patient_id}>
          <h3>{patient.name}</h3>
          <p>Age: {patient.age}</p>
          <p>Gender: {patient.gender}</p>
          {patient.records?.length > 0 && (
            <div className="records">
              <h4>Medical Records:</h4>
              {patient.records.map((record, index) => (
                <div key={index} className="record">
                  <p>Date: {new Date(record.date).toLocaleDateString()}</p>
                  <p>Symptoms: {record.symptoms}</p>
                  {record.bp && <p>Blood Pressure: {record.bp}</p>}
                  {record.temp && <p>Temperature: {record.temp}</p>}
                </div>
              ))}
            </div>
          )}
        </div>
      ))
    ) : (
      <p>No patients found.</p>
    )}
  </div>
);

// Add patient form
const AddPatientForm = ({ onAddPatient }) => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const patientId = uuidv4();
    try {
      // Send POST request to backend
      await axios.post('http://localhost:5000/patients', {
        patient_id: patientId,
        name,
        age: Number(age),
        gender,
      });
      
      // Update local state with complete patient data
      onAddPatient({
        patient_id: patientId,
        name,
        age: Number(age),
        gender,
        records: []  // Initialize empty records array
      });
      
      // Clear form fields
      setName('');
      setAge('');
      setGender('');
    } catch (err) {
      console.error('Error adding patient:', err);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="input-group">
        <label className="input-label">Name</label>
        <input
          className="input-field"
          value={name}
          onChange={e => setName(e.target.value)}
          required
        />
      </div>
      <div className="input-group">
        <label className="input-label">Age</label>
        <input
          className="input-field"
          type="number"
          value={age}
          onChange={e => setAge(e.target.value)}
          required
        />
      </div>
      <div className="input-group">
        <label className="input-label">Gender</label>
        <input
          className="input-field"
          value={gender}
          onChange={e => setGender(e.target.value)}
          required
        />
      </div>
      <button className="button" type="submit">Add Patient</button>
    </form>
  );
};

function App() {
  const [patients, setPatients] = useState([]);
  const [activeTab, setActiveTab] = useState('view');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPatients = async () => {
      try {
        const response = await axios.get('http://localhost:5000/patients');
        // Convert backend object to array
        const patientsArray = Object.values(response.data);
        setPatients(patientsArray);
      } catch (err) {
        console.error('Error fetching patients:', err);
      } finally {
        setLoading(false);
      }
    };
    
    fetchPatients();
  }, []);

  const handleAddPatient = (patient) => {
    setPatients(prev => [...prev, patient]);
  };

  return (
    <div className="container">
      <div className="tabs">
        <button
          className={`tab-btn ${activeTab === 'view' ? 'active' : ''}`}
          onClick={() => setActiveTab('view')}
        >
          View Patients
        </button>
        <button
          className={`tab-btn ${activeTab === 'add' ? 'active' : ''}`}
          onClick={() => setActiveTab('add')}
        >
          Add Patient
        </button>
      </div>
      
      {loading ? (
        <p>Loading patients...</p>
      ) : activeTab === 'view' ? (
        <PatientList patients={patients} />
      ) : (
        <AddPatientForm onAddPatient={handleAddPatient} />
      )}
    </div>
  );
}

export default App;
