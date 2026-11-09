# Module Dependencies & Implementation Order

## Dependency Graph

This document shows how modules depend on each other, helping you understand the implementation order.

---

## Backend Module Dependencies

```
┌─────────────────────────────────────────────────────────────────┐
│                         PHASE 1: FOUNDATION                     │
│                                                                 │
│  config.py ──→ .env                                           │
│       │                                                         │
│       ├──→ utils/db_connection.py ──→ MongoDB                 │
│       │                                                         │
│       └──→ app.py (Flask initialization)                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      PHASE 2: CORE CRUD                         │
│                                                                 │
│  models/income_model.py ──→ utils/validators.py               │
│           │                        │                            │
│           ├──→ services/income_service.py ──→ db_connection   │
│           │            │                                        │
│           │            └──→ api/income_routes.py ──→ app.py   │
│           │                                                     │
│  models/expense_model.py ──→ utils/validators.py              │
│           │                        │                            │
│           └──→ services/expense_service.py ──→ db_connection  │
│                        │                                        │
│                        └──→ api/expense_routes.py ──→ app.py  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 3: MACHINE LEARNING                     │
│                                                                 │
│  services/expense_service.py (provides data)                   │
│           │                                                     │
│           ├──→ ml/categorizer.py                              │
│           │         │                                           │
│           ├──→ ml/predictor.py                                │
│           │         │                                           │
│           ├──→ ml/anomaly_detector.py                         │
│           │         │                                           │
│           │    (All save to ml/saved_models/)                  │
│           │                                                     │
│           └──→ ml/trainer.py (orchestrates training)          │
│                   │                                             │
│                   └──→ services/ml_service.py                 │
│                           │                                     │
│                           └──→ api/ml_routes.py ──→ app.py    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 4: MATLAB ANALYTICS                    │
│                                                                 │
│  services/expense_service.py (provides data)                   │
│  services/income_service.py (provides data)                    │
│           │                                                     │
│           ├──→ matlab/scripts/*.m (MATLAB files)              │
│           │         │                                           │
│           └──→ matlab/matlab_engine.py (Engine API)           │
│                   │      OR                                     │
│                   └──→ matlab/matlab_adapter.py (Batch mode)  │
│                           │                                     │
│                           └──→ services/matlab_service.py      │
│                                   │                             │
│                                   └──→ api/matlab_routes.py ──→ app.py │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                PHASE 5: INTELLIGENCE LAYER                      │
│                                                                 │
│  services/income_service.py                                    │
│  services/expense_service.py                                   │
│  models/budget_model.py                                        │
│           │                                                     │
│           ├──→ services/financial_health_service.py           │
│           │         │                                           │
│           ├──→ services/budget_service.py                     │
│           │         │                                           │
│           └──→ services/investment_planner.py                 │
│                     │                                           │
│                     └──→ api routes (financial health,         │
│                           budgets, investment)                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 6: ALERTS & REPORTS                      │
│                                                                 │
│  config.py (Twilio credentials)                                │
│       │                                                         │
│       └──→ notifications/sms_provider.py                       │
│                   │                                             │
│  services/expense_service.py                                   │
│  services/budget_service.py                                    │
│           │                                                     │
│           └──→ services/alert_service.py ──→ sms_provider     │
│                       │                                         │
│                       └──→ api/alert_routes.py ──→ app.py     │
│                                                                 │
│  services/income_service.py                                    │
│  services/expense_service.py                                   │
│  services/financial_health_service.py                          │
│           │                                                     │
│           ├──→ reports/pdf_generator.py                       │
│           │                                                     │
│           └──→ reports/csv_exporter.py                        │
│                       │                                         │
│                       └──→ api/report_routes.py ──→ app.py    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Frontend Module Dependencies

```
┌─────────────────────────────────────────────────────────────────┐
│                         FOUNDATION                              │
│                                                                 │
│  main.jsx ──→ App.jsx ──→ React Router                        │
│                   │                                             │
│                   └──→ context/AppContext.jsx                  │
│                                                                 │
│  api/client.js (Axios base configuration)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                      COMMON COMPONENTS                          │
│                                                                 │
│  components/common/                                            │
│       ├── Button.jsx                                           │
│       ├── Input.jsx                                            │
│       ├── Modal.jsx                                            │
│       ├── Loading.jsx                                          │
│       └── ErrorMessage.jsx                                     │
│                                                                 │
│  utils/                                                         │
│       ├── formatters.js (currency, date formatting)           │
│       └── validators.js (form validation)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                         API CLIENTS                             │
│                                                                 │
│  api/client.js                                                 │
│       │                                                         │
│       ├──→ api/incomeApi.js                                   │
│       ├──→ api/expenseApi.js                                  │
│       ├──→ api/mlApi.js                                       │
│       ├──→ api/matlabApi.js                                   │
│       ├──→ api/reportApi.js                                   │
│       └──→ api/ragApi.js                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FEATURE COMPONENTS                           │
│                                                                 │
│  components/income/                                            │
│       ├── IncomeForm.jsx ──→ incomeApi.js, validators        │
│       └── IncomeTable.jsx ──→ incomeApi.js, formatters       │
│                                                                 │
│  components/expense/                                           │
│       ├── ExpenseForm.jsx ──→ expenseApi.js, validators      │
│       └── ExpenseTable.jsx ──→ expenseApi.js, formatters     │
│                                                                 │
│  components/charts/                                            │
│       ├── LineChart.jsx ──→ Recharts                          │
│       ├── BarChart.jsx ──→ Recharts                           │
│       ├── PieChart.jsx ──→ Recharts                           │
│       └── AreaChart.jsx ──→ Recharts                          │
│                                                                 │
│  components/insights/                                          │
│       ├── FinancialHealthCard.jsx ──→ charts, formatters     │
│       ├── BudgetRecommendation.jsx ──→ charts, formatters    │
│       └── InvestmentPlan.jsx ──→ charts, matlabApi           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                          PAGES                                  │
│                                                                 │
│  pages/Dashboard.jsx                                           │
│       ├── uses: expenseApi, incomeApi, charts                 │
│       └── displays: FinancialHealthCard, charts, summaries    │
│                                                                 │
│  pages/IncomeManager.jsx                                       │
│       └── uses: IncomeForm, IncomeTable                       │
│                                                                 │
│  pages/ExpenseManager.jsx                                      │
│       └── uses: ExpenseForm, ExpenseTable                     │
│                                                                 │
│  pages/MLInsights.jsx                                          │
│       └── uses: mlApi, charts, ModelCard                      │
│                                                                 │
│  pages/MatlabAnalytics.jsx                                     │
│       └── uses: matlabApi, charts                             │
│                                                                 │
│  pages/Reports.jsx                                             │
│       └── uses: reportApi                                     │
│                                                                 │
│  pages/Settings.jsx                                            │
│       └── uses: alert settings API                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Critical Dependencies by Phase

### Phase 1 Prerequisites (Must be installed first)
- Python 3.9+
- Node.js 16+
- MongoDB
- Git

### Phase 2 Dependencies
**Blocked until Phase 1 complete:**
- Flask server running
- MongoDB connected
- React dev server running

### Phase 3 Dependencies
**Blocked until Phase 2 complete:**
- Expense data available in MongoDB
- Expense service operational

**External:**
- scikit-learn
- pandas
- joblib

### Phase 4 Dependencies
**Blocked until Phase 2 complete:**
- Income/Expense data available

**External:**
- MATLAB installed (optional)
- MATLAB Engine for Python configured (optional)

### Phase 5 Dependencies
**Blocked until Phase 2 complete:**
- Income/Expense services
- Budget model

### Phase 6 Dependencies
**Blocked until Phase 2, 5 complete:**
- All data services
- Financial health service

**External:**
- Twilio account (optional)
- ReportLab (Python library)

### Phase 7 Dependencies
**Blocked until Phases 2-6 complete:**
- All API endpoints functional
- All backend services operational

**External:**
- Recharts
- React Router

### Phase 8 Dependencies
**Blocked until Phases 1-7 complete:**
- All features implemented
- All endpoints functional

**External:**
- pytest
- pytest-flask

### Phase 9 Dependencies (Optional)
**Independent, can be done anytime after Phase 1:**

**External:**
- sentence-transformers
- FAISS
- OpenAI API key or Ollama

---

## Parallel Development Opportunities

These modules can be developed in parallel if multiple people are working:

### Stream 1: Backend Core (Critical Path)
1. Phase 1: Foundation
2. Phase 2: Income/Expense CRUD
3. Phase 5: Financial Health

### Stream 2: Backend ML (Can start after Phase 2 data available)
1. Phase 3: ML models
2. Phase 3: ML training scripts
3. Phase 3: ML API endpoints

### Stream 3: Backend Analytics (Can start after Phase 2 data available)
1. Phase 4: Analytics scripts
2. Phase 4: Python analytics integration
3. Phase 4: Analytics API endpoints

### Stream 4: Backend Alerts & Reports (Can start after Phase 2, 5)
1. Phase 6: Alert system
2. Phase 6: Report generation

### Stream 5: Frontend (Can start after Phase 1 backend)
1. Phase 2: Income/Expense UI
2. Phase 7: Dashboard
3. Phase 7: ML Insights UI
4. Phase 7: MATLAB Analytics UI

### Stream 6: Optional Features (Independent)
1. Phase 9: RAG assistant

---

## Installation Order (Step-by-Step)

### 1. System Prerequisites (Do First)
```bash
# Check Python
python --version  # Should be 3.9+

# Check Node.js
node --version    # Should be 16+

# Check MongoDB
mongod --version

# Check MATLAB (optional)
matlab -batch "disp('MATLAB available')"
```

### 2. Python Backend Dependencies
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors pymongo python-dotenv
pip install pandas numpy scikit-learn joblib
pip install reportlab twilio
pip install pytest pytest-flask  # For testing

# Optional: MATLAB Engine
python -m matlab.engine.install

# Optional: RAG
pip install sentence-transformers faiss-cpu openai
```

### 3. Node.js Frontend Dependencies
```bash
cd frontend
npm install react react-dom react-router-dom
npm install axios
npm install recharts
npm install tailwindcss postcss autoprefixer
npm install -D vite @vitejs/plugin-react
```

### 4. MongoDB Setup
```bash
# Windows: Create data directory
mkdir C:\data\db

# Start MongoDB
mongod --dbpath C:\data\db

# In another terminal, verify connection
mongosh
# In mongosh:
show dbs
use finance_advisor
```

### 5. Environment Configuration
```bash
# Backend
cd backend
cp .env.example .env
# Edit .env with actual values

# Frontend
cd frontend
# Create .env if needed for API URL
```

---

## Verification Checklist

After each phase, verify these dependencies:

### After Phase 1
- [ ] Flask server starts: `python app.py` → "Running on http://127.0.0.1:5000"
- [ ] React dev server starts: `npm run dev` → "Local: http://localhost:5173"
- [ ] MongoDB connects: Test connection from Python
- [ ] MATLAB status known: Available or Not Available documented

### After Phase 2
- [ ] Create income via API → Appears in MongoDB
- [ ] Create expense via API → Appears in MongoDB
- [ ] Frontend forms work → Data appears in tables
- [ ] Filtering works → Correct data returned

### After Phase 3
- [ ] ML models train → .pkl files created in `ml/saved_models/`
- [ ] Models load on server restart → No errors
- [ ] Predictions work → Reasonable outputs

### After Phase 4
- [ ] MATLAB scripts execute → Results returned (or clear error if unavailable)
- [ ] Charts generate → PNG files created or data returned
- [ ] Frontend displays MATLAB results → Charts visible

### After Phase 5
- [ ] Health score calculates → Number between 0-100
- [ ] Budget recommendations → Reasonable percentages
- [ ] Investment allocations → Sum to 100%

### After Phase 6
- [ ] Test SMS sends → Message received (if Twilio configured)
- [ ] PDF generates → File downloads
- [ ] CSV exports → File contains data

### After Phase 7
- [ ] Dashboard loads → All charts render
- [ ] Navigation works → All pages accessible
- [ ] No console errors → Clean browser console

### After Phase 8
- [ ] Tests run → `pytest tests/ -v` passes
- [ ] README accurate → Setup instructions work
- [ ] Demo script → Can execute end-to-end

---

## Common Dependency Issues & Solutions

### Issue: MATLAB Engine not found
**Solution:**
```bash
# Install MATLAB Engine for Python
cd "C:\Program Files\MATLAB\R2023a\extern\engines\python"
python setup.py install

# Or use batch mode fallback (no installation needed)
# Set MATLAB_ENGINE_MODE=batch in .env
```

### Issue: MongoDB connection refused
**Solution:**
```bash
# Ensure MongoDB is running
mongod --dbpath C:\data\db

# Check port not in use
netstat -an | findstr "27017"

# Update connection string in .env if using Atlas
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/
```

### Issue: Twilio authentication failed
**Solution:**
```bash
# Verify credentials in .env
# Get from https://console.twilio.com/
TWILIO_ACCOUNT_SID=ACxxxxx...
TWILIO_AUTH_TOKEN=xxxxx...

# Or disable SMS
SMS_ENABLED=false
```

### Issue: Python package conflicts
**Solution:**
```bash
# Use fresh virtual environment
cd backend
rmdir /s venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: React/Node version mismatch
**Solution:**
```bash
# Update Node.js to LTS version
# Download from nodejs.org

# Clear npm cache
npm cache clean --force
cd frontend
rmdir /s node_modules
npm install
```

### Issue: CORS errors in browser
**Solution:**
```python
# Ensure Flask-CORS configured in app.py
from flask_cors import CORS
CORS(app, origins=["http://localhost:5173"])
```

---

## Integration Points Summary

### Backend to Frontend
- **Protocol:** REST API (JSON)
- **Base URL:** http://localhost:5000/api
- **Auth:** None (single-user demo)
- **Error Format:** `{ "error": "message", "code": 400 }`

### Backend to MongoDB
- **Driver:** PyMongo
- **Connection:** Via `utils/db_connection.py`
- **Validation:** MongoDB schema validation + Python validators

### Backend to MATLAB
- **Option 1:** MATLAB Engine for Python (direct function calls)
- **Option 2:** Batch mode (CSV files + command line)
- **Detection:** Automatic on server start

### Backend to Twilio
- **Protocol:** REST API
- **Library:** `twilio` Python package
- **Fallback:** Test mode if credentials missing

### Frontend to Backend
- **Library:** Axios
- **Base:** `api/client.js` configured instance
- **Interceptors:** Error handling, loading states

### ML to Database
- **Models:** Stored as `.pkl` files in `ml/saved_models/`
- **Metadata:** Stored in `ml_models` collection
- **Loading:** On server start + lazy loading

---

## Next Steps After Understanding Dependencies

1. **Print this document** for reference during implementation
2. **Install prerequisites** in order (Phase 1 checklist)
3. **Verify each installation** before proceeding
4. **Begin Phase 1** only after all prerequisites installed
5. **Follow verification checklist** after each phase

---

**Document Purpose:** Help student understand what depends on what, and in what order to implement modules.

**Key Takeaway:** Always complete dependencies before dependent modules. Test each layer before building on top of it.
