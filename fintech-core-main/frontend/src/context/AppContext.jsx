/**
 * Global application context for state management.
 * Provides shared state across components without prop drilling.
 */

import { createContext, useContext, useState, useEffect } from 'react';
import apiClient from '../api/client';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  // Global state
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  
  // Feature availability
  const [features, setFeatures] = useState({
    analyticsEnabled: true,
    smsEnabled: false,
    ragEnabled: false,
  });
  
  // Date range for filtering (used across multiple pages)
  const [dateRange, setDateRange] = useState({
    startDate: null,
    endDate: null,
  });
  
  // Settings
  const [settings, setSettings] = useState(null);
  
  // Check backend health and feature availability on mount
  useEffect(() => {
    checkBackendHealth();
  }, []);
  
  const checkBackendHealth = async () => {
    try {
      const response = await apiClient.get('/health');
      if (response.data && response.data.features) {
        setFeatures({
          analyticsEnabled: response.data.features.analytics_enabled || true,
          smsEnabled: response.data.features.sms_enabled || false,
          ragEnabled: response.data.features.rag_enabled || false,
        });
      }
    } catch (err) {
      console.error('Failed to check backend health:', err);
      // Don't show error to user on initial load
    }
  };
  
  // Show success message
  const showSuccess = (message, duration = 3000) => {
    setSuccess(message);
    setTimeout(() => setSuccess(null), duration);
  };
  
  // Show error message
  const showError = (message, duration = 5000) => {
    setError(message);
    setTimeout(() => setError(null), duration);
  };
  
  // Clear all messages
  const clearMessages = () => {
    setError(null);
    setSuccess(null);
  };
  
  const value = {
    // State
    isLoading,
    setIsLoading,
    error,
    success,
    features,
    dateRange,
    setDateRange,
    settings,
    setSettings,
    
    // Methods
    showSuccess,
    showError,
    clearMessages,
    checkBackendHealth,
  };
  
  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook to use app context
export const useApp = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within AppProvider');
  }
  return context;
};

export default AppContext;
