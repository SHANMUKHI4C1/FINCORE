/**
 * Validation utility functions for form inputs.
 */

/**
 * Validate amount (positive number).
 * @param {string|number} amount - Amount to validate
 * @returns {object} { isValid: boolean, error: string }
 */
export const validateAmount = (amount) => {
  if (!amount && amount !== 0) {
    return { isValid: false, error: 'Amount is required' };
  }
  
  const numAmount = typeof amount === 'string' ? parseFloat(amount) : amount;
  
  if (isNaN(numAmount)) {
    return { isValid: false, error: 'Amount must be a valid number' };
  }
  
  if (numAmount <= 0) {
    return { isValid: false, error: 'Amount must be greater than zero' };
  }
  
  if (numAmount > 10000000) {
    return { isValid: false, error: 'Amount cannot exceed ₹1,00,00,000' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate date.
 * @param {string} date - Date string to validate
 * @returns {object} { isValid: boolean, error: string }
 */
export const validateDate = (date) => {
  if (!date) {
    return { isValid: false, error: 'Date is required' };
  }
  
  const dateObj = new Date(date);
  
  if (isNaN(dateObj.getTime())) {
    return { isValid: false, error: 'Invalid date format' };
  }
  
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  
  if (dateObj > today) {
    return { isValid: false, error: 'Date cannot be in the future' };
  }
  
  const minDate = new Date('2000-01-01');
  if (dateObj < minDate) {
    return { isValid: false, error: 'Date cannot be before year 2000' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate required text field.
 * @param {string} text - Text to validate
 * @param {string} fieldName - Name of field for error message
 * @param {number} minLength - Minimum length (default: 1)
 * @returns {object} { isValid: boolean, error: string }
 */
export const validateRequired = (text, fieldName = 'Field', minLength = 1) => {
  if (!text || text.trim().length === 0) {
    return { isValid: false, error: `${fieldName} is required` };
  }
  
  if (text.trim().length < minLength) {
    return { isValid: false, error: `${fieldName} must be at least ${minLength} characters` };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate category selection.
 * @param {string} category - Category to validate
 * @returns {object} { isValid: boolean, error: string }
 */
export const validateCategory = (category) => {
  if (!category || category.trim().length === 0) {
    return { isValid: false, error: 'Category is required' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate phone number (Indian format).
 * @param {string} phone - Phone number to validate
 * @returns {object} { isValid: boolean, error: string }
 */
export const validatePhone = (phone) => {
  if (!phone) {
    return { isValid: false, error: 'Phone number is required' };
  }
  
  // Remove spaces and hyphens
  const cleanPhone = phone.replace(/[\s-]/g, '');
  
  // Check for Indian phone number format
  const phoneRegex = /^(\+91)?[6-9]\d{9}$/;
  
  if (!phoneRegex.test(cleanPhone)) {
    return { isValid: false, error: 'Invalid phone number format (use +91XXXXXXXXXX or 10 digits)' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate date range.
 * @param {string} startDate - Start date
 * @param {string} endDate - End date
 * @returns {object} { isValid: boolean, error: string }
 */
export const validateDateRange = (startDate, endDate) => {
  if (!startDate || !endDate) {
    return { isValid: false, error: 'Both start and end dates are required' };
  }
  
  const start = new Date(startDate);
  const end = new Date(endDate);
  
  if (isNaN(start.getTime()) || isNaN(end.getTime())) {
    return { isValid: false, error: 'Invalid date format' };
  }
  
  if (start > end) {
    return { isValid: false, error: 'Start date must be before end date' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate percentage (0-100).
 * @param {string|number} percentage - Percentage to validate
 * @returns {object} { isValid: boolean, error: string }
 */
export const validatePercentage = (percentage) => {
  if (percentage === null || percentage === undefined || percentage === '') {
    return { isValid: false, error: 'Percentage is required' };
  }
  
  const numPercentage = typeof percentage === 'string' ? parseFloat(percentage) : percentage;
  
  if (isNaN(numPercentage)) {
    return { isValid: false, error: 'Percentage must be a valid number' };
  }
  
  if (numPercentage < 0 || numPercentage > 100) {
    return { isValid: false, error: 'Percentage must be between 0 and 100' };
  }
  
  return { isValid: true, error: null };
};

/**
 * Validate entire form object.
 * @param {object} formData - Form data object
 * @param {object} validationRules - Validation rules object
 * @returns {object} { isValid: boolean, errors: object }
 */
export const validateForm = (formData, validationRules) => {
  const errors = {};
  let isValid = true;
  
  Object.keys(validationRules).forEach(field => {
    const rule = validationRules[field];
    const value = formData[field];
    
    let result;
    switch (rule.type) {
      case 'amount':
        result = validateAmount(value);
        break;
      case 'date':
        result = validateDate(value);
        break;
      case 'required':
        result = validateRequired(value, rule.label, rule.minLength);
        break;
      case 'category':
        result = validateCategory(value);
        break;
      case 'phone':
        result = validatePhone(value);
        break;
      case 'percentage':
        result = validatePercentage(value);
        break;
      default:
        result = { isValid: true, error: null };
    }
    
    if (!result.isValid) {
      errors[field] = result.error;
      isValid = false;
    }
  });
  
  return { isValid, errors };
};

export default {
  validateAmount,
  validateDate,
  validateRequired,
  validateCategory,
  validatePhone,
  validateDateRange,
  validatePercentage,
  validateForm,
};
