import axios from "axios";

const api = axios.create({
  baseURL: "https://travel-agent-5yk7.onrender.com",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;