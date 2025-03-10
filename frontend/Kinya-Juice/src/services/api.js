import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000"; // Ensure this matches your Flask backend

export const signup = async (userData) => {
  try {
    const response = await axios.post(`${BASE_URL}/auth/signup`, userData, {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true, // Ensures cookies are included
    });
    return response.data; // Return only the response data
  } catch (error) {
    console.error("Signup Error:", error.response ? error.response.data : error);
    throw error;
  }
};



export const login = async (email, password) => {
  try {
    const response = await axios.post(
      `${BASE_URL}/auth/login`, // Adjust this based on your Flask API
      { email, password },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true, // Ensures cookies/auth are sent
      }
    );
    return response.data; // Return only data for cleaner handling
  } catch (error) {
    console.error("Login Error:", error.response ? error.response.data : error);
    throw error;
  }
};
