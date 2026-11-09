/**
 * Main App component with routing and layout.
 */

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { AppProvider } from './context/AppContext'

// Pages (will be created in Phase 2-7)
// import Dashboard from './pages/Dashboard'
// import IncomeManager from './pages/IncomeManager'
// import ExpenseManager from './pages/ExpenseManager'
// import MLInsights from './pages/MLInsights'
// import Analytics from './pages/Analytics'
// import Reports from './pages/Reports'
// import Settings from './pages/Settings'

// Temporary home page for Phase 1
function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-2xl w-full">
        <div className="text-center">
          <div className="flex justify-center mb-6">
            <div className="bg-blue-600 text-white p-4 rounded-full">
              <svg className="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
          </div>
          
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            FinCore Analytics
          </h1>
          
          <p className="text-xl text-blue-600 font-semibold mb-6">
            AI-Based Personal Finance Advisor
          </p>
          
          <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-6">
            <div className="flex items-center justify-center">
              <svg className="w-6 h-6 text-green-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span className="text-green-800 font-semibold">Phase 1 Complete: Foundation Setup</span>
            </div>
          </div>
          
          <div className="text-left bg-gray-50 rounded-lg p-6 mb-6">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Current Status:</h2>
            <ul className="space-y-2 text-gray-700">
              <li className="flex items-center">
                <span className="text-green-500 mr-2">✓</span>
                Backend Flask server configured
              </li>
              <li className="flex items-center">
                <span className="text-green-500 mr-2">✓</span>
                Frontend React application initialized
              </li>
              <li className="flex items-center">
                <span className="text-green-500 mr-2">✓</span>
                MongoDB connection ready
              </li>
              <li className="flex items-center">
                <span className="text-green-500 mr-2">✓</span>
                Project structure established
              </li>
            </ul>
          </div>
          
          <div className="text-sm text-gray-600 space-y-2">
            <p className="font-semibold">Features Coming Soon:</p>
            <div className="grid grid-cols-2 gap-2 text-left">
              <div className="bg-white p-3 rounded border">
                <span className="text-blue-600">📊</span> Dashboard & Analytics
              </div>
              <div className="bg-white p-3 rounded border">
                <span className="text-green-600">💰</span> Income & Expense Management
              </div>
              <div className="bg-white p-3 rounded border">
                <span className="text-purple-600">🤖</span> ML Predictions
              </div>
              <div className="bg-white p-3 rounded border">
                <span className="text-red-600">📐</span> Python Analytics
              </div>
            </div>
          </div>
          
          <p className="mt-6 text-gray-500 text-sm">
            College Final Year Project | AI & ML Integration
          </p>
        </div>
      </div>
    </div>
  )
}

function App() {
  return (
    <AppProvider>
      <Router>
        <div className="app">
          <Routes>
            <Route path="/" element={<HomePage />} />
            {/* Phase 2-7 routes will be added here:
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/income" element={<IncomeManager />} />
            <Route path="/expenses" element={<ExpenseManager />} />
            <Route path="/ml-insights" element={<MLInsights />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/settings" element={<Settings />} />
            */}
          </Routes>
        </div>
      </Router>
    </AppProvider>
  )
}

export default App
