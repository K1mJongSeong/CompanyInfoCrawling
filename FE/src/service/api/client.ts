import axios from "axios";

const client = axios.create();

// local
client.defaults.baseURL = "http://192.168.0.158:8080";
// server
client.defaults.withCredentials = true;

export default client;
