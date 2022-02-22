import React, {useState} from 'react';
import {useAuth} from "../services/AuthProvider";
import {register} from "../services/authApi";
import {Navigate} from "react-router-dom";
import {Button, Grid, TextField, Typography} from "@mui/material";

const Register: React.FC = () => {

    const {isRegistered, register} = useAuth();

    const [username, setUsername] = useState<string>();
    const [password, setPassword] = useState<string>();
    const [confirmPassword, setConfirmPassword] = useState<string>();
    const [fullName, setFullName] = useState<string>();
    const [notMatching, setNotMatching] = useState<boolean>(false);

    const handleRegister = async () => {
        if (password !== confirmPassword) {
            setNotMatching(true);
            return;
        }
        register && register(username, password, fullName);
    }

    if (isRegistered) {
        return <Navigate to="/login"/>
    }

    const checkPasswordMatch = (password:string, confirmPassword:string) => {
        if(password !== confirmPassword)
            setNotMatching(true);
        else
            setNotMatching(false);
    }

    return (

        <Grid
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justifyContent="center"
            style={{minHeight: '80vh'}}
        >

            <Grid item xs={3}>
                <div>

                    <Grid
                        container
                        spacing={0.8}
                        direction="column"
                        alignItems="center"
                        justifyContent="center"
                    >

                        <Grid item xs={3}>
                            <h2>Register</h2>
                        </Grid>
                        <Grid item xs={3}>
                            <TextField label="username" variant="standard" placeholder="username" type="text"
                                       onChange={(e) => {
                                           setUsername(e.target.value)
                                       }}/>
                        </Grid>
                        <Grid item xs={3}>
                            <TextField label="password" variant="standard" placeholder="password" type="password"
                                       error={notMatching} helperText={notMatching ? "passwords not matching" : ""}
                                       onChange={(e) => {
                                           setPassword(e.target.value);
                                           checkPasswordMatch(e.target.value, confirmPassword || "");
                                       }}/>
                        </Grid>
                        <Grid item xs={3}>
                            <TextField label="confirm password" variant="standard" placeholder="confirm password"
                                       error={notMatching} helperText={notMatching ? "passwords not matching" : ""}
                                       type="password" onChange={(e) => {
                                setConfirmPassword(e.target.value);
                                checkPasswordMatch(password || "", e.target.value);
                            }}/>
                        </Grid>
                        <Grid item xs={3}>
                            <TextField label="full name" variant="standard" placeholder="full name" type="text"
                                       onChange={(e) => {
                                           setFullName(e.target.value)
                                       }}/>
                        </Grid>

                        <Grid item xs={3}>
                            <Button variant="contained" onClick={() => handleRegister()}>
                                Register
                            </Button>
                        </Grid>

                    </Grid>

                </div>

            </Grid>

        </Grid>
    );
};

export default Register;
