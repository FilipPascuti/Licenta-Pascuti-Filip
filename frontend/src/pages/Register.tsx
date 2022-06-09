import React, {useState} from 'react';
import {useAuth} from "../services/AuthProvider";
import {register} from "../services/authApi";
import {Navigate} from "react-router-dom";
import {Box, Button, FormField, grommet, Grommet, Select, Text, TextInput} from "grommet";

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

    const checkPasswordMatch = (password: string, confirmPassword: string) => {
        if (password !== confirmPassword)
            setNotMatching(true);
        else
            setNotMatching(false);
    }

    return (


        <>

            <Grommet full theme={grommet}>
                <Box fill justify="center" align="center" gap="medium">

                    <Box align="center" width="large" height="large" pad="medium" margin={{top:"xlarge"}}>
                        <Text size="xlarge" weight="bold" margin="medium">
                            Register
                        </Text>

                        <FormField>
                            <TextInput
                                placeholder="username"
                                value={username}
                                onChange={event => setUsername(event.target.value)}
                            />
                        </FormField>

                        <FormField>
                            <TextInput
                                placeholder="full name"
                                value={fullName}
                                onChange={event => setFullName(event.target.value)}
                            />
                        </FormField>



                        <FormField error={notMatching ? "passwords not matching" : ""}>
                            <TextInput
                                placeholder="password"
                                value={password}
                                type="password"
                                onChange={event => {
                                    setPassword(event.target.value)
                                    checkPasswordMatch(event.target.value, confirmPassword || "")
                                }}
                            />
                        </FormField>

                        <FormField error={notMatching ? "passwords not matching" : ""}>
                            <TextInput
                                placeholder="confirm password"
                                value={confirmPassword}
                                type="password"
                                onChange={event => {
                                    setConfirmPassword(event.target.value)
                                    checkPasswordMatch(password || "", event.target.value)
                                }}
                            />
                        </FormField>

                        <Select
                            options={['guitar', 'drums', 'piano', 'keys', 'bass']}
                            defaultValue={"drums"}
                            size="small"
                            onChange={({option}) => console.log(option)}
                        />

                        <Button primary label="Sign up"
                                margin="medium"
                                size="large"
                            onClick={() => handleRegister()}
                        />


                    </Box>
                </Box>
            </Grommet>


            {/*<Grid*/}
            {/*    container*/}
            {/*    spacing={0}*/}
            {/*    direction="column"*/}
            {/*    alignItems="center"*/}
            {/*    justifyContent="center"*/}
            {/*    style={{minHeight: '80vh'}}*/}
            {/*>*/}

            {/*    <Grid item xs={3}>*/}
            {/*        <div>*/}

            {/*            <Grid*/}
            {/*                container*/}
            {/*                spacing={0.8}*/}
            {/*                direction="column"*/}
            {/*                alignItems="center"*/}
            {/*                justifyContent="center"*/}
            {/*            >*/}

            {/*                <Grid item xs={3}>*/}
            {/*                    <h2>Register</h2>*/}
            {/*                </Grid>*/}
            {/*                <Grid item xs={3}>*/}
            {/*                    <TextField label="username" variant="standard" placeholder="username" type="text"*/}
            {/*                               onChange={(e) => {*/}
            {/*                                   setUsername(e.target.value)*/}
            {/*                               }}/>*/}
            {/*                </Grid>*/}
            {/*                <Grid item xs={3}>*/}
            {/*                    <TextField label="password" variant="standard" placeholder="password" type="password"*/}
            {/*                               error={notMatching} helperText={notMatching ? "passwords not matching" : ""}*/}
            {/*                               onChange={(e) => {*/}
            {/*                                   setPassword(e.target.value);*/}
            {/*                                   checkPasswordMatch(e.target.value, confirmPassword || "");*/}
            {/*                               }}/>*/}
            {/*                </Grid>*/}
            {/*                <Grid item xs={3}>*/}
            {/*                    <TextField label="confirm password" variant="standard" placeholder="confirm password"*/}
            {/*                               error={notMatching} helperText={notMatching ? "passwords not matching" : ""}*/}
            {/*                               type="password" onChange={(e) => {*/}
            {/*                        setConfirmPassword(e.target.value);*/}
            {/*                        checkPasswordMatch(password || "", e.target.value);*/}
            {/*                    }}/>*/}
            {/*                </Grid>*/}
            {/*                <Grid item xs={3}>*/}
            {/*                    <TextField label="full name" variant="standard" placeholder="full name" type="text"*/}
            {/*                               onChange={(e) => {*/}
            {/*                                   setFullName(e.target.value)*/}
            {/*                               }}/>*/}
            {/*                </Grid>*/}

            {/*                <Grid item xs={3}>*/}
            {/*                    <Button variant="contained" onClick={() => handleRegister()}>*/}
            {/*                        Register*/}
            {/*                    </Button>*/}
            {/*                </Grid>*/}

            {/*            </Grid>*/}

            {/*        </div>*/}

            {/*    </Grid>*/}

            {/*</Grid>*/}

        </>

    );
};

export default Register;
