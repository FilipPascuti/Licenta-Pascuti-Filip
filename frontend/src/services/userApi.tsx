import {authConfig, baseUrl, withLogs} from "../core";
import axios from "axios";
import {User} from "./User";

const userDetails = `http://${baseUrl}/api/user/details`
const configureUser = `http://${baseUrl}/api/user/characterization`
const recommendations = `http://${baseUrl}/api/user/recommendation`



export const getCurrentUser: (token: string) => Promise<User> =
    token => {
        return withLogs(axios.get<User>(userDetails, authConfig(token)), "getCurrentUser")
    }

export const sendAudioFile: (token: string, data: FormData) =>  Promise<any> = (token, data) => {
    return withLogs(axios.post(configureUser, data, authConfig(token)), "sendAudioFile")
}

export const getRecommendations: (token: string) => Promise<User[]> = token => {
    return withLogs(axios.get(recommendations, authConfig(token)), "getRecommendations")
}