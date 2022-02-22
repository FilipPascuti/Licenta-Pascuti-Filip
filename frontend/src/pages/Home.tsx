import React from 'react';
import {useAuth} from "../services/AuthProvider";
import {useNavigate} from "react-router-dom";

const Home: React.FC = () => {
    const {username, password, logout} = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout && logout();
        navigate("/");
    }

    return (
        <div>
            <h1>Home page</h1>
            <h1>Welcome {username}!</h1>

            <button onClick={() => handleLogout()}>
                Logout
            </button>
        </div>
    );
};

export default Home;
