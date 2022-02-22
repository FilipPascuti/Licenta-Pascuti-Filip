import React from 'react';
import {Routes, Route, Link} from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import {AuthProvider} from "./services/AuthProvider";
import RequireAuth from "./services/RequireAuth";
import Register from "./pages/Register";

function App() {
    return (
        <AuthProvider>
            <Routes>
                <Route path="/login" element={<Login/>} />
                <Route path="/register" element={<Register/>} />
                <Route path="/home" element={
                    <RequireAuth>
                        <Home/>
                    </RequireAuth>
                }/>
                <Route path="/" element={<Login/>} />
            </Routes>
        </AuthProvider>
    );
}

export default App;
