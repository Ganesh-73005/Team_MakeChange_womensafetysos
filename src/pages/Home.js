import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Welcome to SafeHer App</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Link to="/sos" className="bg-red-500 text-white p-4 rounded-lg text-center">
          SOS Alert
        </Link>
        <Link to="/safe-route" className="bg-green-500 text-white p-4 rounded-lg text-center">
          Find Safe Route
        </Link>
        <Link to="/chatbot" className="bg-blue-500 text-white p-4 rounded-lg text-center">
          Chat with SafeHer
        </Link>
      </div>
    </div>
  );
};

export default Home;