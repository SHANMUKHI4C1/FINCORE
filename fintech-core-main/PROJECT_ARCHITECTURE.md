# AI-Based Personal Finance Advisor - Project Architecture

## Project Overview

**Title:** AI-Based Personal Finance Advisor using Machine Learning and Python Financial Analytics

**Purpose:** A comprehensive personal finance management system that combines traditional CRUD operations with advanced ML-based insights and Python-powered financial analytics.

**Target:** Final-year college project suitable for demonstration and viva defense.

---

## Technology Stack

### Frontend
- **Framework:** React.js 18.x
- **Styling:** Tailwind CSS 3.x
- **Charts:** Recharts 2.x
- **HTTP Client:** Axios
- **State Management:** React Hooks (useState, useEffect, useContext)
- **Routing:** React Router DOM 6.x

### Backend
- **Framework:** Flask 3.x (Python 3.9+)
- **CORS:** Flask-CORS
- **API Design:** RESTful principles
- **Environment:** python-dotenv

### Database
- **Database:** MongoDB 6.x+
- **Driver:** PyMongo 4.x
- **Schema Validation:** MongoDB schema validation rules
- **Indexing:** Compound indexes on date + category fields

### Machine Learning
- **Core Libraries:** scikit-learn 1.3+, pandas 2.x, NumPy 1.24+
- **Model Persistence:** joblib
- **Algorithms:**
  - Naive Bayes (MultinomialNB) for expense categorization
  - Linear Regression for expense prediction
  - Isolation Forest for anomaly detection

### Python Analytics
- **Libraries:** NumPy 1.24+, SciPy 1.10+, pandas 2.x
- **Integration:** Native Python modules
- **Capabilities:**
  - Statistical and Machine Learning computations
  - Financial calculations
  - Advanced numerical analysis

### Notifications
- **Provider:** Twilio SMS API
- **Configurable:** Environment-based credentials

### Reporting
- **PDF Generation:** ReportLab (Python)
- **CSV Export:** Python csv module

### Optional: RAG Knowledge Assistant
- **Embeddings:** sentence-transformers
- **Vector Store:** FAISS
- **LLM Provider:** OpenAI API or compatible endpoint (configurable)
- **Documents:** Trusted financial literacy PDFs

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (React)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │Dashboard │  │ Income/  │  │ Reports  │  │  ML Insights │  │
│  │  Charts  │  │ Expenses │  │   & PDF  │  │  & Health    │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘  │
│                              │                                  │
│                         API Client (Axios)                      │
└─────────────────────────────┬───────────────────────────────────┘
                              │ HTTP/REST
┌─────────────────────────────┴───────────────────────────────────┐
│                    BACKEND (Flask REST API)                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                     API Routes Layer                      │  │
│  │  /income  /expenses  /ml/predict  /analytics/analyze  /rag  │  │
│  └───────┬──────────────────────────────────────────────────┘  │
│          │                                                       │
│  ┌───────┴────────────────────────────────────────────────┐    │
│  │              Business Logic / Services                  │    │
│  │  IncomeService  ExpenseService  MLService  AlertService│    │
│  └───────┬────────────────────────────────────────────────┘    │
│          │                                                       │
│  ┌───────┴────────┬────────────┬───────────┬──────────────┐    │
│  │   Budget     │   ML       │ Analytics │ Notification │    │
│  │   Access       │   Models   │  Engine   │   Provider   │    │
│  │   (PyMongo)    │  (joblib)  │(NumPy/SciPy)│   (Twilio)   │    │
│  └────────────────┴────────────┴───────────┴──────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────┴───────────────────────────────────┐
│                         MongoDB Database                        │
│  Collections: income, expenses, budgets, ml_models, alerts      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Modular Architecture

### Backend Module Structure

```
backend/
├── app.py                      # Flask application entry point
├── config.py                   # Configuration and environment variables
├── requirements.txt            # Python dependencies
│
├── api/                        # API Routes (Controllers)
│   ├── __init__.py
│   ├── income_routes.py
│   ├── expense_routes.py
│   ├── ml_routes.py
│   ├── matlab_routes.py
│   ├── report_routes.py
│   ├── alert_routes.py
│   └── rag_routes.py           # Optional RAG assistant
│
├── services/                   # Business Logic
│   ├── __init__.py
│   ├── income_service.py
│   ├── expense_service.py
│   ├── budget_service.py
│   ├── ml_service.py
│   ├── analytics_service.py
│   ├── report_service.py
│   ├── alert_service.py
│   ├── financial_health_service.py
│   └── rag_service.py          # Optional
│
├── models/                     # Database Models & Validation
│   ├── __init__.py
│   ├── income_model.py
│   ├── expense_model.py
│   ├── budget_model.py
│   └── alert_model.py
│
├── ml/                         # Machine Learning
│   ├── __init__.py
│   ├── categorizer.py          # Naive Bayes categorization
│   ├── predictor.py            # Linear Regression prediction
│   ├── anomaly_detector.py     # Isolation Forest
│   ├── trainer.py              # Model training orchestrator
│   └── saved_models/           # Trained model files (.pkl)
│
├── matlab/                     # MATLAB Integration
│   ├── __init__.py
│   ├── matlab_engine.py        # MATLAB Engine wrapper
│   ├── matlab_adapter.py       # Batch/CSV fallback adapter
│   ├── scripts/                # MATLAB .m files
│   │   ├── spending_trends.m
│   │   ├── risk_analysis.m
│   │   ├── investment_allocation.m
│   │   └── financial_metrics.m
│   └── data/                   # Input/output CSV files
│
├── notifications/              # SMS Alerts
│   ├── __init__.py
│   └── sms_provider.py         # Twilio integration
│
├── reports/                    # Report Generation
│   ├── __init__.py
│   ├── pdf_generator.py
│   └── csv_exporter.py
│
├── utils/                      # Utilities
│   ├── __init__.py
│   ├── db_connection.py        # MongoDB connection
│   ├── validators.py           # Input validation
│   └── date_utils.py           # Date formatting helpers
│
└── tests/                      # Unit and Integration Tests
    ├── __init__.py
    ├── test_income_api.py
    ├── test_expense_api.py
    ├── test_ml_service.py
    ├── test_analytics_service.py
    └── test_financial_health.py
```

### Frontend Module Structure

```
frontend/
├── package.json
├── tailwind.config.js
├── vite.config.js              # Using Vite for faster builds
│
├── public/
│   └── index.html
│
└── src/
    ├── App.jsx                 # Main app component
    ├── main.jsx                # Entry point
    ├── index.css               # Tailwind imports
    │
    ├── api/                    # API Client
    │   ├── client.js           # Axios instance
    │   ├── incomeApi.js
    │   ├── expenseApi.js
    │   ├── mlApi.js
    │   ├── analyticsApi.js
    │   └── reportApi.js
    │
    ├── pages/                  # Main Pages
    │   ├── Dashboard.jsx
    │   ├── IncomeManager.jsx
    │   ├── ExpenseManager.jsx
    │   ├── MLInsights.jsx
    │   ├── Analytics.jsx
    │   ├── Reports.jsx
    │   └── Settings.jsx
    │
    ├── components/             # Reusable Components
    │   ├── common/
    │   │   ├── Button.jsx
    │   │   ├── Input.jsx
    │   │   ├── Modal.jsx
    │   │   ├── Loading.jsx
    │   │   └── ErrorMessage.jsx
    │   ├── charts/
    │   │   ├── LineChart.jsx
    │   │   ├── BarChart.jsx
    │   │   ├── PieChart.jsx
    │   │   └── AreaChart.jsx
    │   ├── income/
    │   │   ├── IncomeForm.jsx
    │   │   └── IncomeTable.jsx
    │   ├── expense/
    │   │   ├── ExpenseForm.jsx
    │   │   └── ExpenseTable.jsx
    │   └── insights/
    │       ├── FinancialHealthCard.jsx
    │       ├── BudgetRecommendation.jsx
    │       └── InvestmentPlan.jsx
    │
    ├── context/                # React Context
    │   └── AppContext.jsx      # Global state
    │
    └── utils/                  # Frontend Utilities
        ├── formatters.js       # Currency, date formatting
        └── validators.js       # Form validation
```

---

## Data Flow

### 1. Income/Expense CRUD Flow
```
User Input → React Form → API Client → Flask Route → Service Layer → 
MongoDB (via PyMongo) → Response → Update React State → Re-render UI
```

### 2. ML Prediction Flow
```
User requests prediction → Flask ML Route → ML Service loads model → 
Apply preprocessing → Model.predict() → Validate output → 
Store result in MongoDB → Return to frontend → Display insight card
```

### 3. Analytics Flow
```
User requests analysis → Flask Analytics Route → Analytics Service → 
Prepare data → Execute Python analytics module → 
Parse output (charts, metrics) → Store results → 
Return to frontend → Display charts and metrics
```
Return to frontend → Display charts and metrics
```

### 4. Alert Flow
```
Expense created/updated → Service checks thresholds → 
If threshold exceeded → Alert Service → Twilio SMS API → 
Log alert in MongoDB → Return status
```

---

## Database Schema Design

### Income Collection
```javascript
{
  _id: ObjectId,
  amount: Number,           // Required, positive
  source: String,           // Required (e.g., "Salary", "Freelance")
  date: ISODate,           // Required
  description: String,      // Optional
  category: String,         // e.g., "Primary", "Secondary"
  created_at: ISODate,
  updated_at: ISODate
}
// Indexes: { date: -1 }, { source: 1, date: -1 }
```

### Expenses Collection
```javascript
{
  _id: ObjectId,
  amount: Number,           // Required, positive
  category: String,         // Required (Food, Transport, Entertainment, etc.)
  description: String,      // Required (used for ML categorization)
  date: ISODate,           // Required
  payment_method: String,   // Optional (Cash, Card, UPI)
  is_anomaly: Boolean,      // Set by Isolation Forest
  predicted_category: String, // Set by Naive Bayes
  created_at: ISODate,
  updated_at: ISODate
}
// Indexes: { date: -1 }, { category: 1, date: -1 }
```

### Budgets Collection
```javascript
{
  _id: ObjectId,
  month: String,            // "2024-01"
  category: String,
  budget_amount: Number,
  spent_amount: Number,
  recommended_budget: Number, // From ML/rule-based system
  created_at: ISODate,
  updated_at: ISODate
}
// Indexes: { month: -1, category: 1 }
```

### ML Models Collection
```javascript
{
  _id: ObjectId,
  model_name: String,       // "categorizer", "predictor", "anomaly_detector"
  model_path: String,       // File path to .pkl
  training_date: ISODate,
  accuracy: Number,         // Actual measured accuracy
  training_samples: Number,
  features: Array,
  metadata: Object
}
```

### Alerts Collection
```javascript
{
  _id: ObjectId,
  alert_type: String,       // "budget_overrun", "anomaly", "low_savings"
  message: String,
  severity: String,         // "low", "medium", "high"
  triggered_at: ISODate,
  sms_sent: Boolean,
  sms_status: String,
  related_expense_id: ObjectId // Optional reference
}
```

---

## Machine Learning Design

### 1. Expense Categorization (Naive Bayes)
- **Input:** Expense description text
- **Output:** Predicted category (Food, Transport, etc.)
- **Algorithm:** MultinomialNB with TF-IDF vectorization
- **Training:** Requires at least 50 labeled expenses across categories
- **Validation:** Train/test split, report accuracy
- **Limitations:** Performance degrades with very short descriptions or unseen vocabulary

### 2. Expense Prediction (Linear Regression)
- **Input:** Historical expenses by category, month, trends
- **Output:** Predicted expense for next period
- **Features:** Month number, category encoded, rolling averages, trend
- **Validation:** Mean Absolute Error (MAE), R² score
- **Limitations:** Assumes linear patterns, poor with sparse data

### 3. Anomaly Detection (Isolation Forest)
- **Input:** Expense amount, category, day of week, time features
- **Output:** Binary flag (normal/anomaly)
- **Algorithm:** Isolation Forest (unsupervised)
- **Threshold:** Configurable contamination parameter
- **Use Case:** Flag unusually high expenses for review
- **Limitations:** High false-positive rate with irregular but legitimate spending

### 4. Budget Recommendations (Rule-Based + ML-Informed)
- Inputs: Total income, historical spending by category, savings goal percentage
- Rules:
  - Essential categories (Food, Housing): 50% of income
  - Discretionary (Entertainment, Shopping): 30% of income
  - Savings: 20% of income (50-30-20 rule)
- Adjustments based on actual spending patterns
- Transparency: Show calculation steps to user

### 5. Investment Planner (Educational Rule-Based)
- **NOT financial advice**
- Inputs: Risk tolerance (conservative/moderate/aggressive), time horizon, financial goals
- Output: Illustrative allocation percentages (e.g., 60% equities, 30% bonds, 10% cash)
- Disclaimer: Educational purposes only, consult certified financial advisor
- Rules based on standard age-based/risk-based allocation guidelines

---

## Python Analytics Design

### Integration Strategy

**Native Python Implementation:**
- Direct Python module integration
- Uses NumPy, SciPy, and pandas for computations
- No external dependencies required
- Optimized numerical computations

**Benefits:**
- Seamless integration with Flask backend
- No additional software installation required
- Full control over implementation
- Consistent development environment

### Analytics Modules

#### 1. `trend_analysis.py`
- **Input:** Date array, amount array, category labels
- **Computations:**
  - Moving averages (7-day, 30-day) using NumPy
  - Trend line (linear fit) using SciPy
  - Month-over-month growth rate
- **Output:** Trend data, coefficients, chart data

#### 2. `risk_analysis.py`
- **Input:** Expense amounts, income amounts
- **Computations:**
  - Standard deviation using NumPy
  - Coefficient of Variation (CV)
  - Expense-to-income ratio
  - Risk score (0-100 scale)
- **Output:** Risk metrics, variability data

#### 3. `investment_planner.py`
- **Input:** Risk tolerance, time horizon, current age, target retirement age
- **Computations:**
  - Age-based equity allocation: `equity% = 110 - age`
  - Risk-adjusted allocation
  - Diversification recommendations
- **Output:** Allocation percentages, distribution data

#### 4. `financial_metrics.py`
- **Input:** Income, expenses, savings, debts
- **Computations:**
  - Savings rate: `(income - expenses) / income * 100`
  - Debt-to-income ratio
  - Emergency fund sufficiency (months of expenses covered)
  - Financial health score components
- **Output:** Metrics dictionary, summary report

---

## Financial Health Score Calculation

**Transparent, Rule-Based Scoring (0-100 scale)**

Components (each 0-100, weighted):
1. **Savings Rate (30% weight)**
   - ≥20% income saved: 100 points
   - 10-20%: 50-100 points (linear)
   - <10%: 0-50 points

2. **Budget Adherence (25% weight)**
   - Average category spending vs. budget
   - Within budget: 100 points
   - Up to 10% over: 70 points
   - >20% over: 0 points

3. **Debt-to-Income Ratio (20% weight)**
   - No debt: 100 points
   - <30% income: 70 points
   - >50% income: 0 points

4. **Emergency Fund (15% weight)**
   - ≥6 months expenses: 100 points
   - 3-6 months: 50-100 points
   - <3 months: 0-50 points

5. **Spending Consistency (10% weight)**
   - Low variance in monthly expenses: 100 points
   - High volatility: lower score

**Formula:**
```
Health Score = 0.30 * Savings + 0.25 * Budget + 0.20 * Debt + 
               0.15 * Emergency + 0.10 * Consistency
```

**Interpretation:**
- 80-100: Excellent financial health
- 60-79: Good, minor improvements possible
- 40-59: Fair, needs attention
- <40: Poor, significant changes needed

---

## Alert System Design

### Trigger Conditions

1. **Budget Overrun Alert**
   - Trigger: Category spending exceeds budget by configurable % (default 90%)
   - Message: "⚠️ You've spent 95% of your Food budget this month"

2. **Anomaly Alert**
   - Trigger: Isolation Forest flags expense as anomaly
   - Message: "🚨 Unusual expense detected: ₹5000 in Entertainment"

3. **Low Savings Alert**
   - Trigger: Month-end savings below target threshold
   - Message: "📉 Savings this month: ₹2000 (Target: ₹5000)"

4. **High Daily Spending Alert**
   - Trigger: Daily total exceeds configurable limit
   - Message: "💸 High spending today: ₹3500"

### Configuration (stored in MongoDB settings collection)
```javascript
{
  user_settings: {
    alerts_enabled: true,
    phone_number: "+919876543210",
    thresholds: {
      budget_warning_percent: 90,
      daily_spending_limit: 2000,
      savings_target_monthly: 5000,
      anomaly_sensitivity: 0.1
    }
  }
}
```

---

## Optional: RAG Knowledge Assistant

**Purpose:** Answer financial literacy questions using trusted document collection

**Architecture:**
1. **Document Collection:** PDFs on budgeting, investing, tax planning, debt management
2. **Embedding:** sentence-transformers (all-MiniLM-L6-v2)
3. **Vector Store:** FAISS index
4. **Retrieval:** Top-K similar chunks for user query
5. **Generation:** LLM synthesizes answer from retrieved context

**Setup:**
- Place PDFs in `backend/rag/documents/`
- Run embedding script to create FAISS index
- Configure OpenAI/Ollama API key in `.env`

**Isolation:**
- Separate Flask route: `/api/rag/ask`
- Separate service module
- Graceful degradation if LLM API unavailable

**Limitations:**
- Answers quality depends on document collection
- Not a substitute for professional financial advice
- May hallucinate if context insufficient

---

## Testing Strategy

### Unit Tests (pytest)
- `test_income_service.py`: CRUD operations, validation
- `test_expense_service.py`: CRUD, filtering, aggregation
- `test_ml_service.py`: Model loading, prediction logic
- `test_financial_health_service.py`: Score calculation with known inputs
- `test_validators.py`: Input validation edge cases

### Integration Tests
- `test_income_api.py`: Full request-response cycle with test MongoDB
- `test_ml_integration.py`: Train model → save → load → predict
- `test_analytics_integration.py`: Execute analytics → parse output

### Manual Testing Checklist
- [ ] Create income, verify in MongoDB
- [ ] Create expenses, verify categorization
- [ ] Train ML models with synthetic data, verify saved
- [ ] Generate PDF report, verify contents
- [ ] Execute Python analytics, verify results generated
- [ ] Trigger alert, verify SMS sent (test mode)
- [ ] Dashboard charts render with real data
- [ ] Filter expenses by date range, category

---

## Environment Variables

`.env` file structure:

```ini
# Flask
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-change-in-production

# MongoDB
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB_NAME=finance_advisor

# MATLAB
MATLAB_AVAILABLE=true
MATLAB_ENGINE_MODE=engine  # or "batch"
MATLAB_PATH=/path/to/matlab/bin/matlab

# Twilio SMS
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
USER_PHONE_NUMBER=+919876543210
SMS_ENABLED=true

# Optional: RAG Assistant
RAG_ENABLED=false
OPENAI_API_KEY=sk-...
RAG_MODEL=gpt-3.5-turbo
RAG_TEMPERATURE=0.7

# ML Settings
ML_TRAINING_MIN_SAMPLES=50
ML_MODEL_DIR=./ml/saved_models/

# Reports
REPORTS_OUTPUT_DIR=./reports/output/
```

---

## Known Limitations and Scope

### What this project IS:
- ✅ Comprehensive demonstration of ML + MATLAB + full-stack integration
- ✅ Educational tool for understanding personal finance analytics
- ✅ Portfolio-worthy college project
- ✅ Locally runnable single-user application

### What this project IS NOT:
- ❌ Production-ready multi-user SaaS
- ❌ Secure enough for real financial data (no auth, no encryption at rest)
- ❌ Financial advice (all recommendations are illustrative)
- ❌ Guaranteed-accurate predictions (ML has inherent uncertainty)
- ❌ Real-time stock trading or portfolio management

### ML Limitations:
- Requires minimum training data (50+ samples recommended)
- Accuracy depends on data quality and diversity
- Models are illustrative, not production-grade
- No online learning (requires manual retraining)

### Data Limitations:
- Single-user (no multi-tenancy)
- No data backup/restore built-in
- No audit trail or versioning
- Currency assumed to be INR (₹)

---

## Viva Defense Preparation

### Expected Questions and Answers

**Q1: Why did you choose Naive Bayes for categorization?**
- A: Naive Bayes works well with text data (expense descriptions), is fast to train, and performs reasonably well even with small datasets. It's interpretable and suitable for multi-class classification with relatively independent features.

**Q2: How does Python analytics work?**
- A: The analytics modules use NumPy for array operations and numerical computations, SciPy for advanced statistical functions like linear regression, and pandas for data manipulation. All computations are done natively in Python without external dependencies, providing seamless integration with the Flask backend.

**Q3: What happens if ML models have insufficient training data?**
- A: The system checks sample count before training. If below threshold (50 samples), it returns an error message to the user explaining that more data is needed. The app continues to function using manual categorization until sufficient data is collected.

**Q4: How is Financial Health Score calculated?**
- A: It's a weighted combination of five components: savings rate (30%), budget adherence (25%), debt-to-income (20%), emergency fund (15%), and spending consistency (10%). Each component is scored 0-100 using transparent rules, then weighted to produce final score.

**Q5: Is this secure enough for real user data?**
- A: No. This is a demonstration project without authentication, authorization, or encryption. It's designed for local single-user use. For production, we'd need JWT auth, HTTPS, encrypted database fields, and comprehensive security audit.

**Q6: Why use Python analytics instead of MATLAB?**
- A: Python analytics provide native integration with the Flask backend, eliminate external dependencies, use widely-available open-source libraries (NumPy, SciPy), and maintain all analytical capabilities while simplifying deployment and maintenance.

**Q7: Why MongoDB instead of SQL?**
- A: MongoDB's flexible schema suits the varying structure of financial transactions and ML results. It handles JSON-like documents naturally, which aligns well with REST API responses. For this project scale, either would work, but MongoDB provides easier prototyping.

**Q8: How accurate are the expense predictions?**
- A: Accuracy varies with data. Linear Regression works well for stable spending patterns but struggles with high variability. We measure and report MAE and R² score. Typical R² might be 0.6-0.8 with good data. We document these limitations clearly.

**Q9: Can users customize budget categories?**
- A: In the current version, categories are predefined (Food, Transport, etc.) for consistency with ML models. Future enhancement could allow custom categories with retraining capability.

**Q10: What's the difference between your ML predictions and Python analytics?**
- A: ML focuses on classification and prediction tasks (categorize expenses, predict future spending, detect anomalies) using machine learning algorithms. Python analytics provides statistical and financial computations (trend analysis, risk metrics, investment allocation calculations, advanced numerical analysis). They complement each other.

---

## Success Criteria

### Must Have (MVP)
- ✅ Income CRUD with MongoDB persistence
- ✅ Expense CRUD with MongoDB persistence
- ✅ At least one trained ML model (categorization)
- ✅ At least one Python analytics module (spending trends)
- ✅ Financial Health Score calculation
- ✅ React dashboard with charts
- ✅ PDF report generation
- ✅ Basic error handling and validation

### Should Have
- ✅ All three ML models (categorization, prediction, anomaly)
- ✅ All four Python analytics modules
- ✅ SMS alerts (with test mode)
- ✅ Budget recommendations
- ✅ Investment planner
- ✅ CSV export
- ✅ Comprehensive testing
- ✅ Complete documentation

### Could Have (Nice to Have)
- ✅ RAG knowledge assistant
- ⭕ User settings/preferences page
- ⭕ Data import from bank statements
- ⭕ Multi-currency support
- ⭕ Mobile-responsive design optimization

---

## Next Steps

After architecture approval, development will proceed in this order:

1. **Phase 1: Foundation** (Setup + Database)
   - Project structure creation
   - Dependency installation
   - MongoDB connection and schemas
   - Environment configuration

2. **Phase 2: Core CRUD** (Income + Expenses)
   - Backend models, services, routes
   - Frontend forms, tables, API client
   - Basic validation and error handling

3. **Phase 3: Machine Learning** (Models + Training)
   - ML service implementation
   - Model training scripts
   - Prediction endpoints

4. **Phase 4: Python Analytics** (Analytics Engine)
   - Python analytics modules
   - Analytics service integration
   - Analytics endpoints

5. **Phase 5: Intelligence Layer** (Health Score + Recommendations)
   - Financial health calculation
   - Budget recommendations
   - Investment planner

6. **Phase 6: Alerts & Reports** (Notifications + PDF/CSV)
   - Alert system
   - SMS integration
   - Report generation

7. **Phase 7: Dashboard & UI Polish** (Charts + UX)
   - Dashboard implementation
   - Charts integration
   - Loading states, error handling

8. **Phase 8: Testing & Documentation** (Quality Assurance)
   - Unit and integration tests
   - README and setup guides
   - Viva preparation materials

9. **Phase 9 (Optional): RAG Assistant**
   - Document processing
   - Embedding and retrieval
   - LLM integration

---

## References and Resources

### Documentation
- Flask: https://flask.palletsprojects.com/
- React: https://react.dev/
- MongoDB: https://www.mongodb.com/docs/
- scikit-learn: https://scikit-learn.org/
- NumPy: https://numpy.org/doc/
- SciPy: https://docs.scipy.org/
- Twilio SMS: https://www.twilio.com/docs/sms

### Financial Education
- 50-30-20 Budgeting Rule
- Age-based investment allocation principles
- Financial health metrics (industry standard ratios)

### Academic Context
- This is an educational project for demonstration purposes
- All ML algorithms and financial calculations are transparent and explainable
- No proprietary or black-box systems
- Suitable for academic viva and evaluation

---

**Document Version:** 1.0  
**Last Updated:** 2026-10-09  
**Status:** Ready for Review and Implementation
