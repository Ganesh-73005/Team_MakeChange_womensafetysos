import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';
import { auth } from '../utils/firebase';

const Header = () => {
  const { currentUser } = useContext(AuthContext);

  return (
    <header className="bg-blue-500 p-4">
      <nav className="flex justify-between items-center">
        <Link to="/" className="text-white text-2xl font-bold">SafeHer</Link>
        <div>
          {currentUser ? (
            <>
              <Link to="/" className="text-white mr-4">Home</Link>
              <Link to="/sos" className="text-white mr-4">SOS</Link>
              <Link to="/safe-route" className="text-white mr-4">Safe Route</Link>
              <Link to="/chatbot" className="text-white mr-4">Chatbot</Link>
              <button onClick={() => auth.signOut()} className="text-white">Logout</button>
            </>
          ) : (
            <>
              <Link to="/login" className="text-white mr-4">Login</Link>
              <Link to="/register" className="text-white">Register</Link>
            </>
          )}
        </div>
      </nav>
    </header>
  );
};

export default Header;