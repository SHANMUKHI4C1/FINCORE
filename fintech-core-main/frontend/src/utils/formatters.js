/**
 * Utility functions for formatting data (currency, dates, numbers).
 */

/**
 * Format number as Indian Rupee currency.
 * @param {number} amount - Amount to format
 * @returns {string} Formatted currency string
 */
export const formatCurrency = (amount) => {
  if (amount === null || amount === undefined || isNaN(amount)) {
    return '₹0.00';
  }
  
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(amount);
};

/**
 * Format date to readable string.
 * @param {string|Date} date - Date to format
 * @param {string} format - Format type ('short', 'long', 'iso')
 * @returns {string} Formatted date string
 */
export const formatDate = (date, format = 'short') => {
  if (!date) return '';
  
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  
  if (isNaN(dateObj.getTime())) {
    return '';
  }
  
  switch (format) {
    case 'short':
      // DD/MM/YYYY
      return dateObj.toLocaleDateString('en-IN');
    
    case 'long':
      // 9 October 2026
      return dateObj.toLocaleDateString('en-IN', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
      });
    
    case 'iso':
      // YYYY-MM-DD
      return dateObj.toISOString().split('T')[0];
    
    case 'datetime':
      // DD/MM/YYYY HH:MM
      return dateObj.toLocaleString('en-IN', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    
    default:
      return dateObj.toLocaleDateString('en-IN');
  }
};

/**
 * Format number with commas.
 * @param {number} num - Number to format
 * @param {number} decimals - Number of decimal places
 * @returns {string} Formatted number string
 */
export const formatNumber = (num, decimals = 0) => {
  if (num === null || num === undefined || isNaN(num)) {
    return '0';
  }
  
  return new Intl.NumberFormat('en-IN', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  }).format(num);
};

/**
 * Format percentage.
 * @param {number} value - Value to format as percentage
 * @param {number} decimals - Number of decimal places
 * @returns {string} Formatted percentage string
 */
export const formatPercentage = (value, decimals = 1) => {
  if (value === null || value === undefined || isNaN(value)) {
    return '0%';
  }
  
  return `${formatNumber(value, decimals)}%`;
};

/**
 * Truncate text to specified length.
 * @param {string} text - Text to truncate
 * @param {number} maxLength - Maximum length
 * @returns {string} Truncated text with ellipsis
 */
export const truncateText = (text, maxLength = 50) => {
  if (!text) return '';
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};

/**
 * Get relative time string (e.g., "2 hours ago").
 * @param {string|Date} date - Date to compare
 * @returns {string} Relative time string
 */
export const getRelativeTime = (date) => {
  if (!date) return '';
  
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  const now = new Date();
  const diffMs = now - dateObj;
  const diffSec = Math.floor(diffMs / 1000);
  const diffMin = Math.floor(diffSec / 60);
  const diffHour = Math.floor(diffMin / 60);
  const diffDay = Math.floor(diffHour / 24);
  
  if (diffSec < 60) return 'just now';
  if (diffMin < 60) return `${diffMin} minute${diffMin > 1 ? 's' : ''} ago`;
  if (diffHour < 24) return `${diffHour} hour${diffHour > 1 ? 's' : ''} ago`;
  if (diffDay < 7) return `${diffDay} day${diffDay > 1 ? 's' : ''} ago`;
  
  return formatDate(dateObj, 'short');
};

/**
 * Format month-year for display.
 * @param {string} monthYear - Month in YYYY-MM format
 * @returns {string} Formatted month-year (e.g., "October 2026")
 */
export const formatMonthYear = (monthYear) => {
  if (!monthYear) return '';
  
  const [year, month] = monthYear.split('-');
  const date = new Date(year, month - 1);
  
  return date.toLocaleDateString('en-IN', {
    month: 'long',
    year: 'numeric',
  });
};

export default {
  formatCurrency,
  formatDate,
  formatNumber,
  formatPercentage,
  truncateText,
  getRelativeTime,
  formatMonthYear,
};
