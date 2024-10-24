// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import Startpage from './components/Startpage';
import PrivateRoute from './components/PrivateRoute'; // Import PrivateRoute

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/startpage" element={<PrivateRoute>
                            <Startpage />
                </PrivateRoute>}/> {/* Use PrivateRoute correctly here */}
            </Routes>
        </Router>
    );
};

export default App;
