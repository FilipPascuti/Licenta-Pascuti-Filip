import React, {useState} from 'react';
import {useAuth} from "../services/AuthProvider";
import {Navigate, useNavigate} from "react-router-dom";
import {Box, grommet, Grommet, Form, FormField, TextInput, Button, Text} from "grommet";


const Login: React.FC = () => {

    const {isAuthenticated, authenticationError, login} = useAuth();
    const navigate = useNavigate()
    const [newUsername, setNewUsername] = useState<string>();
    const [newPassword, setNewPassword] = useState<string>();

    const handleLogin = () => {
        login && login(newUsername, newPassword);
    }

    const routeToRegister = () => {
        console.log("register")
        return navigate("/register");
    }

    if (isAuthenticated) {
        return <Navigate to="/home"/>
    }

    return (

        <Grommet full theme={grommet}>
            <Box fill justify="center" align="center" gap="medium">

                <Box align="center" width="large" height="medium" pad="medium">
                    <Text size="xlarge" weight="bold" margin="medium">
                        Login
                    </Text>

                    <FormField>
                        <TextInput
                            placeholder="username"
                            value={newUsername}
                            onChange={event => setNewUsername(event.target.value)}
                        />
                    </FormField>


                    <FormField>
                        <TextInput
                            placeholder="password"
                            value={newPassword}
                            type="password"
                            onChange={event => setNewPassword(event.target.value)}
                        />
                    </FormField>

                    <Box direction="row" margin={{top: "medium"}}>
                        <Button primary label="Login"
                                margin={{horizontal: 'xsmall'}}
                                onClick={() => handleLogin()}
                        />
                        <Button primary label="Sign up"
                                margin={{horizontal: 'xsmall'}}
                                onClick={() => routeToRegister()}
                        />
                    </Box>

                    {
                        authenticationError &&
                        <Text size="large" weight="bold" margin="medium" color="red">
                            Your credentials are incorrect!
                        </Text>

                    }

                </Box>
            </Box>
        </Grommet>


        // <Grid
        //     container
        //     spacing={0}
        //     direction="column"
        //     alignItems="center"
        //     justifyContent="center"
        //     style={{minHeight: '80vh'}}
        // >
        //
        //     <Grid item>
        //         <div>
        //
        //             <Grid
        //                 container
        //                 spacing={0.8}
        //                 direction="column"
        //                 alignItems="center"
        //                 justifyContent="center"
        //             >
        //                 <Grid item xs={3}>
        //                     <h2>Login</h2>
        //                 </Grid>
        //                 <Grid item xs={3}>
        //                     <TextField label="username" variant="standard" placeholder="username" type="text"
        //                                onChange={(e) => {
        //                                    setNewUsername(e.target.value)
        //                                }}/>
        //                 </Grid>
        //                 <Grid item xs={3}>
        //                     <TextField label="password" variant="standard" placeholder="password" type="password"
        //                                onChange={(e) => {
        //                                    setNewPassword(e.target.value)
        //                                }}/>
        //                 </Grid>
        //                 <Grid item xs={3}>
        //
        //                     <Grid
        //                         container
        //                         direction="row"
        //                         spacing={1}
        //                         justifyContent="space-evenly"
        //                     >
        //
        //                         <Grid item>
        //                             <Button variant="contained" onClick={() => handleLogin()}>
        //                                 Login
        //                             </Button>
        //
        //                         </Grid>
        //                         <Grid item>
        //                             <Button variant="contained" color="secondary" onClick={() => routeToRegister()}>
        //                                 Register
        //                             </Button>
        //                         </Grid>
        //
        //                     </Grid>
        //                 </Grid>
        //
        //                 {
        //                     authenticationError &&
        //                     <Grid item xs={3}>
        //                         <p style={{
        //                             color: "red"
        //                         }}>username of password are wrong</p>
        //                     </Grid>
        //                 }
        //
        //
        //             </Grid>
        //
        //         </div>
        //
        //     </Grid>
        //
        // </Grid>

    );
};

export default Login;
