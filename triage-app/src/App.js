import { useState } from 'react';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    symptoms: '',
    type: 'issue type'
  });

  function handleChange(event) {
    const { name, value } = event.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    console.log(formData);
    // Later gotta add logic to add the patient to the triage list
  }

  return (
    <div className="App">
      <h1>Hospital Triage Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Patient Name:</label><br/>
          <input 
            type="text" 
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Age:</label><br/>
          <input 
            type="number" 
            name="age"
            value={formData.age}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Symptoms:</label><br/>
          <textarea 
            name="symptoms"
            value={formData.symptoms}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Type:</label><br/>
          <select 
            name="issue type"
            value={formData.type}
            onChange={handleChange}
          >
            <option value="Critical">Injury</option>
            <option value="Urgent">Illness</option>
            <option value="Less Urgent">Allergy</option>
            <option value="Non-Urgent">Something else</option>
          </select>
        </div>

        <button type="submit">Add to List</button>
      </form>
    </div>
  );
}

export default App;
