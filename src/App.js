import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/data/')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to My Simple React App</h1>
        <p>This is a simple React component demonstrating a frontend page.</p>
        {data && (
          <div>
            <h2>Data from API:</h2>
            <p>Name: {data.name}</p>
            <p>Age: {data.age}</p>
            <p>Location: {data.location}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
