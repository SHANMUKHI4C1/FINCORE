/**
 * Axios client configuration for API calls.
 * Provides base configuration and interceptors for error handling.
 */

import axios from 'axios';

// Base URL for API - using Vite proxy in development
const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: BASE_URL,
  timeout: 30000, // 30 second timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth tokens (future use)
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token here when implementing authentication
    // const token = localStorage.getItem('token');
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`;
    // }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Handle specific error cases
    if (error.response) {
      // Server responded with error status
      const { status, data } = error.response;
      
      switch (status) {
        case 400:
          console.error('Bad Request:', data.message || 'Invalid request');
          break;
        case 404:
          console.error('Not Found:', data.message || 'Resource not found');
          break;
        case 500:
          console.error('Server Error:', data.message || 'Internal server error');
          break;
        default:
          console.error('API Error:', data.message || 'Unknown error occurred');
      }
      
      return Promise.reject(data || error);
    } else if (error.request) {
      // Request made but no response received
      console.error('Network Error: No response from server');
      return Promise.reject({
        error: 'Network Error',
        message: 'Could not connect to server. Please check if the backend is running.',
      });
    } else {
      // Something else happened
      console.error('Error:', error.message);
      return Promise.reject({
        error: 'Error',
        message: error.message,
      });
    }
  }
);

export default apiClient;
