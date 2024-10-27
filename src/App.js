import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import PrivateRoute from './components/PrivateRoute';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import SOSAlert from './pages/SOSAlert';
import Chatbot from './pages/Chatbot';
import { Navigate } from 'react-router-dom';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} /> {/* Redirect to login */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route 
          path="/home" 
           element={<Home />}  
        />
        <Route 
          path="/sos-alert" 
          element={<PrivateRoute element={<SOSAlert />} />} 
        />
        <Route 
          path="/chatbot" 
          element={<PrivateRoute element={<Chatbot />} />} 
        />
      </Routes>
    </Router>
  );
};

export default App;
