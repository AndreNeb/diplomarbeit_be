// src/components/PrivateRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ children }) => {
    const token = localStorage.getItem('token'); // Check if token exists
    if (!token) {
        alert('You need to log in to access this page.'); // Alert if not logged in
        return <Navigate to="/" />; // Redirect to home if not authenticated
    }

    return children; // Render the children if authenticated
};

export default PrivateRoute;
