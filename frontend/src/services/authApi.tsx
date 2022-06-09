import {baseUrl, config, formDataConfig, withLogs} from "../core";
import axios from "axios";

const authUrl = `http://${baseUrl}/api/auth/login`
const registerUrl = `http://${baseUrl}/api/auth/register`

export interface AuthProps {
    access_token: string;
}

export const login: (username?: string, password?: string) => Promise<AuthProps> =
    (username, password) => {
        let bodyFormData = new FormData();
        bodyFormData.append('username', username || "");
        bodyFormData.append('password', password || "");
        return withLogs(axios.post(authUrl, bodyFormData, formDataConfig), 'login');
    }

export const register: (username?: string, password?: string, fullname?: string) => Promise<any> =
    (username, password, fullname) => {

        return withLogs(axios.post(registerUrl, {username, password, fullname}, config), 'register');
    }
