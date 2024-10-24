// src/components/Home.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const navigate = useNavigate();

    return (
        <div>
            <h1 style={{ color: '#11557C' }}>Willkommen</h1>
            <div className="nav-button">
                <button onClick={() => navigate('/login')}>Login</button>
                <button onClick={() => navigate('/register')}>Register</button>
                <button onClick={() => navigate('/startpage')}>Startpage</button>
            </div>
        </div>
    );
};

export default Home;
