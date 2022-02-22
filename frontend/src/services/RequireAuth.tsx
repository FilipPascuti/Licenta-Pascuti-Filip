import React from 'react';
import {useAuth} from "./AuthProvider";
import {Navigate} from "react-router-dom";

const RequireAuth: React.FC = ({children}) => {
    const {isAuthenticated} = useAuth();

    if (!isAuthenticated) {
        return <Navigate to={"/login"}/>
    }

    return (
        <div>
            {children}
        </div>
    );
};

export default RequireAuth;
