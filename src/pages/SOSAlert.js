import React, { useState, useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';
import axios from 'axios';

const SOSAlert = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { currentUser } = useContext(AuthContext);

  const sendSOS = async () => {
    setLoading(true);
    setError('');
    try {
      const position = await new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(resolve, reject);
      });

      const { latitude, longitude } = position.coords;

      const response = await axios.post('http://localhost:5000/api/sos/alert', {
        latitude,
        longitude
      }, {
        headers: {
          'Authorization': await currentUser.getIdToken()
        }
      });

      alert('SOS alert sent successfully!');
    } catch (error) {
      setError('Failed to send SOS alert. Please try again.');
      console.error('Error sending SOS:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">SOS Alert</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button
        onClick={sendSOS}
        disabled={loading}
        className={`bg-red-500 text-white p-4 rounded-lg ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
      >
        {loading ? 'Sending...' : 'Send SOS Alert'}
      </button>
    </div>
  );
};

export default SOSAlert;