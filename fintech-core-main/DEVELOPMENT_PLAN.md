# Development Plan & Module Checklist

## Project: AI-Based Personal Finance Advisor

---

## Development Phases Overview

| Phase | Focus Area | Duration Est. | Priority |
|-------|-----------|---------------|----------|
| 1 | Foundation & Setup | 2-3 hours | CRITICAL |
| 2 | Core CRUD (Income/Expenses) | 4-5 hours | CRITICAL |
| 3 | Machine Learning Integration | 3-4 hours | HIGH |
| 4 | Python Analytics Engine | 3-4 hours | HIGH |
| 5 | Intelligence Layer (Health Score) | 2-3 hours | HIGH |
| 6 | Alerts & Reports | 2-3 hours | MEDIUM |
| 7 | Dashboard & UI | 3-4 hours | HIGH |
| 8 | Testing & Documentation | 2-3 hours | HIGH |
| 9 | Optional: RAG Assistant | 2-3 hours | LOW |

**Total Estimated Time:** 23-32 hours

---

## Phase 1: Foundation & Setup

### Objectives
- Set up project structure
- Install and verify dependencies
- Establish MongoDB connection
- Configure environment variables

### Tasks

#### Backend Setup
- [ ] Create backend folder structure
- [ ] Create `requirements.txt` with all dependencies
- [ ] Create virtual environment and install packages
- [ ] Create `.env.example` file
- [ ] Create `config.py` for configuration management
- [ ] Create `app.py` Flask application entry point
- [ ] Implement CORS configuration
- [ ] Test Flask server starts successfully

#### Frontend Setup
- [ ] Create frontend folder using Vite + React
- [ ] Install dependencies (React, Tailwind, Recharts, Axios, React Router)
- [ ] Configure Tailwind CSS
- [ ] Create folder structure (pages, components, api, utils)
- [ ] Create API client base configuration
- [ ] Test development server starts successfully

#### Database Setup
- [ ] Install MongoDB locally or configure MongoDB Atlas
- [ ] Create database: `finance_advisor`
- [ ] Create collections: `income`, `expenses`, `budgets`, `ml_models`, `alerts`, `settings`
- [ ] Implement MongoDB connection utility (`utils/db_connection.py`)
- [ ] Add schema validation rules
- [ ] Create indexes for performance
- [ ] Test connection from Python

### Acceptance Criteria
- ✅ Backend Flask server runs on http://localhost:5000
- ✅ Frontend React app runs on http://localhost:5173
- ✅ MongoDB connection established successfully
- ✅ All dependencies installed without errors
- ✅ Environment variables template created

### Verification Commands
```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
npm install
npm run dev

# MongoDB
python -c "from pymongo import MongoClient; client = MongoClient('mongodb://localhost:27017/'); print('Connected:', client.server_info()['version'])"
```

---

## Phase 2: Core CRUD (Income & Expenses)

### Objectives
- Implement complete income management
- Implement complete expense management
- Create reusable MongoDB models
- Build REST API endpoints
- Create frontend forms and tables
- Implement filtering and search

### Backend Tasks

#### Income Module
- [ ] Create `models/income_model.py` with schema and validation
- [ ] Create `services/income_service.py` with business logic:
  - [ ] Create income
  - [ ] Get all incomes (with filtering by date range, source)
  - [ ] Get income by ID
  - [ ] Update income
  - [ ] Delete income
  - [ ] Get income summary (total, by source, by period)
- [ ] Create `api/income_routes.py` with endpoints:
  - [ ] `POST /api/income` - Create income
  - [ ] `GET /api/income` - List all (with query params)
  - [ ] `GET /api/income/<id>` - Get single
  - [ ] `PUT /api/income/<id>` - Update
  - [ ] `DELETE /api/income/<id>` - Delete
  - [ ] `GET /api/income/summary` - Get summary statistics
- [ ] Implement input validation
- [ ] Implement error handling
- [ ] Add logging

#### Expense Module
- [ ] Create `models/expense_model.py` with schema and validation
- [ ] Create `services/expense_service.py` with business logic:
  - [ ] Create expense
  - [ ] Get all expenses (with filtering by date, category, amount range)
  - [ ] Search expenses by description
  - [ ] Get expense by ID
  - [ ] Update expense
  - [ ] Delete expense
  - [ ] Get expense summary (total, by category, by period)
  - [ ] Get category breakdown
- [ ] Create `api/expense_routes.py` with endpoints:
  - [ ] `POST /api/expenses` - Create expense
  - [ ] `GET /api/expenses` - List all (with query params)
  - [ ] `GET /api/expenses/<id>` - Get single
  - [ ] `PUT /api/expenses/<id>` - Update
  - [ ] `DELETE /api/expenses/<id>` - Delete
  - [ ] `GET /api/expenses/summary` - Get summary statistics
  - [ ] `GET /api/expenses/by-category` - Category breakdown
- [ ] Implement input validation
- [ ] Implement error handling
- [ ] Add logging

#### Utilities
- [ ] Create `utils/validators.py` - Input validation helpers
- [ ] Create `utils/date_utils.py` - Date parsing and formatting
- [ ] Implement duplicate detection logic (optional)

### Frontend Tasks

#### API Client
- [ ] Create `api/client.js` - Axios instance with base URL and interceptors
- [ ] Create `api/incomeApi.js` - Income API functions
- [ ] Create `api/expenseApi.js` - Expense API functions
- [ ] Implement error handling in API client

#### Income Components
- [ ] Create `components/income/IncomeForm.jsx` - Form for create/edit
- [ ] Create `components/income/IncomeTable.jsx` - Table with actions
- [ ] Create `pages/IncomeManager.jsx` - Main income management page
- [ ] Implement form validation
- [ ] Implement date picker
- [ ] Implement filter controls (date range, source)
- [ ] Implement loading states
- [ ] Implement error messages
- [ ] Implement success notifications

#### Expense Components
- [ ] Create `components/expense/ExpenseForm.jsx` - Form for create/edit
- [ ] Create `components/expense/ExpenseTable.jsx` - Table with actions
- [ ] Create `pages/ExpenseManager.jsx` - Main expense management page
- [ ] Implement form validation
- [ ] Implement category dropdown
- [ ] Implement search functionality
- [ ] Implement filter controls (date range, category, amount)
- [ ] Implement loading states
- [ ] Implement error messages
- [ ] Implement success notifications

#### Common Components
- [ ] Create `components/common/Button.jsx` - Reusable button
- [ ] Create `components/common/Input.jsx` - Reusable input
- [ ] Create `components/common/Modal.jsx` - Reusable modal
- [ ] Create `components/common/Loading.jsx` - Loading spinner
- [ ] Create `components/common/ErrorMessage.jsx` - Error display

#### Utilities
- [ ] Create `utils/formatters.js` - Currency and date formatting
- [ ] Create `utils/validators.js` - Frontend validation

### Acceptance Criteria
- ✅ Can create, read, update, delete incomes via API and UI
- ✅ Can create, read, update, delete expenses via API and UI
- ✅ Filtering and search work correctly
- ✅ Validation prevents invalid data entry
- ✅ Data persists in MongoDB
- ✅ UI updates reflect database state
- ✅ Error handling works (network errors, validation errors)
- ✅ Loading states display during API calls

### Testing Checklist
- [ ] Create income with valid data → Success
- [ ] Create income with invalid data → Validation error
- [ ] Get all incomes → Returns list
- [ ] Filter incomes by date range → Returns filtered list
- [ ] Update income → Changes reflected
- [ ] Delete income → Removed from database
- [ ] Same tests for expenses
- [ ] Search expenses by description → Returns matching results
- [ ] Filter expenses by category → Returns filtered list

---

## Phase 3: Machine Learning Integration

### Objectives
- Implement expense categorization (Naive Bayes)
- Implement expense prediction (Linear Regression)
- Implement anomaly detection (Isolation Forest)
- Create model training pipeline
- Create prediction endpoints
- Display ML insights in frontend

### Backend Tasks

#### ML Service Core
- [ ] Create `ml/__init__.py`
- [ ] Create `ml/saved_models/` directory with `.gitkeep`
- [ ] Create `ml/trainer.py` - Model training orchestrator:
  - [ ] Data fetching from MongoDB
  - [ ] Data preprocessing
  - [ ] Train/test split
  - [ ] Model training
  - [ ] Accuracy calculation
  - [ ] Model persistence (joblib)
  - [ ] Metadata storage in MongoDB

#### Expense Categorization
- [ ] Create `ml/categorizer.py`:
  - [ ] TF-IDF vectorization of descriptions
  - [ ] MultinomialNB training
  - [ ] Prediction function
  - [ ] Confidence score calculation
  - [ ] Handle unseen vocabulary
- [ ] Create training endpoint: `POST /api/ml/train-categorizer`
- [ ] Create prediction endpoint: `POST /api/ml/predict-category`
- [ ] Implement minimum sample check (50+)
- [ ] Add logging and error handling

#### Expense Prediction
- [ ] Create `ml/predictor.py`:
  - [ ] Feature engineering (month, category, trends)
  - [ ] Linear Regression training
  - [ ] Prediction for next period
  - [ ] Calculate MAE and R² score
- [ ] Create training endpoint: `POST /api/ml/train-predictor`
- [ ] Create prediction endpoint: `POST /api/ml/predict-expenses`
- [ ] Implement minimum sample check
- [ ] Handle sparse data gracefully

#### Anomaly Detection
- [ ] Create `ml/anomaly_detector.py`:
  - [ ] Feature extraction (amount, category, day, time)
  - [ ] Isolation Forest training
  - [ ] Anomaly prediction
  - [ ] Configurable contamination parameter
- [ ] Create training endpoint: `POST /api/ml/train-anomaly-detector`
- [ ] Create detection endpoint: `POST /api/ml/detect-anomaly`
- [ ] Automatically flag expenses on creation (optional)
- [ ] Store anomaly flag in expense document

#### ML Service Integration
- [ ] Create `services/ml_service.py` - High-level ML operations
- [ ] Create `api/ml_routes.py` - ML API endpoints
- [ ] Implement model loading on server start
- [ ] Implement automatic retraining logic (optional)
- [ ] Add comprehensive error handling

### Frontend Tasks

#### ML API Client
- [ ] Create `api/mlApi.js` - ML API functions:
  - [ ] trainCategorizer()
  - [ ] predictCategory(description)
  - [ ] trainPredictor()
  - [ ] predictExpenses(params)
  - [ ] trainAnomalyDetector()
  - [ ] detectAnomaly(expense)

#### ML Insights Page
- [ ] Create `pages/MLInsights.jsx` - ML dashboard:
  - [ ] Model training section
  - [ ] Training status display
  - [ ] Model accuracy display
  - [ ] Last trained date
  - [ ] Training controls (buttons)
- [ ] Create `components/insights/ModelCard.jsx` - Individual model display
- [ ] Create `components/insights/PredictionPanel.jsx` - Test predictions
- [ ] Display anomalous expenses with highlighting
- [ ] Show predicted categories on expense form (optional)

### Acceptance Criteria
- ✅ Categorizer trains with sufficient data and saves model
- ✅ Categorizer predicts category for new description
- ✅ Predictor trains and forecasts next month's expenses
- ✅ Anomaly detector identifies unusual expenses
- ✅ Models persist and reload after server restart
- ✅ Accuracy metrics are calculated and displayed
- ✅ Insufficient data is handled gracefully
- ✅ Frontend displays ML insights clearly

### Testing Checklist
- [ ] Train categorizer with 100 labeled expenses → Model saved
- [ ] Predict category for "coffee at starbucks" → Returns "Food" or similar
- [ ] Train predictor with 3 months of data → Model saved, R² > 0.5
- [ ] Predict next month expenses → Returns reasonable forecast
- [ ] Train anomaly detector → Model saved
- [ ] Detect anomaly for unusually high expense → Flags as anomaly
- [ ] Restart server → Models reload successfully
- [ ] Train with <50 samples → Returns error message

---

## Phase 4: MATLAB Analytics Engine

### Objectives
- Create MATLAB analysis scripts
- Implement Python-MATLAB integration
- Create analytics endpoints
- Display MATLAB outputs in frontend
- Handle MATLAB unavailability gracefully

### Backend Tasks

#### MATLAB Integration Core
- [ ] Create `matlab/__init__.py`
- [ ] Create `matlab/scripts/` directory for .m files
- [ ] Create `matlab/data/` directory for CSV input/output
- [ ] Create `matlab/matlab_engine.py` - MATLAB Engine wrapper:
  - [ ] Engine initialization
  - [ ] Data conversion (NumPy ↔ MATLAB)
  - [ ] Script execution
  - [ ] Result retrieval
  - [ ] Error handling
- [ ] Create `matlab/matlab_adapter.py` - Batch CSV fallback:
  - [ ] Write data to CSV
  - [ ] Execute MATLAB script via command line
  - [ ] Read output CSV
  - [ ] Parse results
- [ ] Implement availability detection on server start

#### MATLAB Scripts

##### spending_trends.m
- [ ] Create script that:
  - [ ] Reads input data (dates, amounts, categories)
  - [ ] Calculates 7-day moving average
  - [ ] Calculates 30-day moving average
  - [ ] Fits linear trend line
  - [ ] Calculates month-over-month growth
  - [ ] Generates trend chart (PNG)
  - [ ] Returns results as struct/CSV
- [ ] Test script independently in MATLAB
- [ ] Document required inputs and outputs

##### risk_analysis.m
- [ ] Create script that:
  - [ ] Calculates expense standard deviation
  - [ ] Calculates coefficient of variation
  - [ ] Calculates expense-to-income ratio
  - [ ] Computes risk score (0-100)
  - [ ] Generates variability chart (PNG)
  - [ ] Returns metrics struct/CSV
- [ ] Test script independently
- [ ] Document calculation formulas

##### investment_allocation.m
- [ ] Create script that:
  - [ ] Takes risk tolerance, age, time horizon
  - [ ] Applies age-based equity rule: equity% = 110 - age
  - [ ] Adjusts for risk tolerance
  - [ ] Calculates allocation percentages
  - [ ] Generates pie chart (PNG)
  - [ ] Returns allocation struct/CSV
- [ ] Test script independently
- [ ] Add disclaimer in output

##### financial_metrics.m
- [ ] Create script that:
  - [ ] Calculates savings rate
  - [ ] Calculates debt-to-income ratio
  - [ ] Calculates emergency fund months
  - [ ] Calculates financial health components
  - [ ] Generates summary report
  - [ ] Returns metrics struct/CSV
- [ ] Test script independently
- [ ] Document metric definitions

#### MATLAB Service Integration
- [ ] Create `services/matlab_service.py`:
  - [ ] analyze_spending_trends(expenses)
  - [ ] analyze_risk(expenses, income)
  - [ ] calculate_investment_allocation(params)
  - [ ] calculate_financial_metrics(financial_data)
- [ ] Create `api/matlab_routes.py`:
  - [ ] `POST /api/matlab/spending-trends`
  - [ ] `POST /api/matlab/risk-analysis`
  - [ ] `POST /api/matlab/investment-allocation`
  - [ ] `POST /api/matlab/financial-metrics`
  - [ ] `GET /api/matlab/status` - Check MATLAB availability
- [ ] Implement result caching (optional)
- [ ] Add comprehensive error handling
- [ ] Return clear errors when MATLAB unavailable

### Frontend Tasks

#### MATLAB API Client
- [ ] Create `api/matlabApi.js` - MATLAB API functions:
  - [ ] analyzeSpendingTrends(dateRange)
  - [ ] analyzeRisk()
  - [ ] calculateInvestmentAllocation(params)
  - [ ] calculateFinancialMetrics()
  - [ ] checkMatlabStatus()

#### MATLAB Analytics Page
- [ ] Create `pages/MatlabAnalytics.jsx`:
  - [ ] MATLAB status indicator
  - [ ] Spending trends section with chart
  - [ ] Risk analysis section with metrics
  - [ ] Investment allocation section with pie chart
  - [ ] Financial metrics summary
  - [ ] Refresh/recalculate buttons
- [ ] Handle MATLAB unavailable state
- [ ] Display MATLAB-generated charts (embed PNGs or render data)
- [ ] Show loading states during calculations
- [ ] Display calculation timestamps

### Acceptance Criteria
- ✅ MATLAB scripts execute successfully in MATLAB environment
- ✅ Python successfully calls MATLAB (Engine or batch mode)
- ✅ All four analytics scripts produce correct outputs
- ✅ Results are returned to frontend and displayed
- ✅ Charts generated by MATLAB are visible
- ✅ System works without MATLAB (with clear messaging)
- ✅ Errors are handled and logged appropriately

### Testing Checklist
- [ ] Run `spending_trends.m` in MATLAB → Generates chart and data
- [ ] Call `/api/matlab/spending-trends` → Returns trend data
- [ ] Run `risk_analysis.m` → Calculates risk metrics
- [ ] Call `/api/matlab/risk-analysis` → Returns risk score
- [ ] Run `investment_allocation.m` → Returns allocation percentages
- [ ] Run `financial_metrics.m` → Calculates all metrics
- [ ] Test with MATLAB unavailable → Returns error, app continues
- [ ] Verify batch mode fallback works if Engine unavailable

---

## Phase 5: Intelligence Layer (Health Score & Recommendations)

### Objectives
- Implement Financial Health Score calculation
- Implement budget recommendations
- Implement investment planner
- Display insights in dashboard

### Backend Tasks

#### Financial Health Service
- [ ] Create `services/financial_health_service.py`:
  - [ ] calculate_savings_rate(income, expenses)
  - [ ] calculate_budget_adherence(actual, budgeted)
  - [ ] calculate_debt_to_income_ratio(debts, income)
  - [ ] calculate_emergency_fund_months(savings, monthly_expenses)
  - [ ] calculate_spending_consistency(expense_history)
  - [ ] calculate_financial_health_score(components) - weighted formula
  - [ ] get_health_interpretation(score)
- [ ] Create endpoint: `GET /api/financial-health`
- [ ] Document scoring formula clearly
- [ ] Add detailed breakdown in response

#### Budget Service
- [ ] Create `services/budget_service.py`:
  - [ ] get_current_budgets()
  - [ ] set_budget(category, amount)
  - [ ] calculate_budget_recommendations(income, expenses, savings_goal):
    - [ ] Apply 50-30-20 rule as baseline
    - [ ] Adjust based on actual spending patterns
    - [ ] Recommend per-category budgets
  - [ ] get_budget_vs_actual(month)
- [ ] Create endpoints:
  - [ ] `GET /api/budgets` - Get all budgets
  - [ ] `POST /api/budgets` - Set budget for category
  - [ ] `GET /api/budgets/recommendations` - Get recommended budgets
  - [ ] `GET /api/budgets/comparison` - Budget vs. actual
- [ ] Implement MongoDB budget storage

#### Investment Planner Service
- [ ] Create `services/investment_planner.py`:
  - [ ] calculate_allocation(risk_tolerance, time_horizon, age):
    - [ ] Conservative: 30% equity, 60% bonds, 10% cash
    - [ ] Moderate: 60% equity, 30% bonds, 10% cash
    - [ ] Aggressive: 80% equity, 15% bonds, 5% cash
    - [ ] Age adjustment
  - [ ] generate_investment_plan(financial_goals, params)
  - [ ] Add disclaimers
- [ ] Create endpoint: `POST /api/investment-plan`
- [ ] Include educational explanations
- [ ] Clear disclaimer: not financial advice

### Frontend Tasks

#### Health Score Display
- [ ] Create `components/insights/FinancialHealthCard.jsx`:
  - [ ] Display score (0-100) with color coding
  - [ ] Show interpretation (Excellent/Good/Fair/Poor)
  - [ ] Display component breakdown (chart or table)
  - [ ] Show calculation details (expandable)
  - [ ] Recommendations for improvement

#### Budget Recommendations
- [ ] Create `components/insights/BudgetRecommendation.jsx`:
  - [ ] Display current budgets
  - [ ] Display recommended budgets
  - [ ] Show comparison (current vs. recommended)
  - [ ] "Apply recommendations" button
  - [ ] Category-by-category breakdown

#### Investment Planner
- [ ] Create `components/insights/InvestmentPlan.jsx`:
  - [ ] Input form (risk tolerance, time horizon, goals)
  - [ ] Display allocation percentages
  - [ ] Pie chart visualization
  - [ ] Educational explanations
  - [ ] Prominent disclaimer
- [ ] Create `pages/InvestmentPlanner.jsx` - Standalone page

#### Dashboard Integration
- [ ] Update `pages/Dashboard.jsx` to include:
  - [ ] Financial Health Score card (prominent)
  - [ ] Budget recommendations section
  - [ ] Quick investment planner access

### Acceptance Criteria
- ✅ Financial Health Score calculates correctly
- ✅ Score components are transparent and explainable
- ✅ Budget recommendations based on 50-30-20 rule
- ✅ Investment allocations adjust for risk and age
- ✅ All calculations documented and verifiable
- ✅ Frontend displays insights clearly
- ✅ Disclaimers are prominent

### Testing Checklist
- [ ] Calculate health score with known inputs → Verify result matches manual calculation
- [ ] Test edge cases: no income, no expenses, high debt → Handles gracefully
- [ ] Request budget recommendations → Returns reasonable percentages summing to 100%
- [ ] Generate investment plan (conservative, 25yo) → Returns appropriate allocation
- [ ] Generate investment plan (aggressive, 55yo) → Returns age-adjusted allocation
- [ ] Verify all disclaimers are visible

---

## Phase 6: Alerts & Reports

### Objectives
- Implement SMS alert system
- Implement PDF report generation
- Implement CSV export
- Create notification settings

### Backend Tasks

#### Alert System
- [ ] Create `models/alert_model.py` - Alert schema
- [ ] Create `notifications/sms_provider.py`:
  - [ ] Initialize Twilio client
  - [ ] send_sms(phone_number, message)
  - [ ] Format alert messages
  - [ ] Log SMS status
  - [ ] Handle errors (invalid number, API failure)
- [ ] Create `services/alert_service.py`:
  - [ ] check_budget_overrun(expense, budget)
  - [ ] check_anomaly_alert(expense)
  - [ ] check_low_savings_alert(month_end_data)
  - [ ] check_high_daily_spending(daily_total, limit)
  - [ ] trigger_alert(alert_type, data)
  - [ ] get_user_settings() - phone number, thresholds
- [ ] Create `api/alert_routes.py`:
  - [ ] `GET /api/alerts` - List all alerts
  - [ ] `GET /api/alerts/settings` - Get notification settings
  - [ ] `PUT /api/alerts/settings` - Update settings
  - [ ] `POST /api/alerts/test` - Send test SMS
- [ ] Integrate alert checks into expense creation flow
- [ ] Store alert history in MongoDB

#### Report Generation
- [ ] Create `reports/pdf_generator.py`:
  - [ ] generate_financial_report(start_date, end_date):
    - [ ] Income summary
    - [ ] Expense summary by category
    - [ ] Charts (embedded images)
    - [ ] Financial health score
    - [ ] Budget comparison
  - [ ] Use ReportLab for PDF creation
  - [ ] Professional formatting
  - [ ] Header/footer with date
- [ ] Create `reports/csv_exporter.py`:
  - [ ] export_income_csv(start_date, end_date)
  - [ ] export_expenses_csv(start_date, end_date)
  - [ ] export_summary_csv(start_date, end_date)
- [ ] Create `api/report_routes.py`:
  - [ ] `GET /api/reports/pdf` - Generate and download PDF
  - [ ] `GET /api/reports/csv/income` - Export income CSV
  - [ ] `GET /api/reports/csv/expenses` - Export expenses CSV
- [ ] Create `reports/output/` directory for generated files
- [ ] Implement file cleanup (delete old reports)

### Frontend Tasks

#### Alert Settings
- [ ] Create `pages/Settings.jsx`:
  - [ ] Notification settings form
  - [ ] Phone number input
  - [ ] Enable/disable toggles for each alert type
  - [ ] Threshold inputs (budget %, daily limit, savings target)
  - [ ] Save button
  - [ ] Test SMS button
- [ ] Display alert history (optional)

#### Reports Section
- [ ] Create `pages/Reports.jsx`:
  - [ ] Date range selector
  - [ ] Report type selector (PDF, CSV)
  - [ ] Generate report button
  - [ ] Download link
  - [ ] Report preview (optional)
- [ ] Create `api/reportApi.js` - Report API functions
- [ ] Handle file downloads in browser

#### Alert Notifications (Frontend)
- [ ] Display recent alerts in dashboard
- [ ] Badge/icon for unread alerts (optional)

### Acceptance Criteria
- ✅ SMS alerts trigger correctly for configured events
- ✅ Test SMS sends successfully
- ✅ PDF report generates with correct data
- ✅ CSV exports contain accurate data
- ✅ User can configure notification settings
- ✅ Alert history is stored and accessible
- ✅ Twilio credentials are never exposed

### Testing Checklist
- [ ] Create expense exceeding budget → SMS alert sent (if configured)
- [ ] Create anomalous expense → SMS alert sent
- [ ] Send test SMS → Receives SMS on configured phone
- [ ] Generate PDF report for date range → PDF downloads correctly
- [ ] Export income CSV → CSV contains correct data
- [ ] Export expenses CSV → CSV contains correct data
- [ ] Update alert settings → Settings persist

---

## Phase 7: Dashboard & UI Polish

### Objectives
- Create comprehensive dashboard
- Integrate all charts
- Implement responsive design
- Add loading and error states
- Polish user experience

### Frontend Tasks

#### Dashboard Implementation
- [ ] Create `pages/Dashboard.jsx`:
  - [ ] Overview cards (total income, total expenses, savings, health score)
  - [ ] Spending trend line chart (Recharts)
  - [ ] Category breakdown pie chart
  - [ ] Income vs. Expenses bar chart
  - [ ] Recent transactions list
  - [ ] ML insights summary
  - [ ] Alerts/notifications panel
  - [ ] Quick action buttons
- [ ] Implement date range filter for dashboard
- [ ] Implement refresh functionality
- [ ] Add tooltips to charts
- [ ] Add drill-down capability (click chart → details)

#### Chart Components
- [ ] Create `components/charts/LineChart.jsx` - Recharts LineChart wrapper
- [ ] Create `components/charts/BarChart.jsx` - Recharts BarChart wrapper
- [ ] Create `components/charts/PieChart.jsx` - Recharts PieChart wrapper
- [ ] Create `components/charts/AreaChart.jsx` - Recharts AreaChart wrapper
- [ ] Ensure responsive design
- [ ] Add legends and labels
- [ ] Implement color schemes

#### Navigation & Layout
- [ ] Create `components/layout/Navbar.jsx` - Top navigation
- [ ] Create `components/layout/Sidebar.jsx` - Side navigation (optional)
- [ ] Implement React Router routes:
  - [ ] `/` - Dashboard
  - [ ] `/income` - Income Manager
  - [ ] `/expenses` - Expense Manager
  - [ ] `/ml-insights` - ML Insights
  - [ ] `/matlab-analytics` - MATLAB Analytics
  - [ ] `/investment-planner` - Investment Planner
  - [ ] `/reports` - Reports
  - [ ] `/settings` - Settings
- [ ] Active route highlighting
- [ ] Mobile-responsive navigation

#### UI/UX Polish
- [ ] Consistent spacing and typography
- [ ] Color scheme and theme
- [ ] Loading spinners for async operations
- [ ] Error boundaries for error handling
- [ ] Empty states for no data
- [ ] Success/error toast notifications
- [ ] Confirm dialogs for delete operations
- [ ] Form validation feedback
- [ ] Accessibility (ARIA labels, keyboard navigation)

#### Context & State Management
- [ ] Create `context/AppContext.jsx`:
  - [ ] Global state for user settings
  - [ ] Selected date range
  - [ ] Toast notifications
  - [ ] MATLAB availability status
- [ ] Implement context provider in App.jsx
- [ ] Use context in components

### Acceptance Criteria
- ✅ Dashboard displays all key metrics and charts
- ✅ Charts update when data changes
- ✅ Navigation works smoothly between pages
- ✅ UI is responsive on different screen sizes
- ✅ Loading states prevent user confusion
- ✅ Errors are displayed clearly
- ✅ User actions feel responsive
- ✅ Design is consistent across pages

### Testing Checklist
- [ ] Load dashboard with data → All charts render
- [ ] Load dashboard with no data → Shows empty state
- [ ] Navigate between pages → Smooth transitions
- [ ] Resize window → UI adapts responsively
- [ ] Trigger API error → Error message displays
- [ ] Long API call → Loading spinner shows
- [ ] Delete item → Confirm dialog appears
- [ ] Test on mobile device → Usable interface

---

## Phase 8: Testing & Documentation

### Objectives
- Write unit tests for critical functions
- Write integration tests for API endpoints
- Create comprehensive README
- Document setup instructions
- Prepare viva materials

### Backend Testing

#### Unit Tests (pytest)
- [ ] Create `tests/test_validators.py`:
  - [ ] Test amount validation
  - [ ] Test date validation
  - [ ] Test category validation
- [ ] Create `tests/test_income_service.py`:
  - [ ] Test create_income()
  - [ ] Test get_income_summary()
  - [ ] Test date filtering
- [ ] Create `tests/test_expense_service.py`:
  - [ ] Test create_expense()
  - [ ] Test get_expense_summary()
  - [ ] Test category breakdown
- [ ] Create `tests/test_financial_health.py`:
  - [ ] Test health score calculation with known inputs
  - [ ] Test edge cases (zero income, etc.)
- [ ] Create `tests/test_ml_service.py`:
  - [ ] Test categorizer with sample data
  - [ ] Test predictor with sample data
  - [ ] Test anomaly detector

#### Integration Tests
- [ ] Create `tests/test_income_api.py`:
  - [ ] Test full request-response cycle
  - [ ] Test error responses
- [ ] Create `tests/test_expense_api.py`:
  - [ ] Test CRUD operations via API
- [ ] Create `tests/test_ml_integration.py`:
  - [ ] Test train → save → load → predict flow
- [ ] Create `tests/test_matlab_integration.py`:
  - [ ] Test MATLAB script execution (if MATLAB available)

#### Test Configuration
- [ ] Create `tests/conftest.py` - pytest fixtures
- [ ] Setup test MongoDB database
- [ ] Create sample test data generators
- [ ] Run all tests: `pytest tests/ -v`

### Documentation

#### README.md
- [ ] Create comprehensive `README.md`:
  - [ ] Project title and description
  - [ ] Features list
  - [ ] Technology stack
  - [ ] Prerequisites
  - [ ] Installation instructions (step-by-step)
  - [ ] Configuration (environment variables)
  - [ ] Running the application
  - [ ] Project structure overview
  - [ ] API documentation (endpoints)
  - [ ] ML models documentation
  - [ ] MATLAB integration setup
  - [ ] Testing instructions
  - [ ] Known limitations
  - [ ] Troubleshooting
  - [ ] Screenshots (optional)
  - [ ] License

#### Setup Guides
- [ ] Create `SETUP_MONGODB.md` - MongoDB setup guide
- [ ] Create `SETUP_MATLAB.md` - MATLAB integration guide
- [ ] Create `SETUP_TWILIO.md` - Twilio SMS setup guide
- [ ] Create `.env.example` - Environment variables template with comments

#### API Documentation
- [ ] Create `API_DOCUMENTATION.md`:
  - [ ] All endpoints with request/response examples
  - [ ] Error codes
  - [ ] Authentication (N/A for this version)

#### Viva Preparation
- [ ] Create `VIVA_QA.md` - Common viva questions and answers:
  - [ ] Why this tech stack?
  - [ ] How does ML work in this project?
  - [ ] MATLAB integration explanation
  - [ ] Financial health score formula
  - [ ] Security considerations
  - [ ] Limitations and future enhancements
  - [ ] Design decisions and tradeoffs
- [ ] Create `DEMO_SCRIPT.md` - Step-by-step demo walkthrough
- [ ] Prepare sample data for demonstration

### Acceptance Criteria
- ✅ All critical functions have unit tests
- ✅ API endpoints have integration tests
- ✅ Test coverage >60% (ideal: >80%)
- ✅ README is comprehensive and clear
- ✅ Setup can be completed by following docs alone
- ✅ Viva materials cover expected questions
- ✅ Demo script tested end-to-end

### Testing Checklist
- [ ] Run `pytest tests/ -v` → All tests pass
- [ ] Follow README setup from scratch → Application runs
- [ ] Review VIVA_QA.md → All answers accurate
- [ ] Execute DEMO_SCRIPT.md → No errors

---

## Phase 9 (Optional): RAG Knowledge Assistant

### Objectives
- Implement document ingestion pipeline
- Create embedding and vector store
- Implement retrieval mechanism
- Integrate LLM for generation
- Create Q&A interface

### Backend Tasks

#### RAG Core
- [ ] Create `rag/` directory structure:
  - [ ] `documents/` - PDF storage
  - [ ] `embeddings/` - FAISS index storage
- [ ] Create `services/rag_service.py`:
  - [ ] load_documents() - PDF parsing
  - [ ] chunk_documents() - Text chunking
  - [ ] create_embeddings() - sentence-transformers
  - [ ] build_faiss_index()
  - [ ] search_similar(query, k=3)
  - [ ] generate_answer(query, context, llm_client)
- [ ] Create embedding script: `scripts/build_rag_index.py`
- [ ] Create `api/rag_routes.py`:
  - [ ] `POST /api/rag/ask` - Ask question
  - [ ] `GET /api/rag/status` - Check RAG availability
- [ ] Implement OpenAI/Ollama client
- [ ] Handle LLM API unavailable gracefully

#### Document Collection
- [ ] Source 5-10 trusted financial literacy PDFs
- [ ] Place in `rag/documents/`
- [ ] Document sources clearly
- [ ] Run embedding script

### Frontend Tasks

#### RAG Interface
- [ ] Create `pages/FinancialAssistant.jsx`:
  - [ ] Chat interface
  - [ ] Question input
  - [ ] Answer display with sources
  - [ ] Conversation history
  - [ ] Disclaimer banner
- [ ] Create `components/rag/ChatMessage.jsx`
- [ ] Create `api/ragApi.js`
- [ ] Display "RAG unavailable" if not configured

### Acceptance Criteria
- ✅ Documents embedded successfully
- ✅ Questions return relevant answers
- ✅ Sources are cited
- ✅ Works without RAG (graceful degradation)
- ✅ LLM API key configurable
- ✅ Disclaimers are prominent

### Testing Checklist
- [ ] Ask "What is the 50-30-20 rule?" → Returns accurate answer with source
- [ ] Ask unrelated question → Returns "not found in documents"
- [ ] Test without LLM API key → Returns error message
- [ ] Verify app works without RAG enabled

---

## Pre-Implementation Checklist

Before starting implementation, verify:

### Prerequisites
- [ ] MongoDB installed or Atlas account created
- [ ] MATLAB installed (optional, document if not available)
- [ ] Python 3.9+ installed
- [ ] Node.js 16+ and npm installed
- [ ] Git installed
- [ ] Code editor (VS Code recommended)

### Environment Preparation
- [ ] Workspace folder created: `fincore analytics`
- [ ] Architecture document reviewed
- [ ] Development plan understood
- [ ] Twilio account created (optional, for SMS)
- [ ] OpenAI API key obtained (optional, for RAG)

### Understanding Check
- [ ] Understand project scope and objectives
- [ ] Understand module dependencies
- [ ] Understand MATLAB integration options
- [ ] Understand testing requirements
- [ ] Understand that this is NOT production-ready
- [ ] Understand single-user limitation

---

## Post-Implementation Checklist

After completing development:

### Functionality Verification
- [ ] All CRUD operations work
- [ ] ML models train and predict
- [ ] MATLAB analytics execute (or clear unavailable message)
- [ ] Financial health score calculates
- [ ] Alerts trigger (test mode)
- [ ] Reports generate
- [ ] Dashboard displays correctly

### Quality Verification
- [ ] No console errors in frontend
- [ ] No server errors in backend logs
- [ ] Data persists across restarts
- [ ] Edge cases handled
- [ ] Error messages are clear
- [ ] Loading states work

### Documentation Verification
- [ ] README is complete
- [ ] Setup guides are accurate
- [ ] API documentation is current
- [ ] Code comments are present
- [ ] Viva materials prepared

### Demo Preparation
- [ ] Sample data loaded
- [ ] Demo script tested
- [ ] Screenshots captured
- [ ] Known issues documented
- [ ] Backup of working version created

---

## Risk Mitigation

### Potential Blockers and Solutions

| Risk | Impact | Mitigation |
|------|--------|-----------|
| MATLAB not available | HIGH | Implement batch fallback, document clearly, allow app to run without MATLAB |
| Insufficient ML training data | MEDIUM | Use synthetic data generator, document minimum requirements |
| MongoDB connection issues | HIGH | Provide detailed setup guide, test connection early |
| Twilio SMS API costs | LOW | Use test mode, make SMS optional, document clearly |
| Complex integration bugs | MEDIUM | Modular architecture, test each module independently first |
| Time constraints | MEDIUM | Prioritize phases 1-7, make phase 9 (RAG) truly optional |
| MATLAB Engine compatibility | MEDIUM | Test early, have batch mode ready as fallback |

---

## Success Metrics

### Minimum Viable Product (MVP)
- All Phase 1-5 features complete
- At least one chart on dashboard
- PDF report generation works
- Basic error handling
- README with setup instructions

### Complete Project
- All Phase 1-8 features complete
- Comprehensive testing
- Full documentation
- Demo-ready with sample data
- Viva materials prepared

### Excellent Project (Stretch)
- Phase 9 (RAG) implemented
- Test coverage >80%
- Professional UI/UX
- Comprehensive error handling
- Detailed code comments
- Performance optimizations

---

## Development Commands Reference

### Backend
```bash
# Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run server
python app.py

# Run tests
pytest tests/ -v

# Train ML models
python -m ml.trainer
```

### Frontend
```bash
# Setup
cd frontend
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Lint
npm run lint
```

### MongoDB
```bash
# Start MongoDB (Windows)
mongod --dbpath C:\data\db

# Connect to shell
mongosh

# Show databases
show dbs
use finance_advisor
show collections
```

### MATLAB
```bash
# Test MATLAB Engine
python -c "import matlab.engine; eng = matlab.engine.start_matlab(); print('MATLAB available')"

# Run script in batch mode
matlab -batch "run('matlab/scripts/spending_trends.m')"
```

---

**Document Version:** 1.0  
**Last Updated:** 2026-10-09  
**Status:** Ready for Student Review and Approval

**Next Step:** Review this plan, ask questions, then approve to begin Phase 1 implementation.
