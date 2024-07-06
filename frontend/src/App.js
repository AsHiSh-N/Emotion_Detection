import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [emotion, setEmotion] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/api/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setEmotion(response.data.emotion);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {emotion && <h2>Emotion: {emotion}</h2>}
    </div>
  );
}

export default App;
