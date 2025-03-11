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
    const response = await axios.post(`${BASE_URL}/auth/login`, { email, password }, {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true, // Only useful if using cookies
    });

    // Store token in localStorage
    const token = response.data.access_token; // Adjust based on Flask response
    localStorage.setItem("token", token);

    return response.data;
  } catch (error) {
    console.error("Login Error:", error.response ? error.response.data : error);
    throw error;
  }
};


export const getOrders = async () => {
  try {
      const response = await axios.get(`${BASE_URL}/products/products`, {
        withCredentials: true,
      });
      return response.data;
    } catch (error) {
      console.error("Get Orders Error:", error.response ? error.response.data : error);
      throw error;
    }
  };
