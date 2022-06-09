import React, {useEffect, useState} from 'react';
import {useAuth} from "../services/AuthProvider";
import {useNavigate} from "react-router-dom";
import {getCurrentUser, getRecommendations, sendAudioFile} from "../services/userApi";
import {User} from "../services/User";
import {
    Anchor,
    Box,
    Button,
    Card, CardBody, CardHeader,
    FormField,
    grommet,
    Grommet,
    NameValueList,
    Nav,
    Select,
    Text,
    TextInput,
    NameValuePair, FileInput
} from "grommet";
import {Logout} from "grommet-icons"

const Home: React.FC = () => {
    const {username, logout, token} = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout && logout();
        navigate("/");
    }

    const [user, setUser] = useState<User>()
    const [hasVectorization, setHasVectorization] = useState(false)


    const getUserDetails = async () => {
        let fetchedUser = await getCurrentUser(token)
        console.log(fetchedUser)
        setUser(fetchedUser)
    }

    useEffect(() => {

        getUserDetails()
    }, [])

    useEffect(() => {
        if (user != null && user.vectorization !== "" && user.vectorization !== null) {
            setHasVectorization(true)
        } else {
            setHasVectorization(false)
        }
    }, [user])

    const [file, setFile] = useState<any>();

    const uploadHandler = (event: any) => {
        console.log(event.target)
        if(!event.target.files){
            setFile(undefined)
            return;
        }
        const file = event.target.files[0];
        if (!file) return;
        file.isUploading = true;
        console.log(file)
        setFile(file)
    }

    const handleUpload = async () => {
        let data = new FormData()
        data.append(
            "upload_file",
            file,
            file.name
        )
        await sendAudioFile(token, data)
        getUserDetails()
    }

    const [recommendations, setRecommendatinos] = useState<User[]>()

    const handleRecommendations = async () => {
        console.log(token)
        let fetched_recommendations = await getRecommendations(token)
        console.log(fetched_recommendations)
        setRecommendatinos(fetched_recommendations)

    }

    return (

        <Grommet full theme={grommet}>

            <Nav direction="row" background="brand" pad="medium">
                <Anchor label="Logout" icon={<Logout/>} alignSelf="end" onClick={() => handleLogout()}/>
            </Nav>

            <Box fill justify="center" align="center" gap="medium">

                <Box align="center" width="large" height="medium" pad="medium">
                    <Text size="xlarge" weight="bold" margin="medium">
                        Welcome to the home page
                    </Text>
                    {
                        hasVectorization ?
                            <>
                                <Text size="large" weight="bold" margin="medium">
                                    Search for a type of musician:
                                </Text>
                                <Select
                                    options={['guitar', 'drums', 'piano', 'keys', 'bass']}
                                    defaultValue={"drums"}
                                    onChange={({option}) => console.log(option)}
                                />

                                <Button primary label="Search"
                                        margin="medium"
                                        onClick={() => handleRecommendations()}
                                />

                                {
                                    !!recommendations && (
                                        <>
                                            <Text margin={"medium"}>The top 5 recommendations are:</Text>
                                            <NameValueList align={"center"} width={"medium"}  pad="medium">
                                                {
                                                    recommendations.map(({username, fullname}) =>
                                                        <NameValuePair name={fullname}>
                                                            <Text>{username}</Text>
                                                        </NameValuePair>
                                                    )}
                                            </NameValueList>
                                        </>

                                    )}

                            </> :
                            <>
                                <Text margin="medium">
                                    Before searching for musician you have to upload an audio file with you playing your favourite song.
                                </Text>

                                <FileInput
                                    name="file"
                                    onChange={uploadHandler}
                                />

                                <Button primary label="Upload File"
                                        margin="medium"
                                        size="large"
                                        disabled={!file}
                                        onClick={() => handleUpload()}
                                />


                            </>
                    }


                </Box>
            </Box>
        </Grommet>


    );
};

export default Home;
