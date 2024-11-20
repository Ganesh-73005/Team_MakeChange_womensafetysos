import React, { useContext } from 'react';
import { Navigate, Route } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';

const PrivateRoute = ({ element: Component, ...rest }) => {
  const { currentUser } = useContext(AuthContext) || {}; // Use useContext with AuthContext

  if (!currentUser) {
    // Redirect to login if user is not authenticated
    return <Navigate to="/Login" />;
  }

  return <Route {...rest} element={<Component />} />;
};

export default PrivateRoute;
