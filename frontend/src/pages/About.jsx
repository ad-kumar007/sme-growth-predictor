import React from 'react';

function About() {
  return (
    <div className="max-w-4xl mx-auto space-y-8">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-xl p-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">About This Project</h1>
        <p className="text-xl text-gray-600">
          An AI-powered solution for predicting SME growth potential using machine learning
        </p>
      </div>

      {/* Dataset Information */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">📊 Dataset Overview</h2>
        <div className="space-y-4 text-gray-700">
          <p>
            The model is trained on real SME (Small and Medium Enterprise) data containing
            comprehensive business metrics and operational indicators.
          </p>
          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-2">Dataset Size</h3>
              <p className="text-sm">101 SME records (80 training, 21 testing)</p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-2">Target Classes</h3>
              <p className="text-sm">High, Medium, Low growth categories</p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-2">Features</h3>
              <p className="text-sm">12 key business and operational metrics</p>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-2">Data Quality</h3>
              <p className="text-sm">Leakage-free, properly preprocessed</p>
            </div>
          </div>
        </div>
      </div>

      {/* Model Information */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">🤖 Machine Learning Model</h2>
        <div className="space-y-4 text-gray-700">
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Algorithm</h3>
            <p>Random Forest Classifier with optimized hyperparameters</p>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Key Features</h3>
            <ul className="list-disc list-inside space-y-1 text-sm ml-4">
              <li>Data leakage detection and removal (3 columns removed)</li>
              <li>Mutual Information-based feature selection (top 10 features)</li>
              <li>Class-balanced training to handle imbalanced data</li>
              <li>5-fold stratified cross-validation</li>
              <li>Hyperparameter tuning via RandomizedSearchCV</li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Model Constraints</h3>
            <ul className="list-disc list-inside space-y-1 text-sm ml-4">
              <li>Max depth: 8-16 (prevents overfitting)</li>
              <li>Min samples per leaf: 3-7</li>
              <li>Min samples per split: 5-15</li>
              <li>Number of estimators: 100-300</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Performance Metrics */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">📈 Model Performance</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <h3 className="font-semibold text-gray-900 mb-3">Test Set Metrics</h3>
            <div className="space-y-2">
              <div className="flex justify-between items-center p-3 bg-green-50 rounded">
                <span className="text-sm font-medium">Accuracy</span>
                <span className="text-lg font-bold text-green-600">81%</span>
              </div>
              <div className="flex justify-between items-center p-3 bg-blue-50 rounded">
                <span className="text-sm font-medium">Precision (Macro)</span>
                <span className="text-lg font-bold text-blue-600">0.47</span>
              </div>
              <div className="flex justify-between items-center p-3 bg-purple-50 rounded">
                <span className="text-sm font-medium">Recall (Macro)</span>
                <span className="text-lg font-bold text-purple-600">0.50</span>
              </div>
              <div className="flex justify-between items-center p-3 bg-indigo-50 rounded">
                <span className="text-sm font-medium">F1 Score (Macro)</span>
                <span className="text-lg font-bold text-indigo-600">0.76</span>
              </div>
            </div>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-3">Overfitting Control</h3>
            <div className="space-y-2">
              <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
                <span className="text-sm font-medium">Train Accuracy</span>
                <span className="text-lg font-bold text-gray-700">96%</span>
              </div>
              <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
                <span className="text-sm font-medium">Test Accuracy</span>
                <span className="text-lg font-bold text-gray-700">81%</span>
              </div>
              <div className="flex justify-between items-center p-3 bg-yellow-50 rounded">
                <span className="text-sm font-medium">Train-Test Gap</span>
                <span className="text-lg font-bold text-yellow-600">15%</span>
              </div>
              <p className="text-xs text-gray-600 mt-2">
                ✓ Gap reduced by 55% compared to baseline overfitted model
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Technical Stack */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">🛠️ Technology Stack</h2>
        <div className="grid md:grid-cols-3 gap-6">
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Frontend</h3>
            <ul className="text-sm text-gray-700 space-y-1">
              <li>• React 18</li>
              <li>• Tailwind CSS</li>
              <li>• React Router</li>
              <li>• Recharts</li>
              <li>• Axios</li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">Backend</h3>
            <ul className="text-sm text-gray-700 space-y-1">
              <li>• FastAPI</li>
              <li>• Python 3.12</li>
              <li>• Uvicorn</li>
              <li>• Pydantic</li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-gray-900 mb-2">ML/Data</h3>
            <ul className="text-sm text-gray-700 space-y-1">
              <li>• scikit-learn</li>
              <li>• pandas</li>
              <li>• NumPy</li>
              <li>• Random Forest</li>
            </ul>
          </div>
        </div>
      </div>

      {/* How to Use */}
      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg shadow-xl p-8 text-white">
        <h2 className="text-2xl font-bold mb-4">🚀 How to Use</h2>
        <ol className="space-y-3">
          <li className="flex items-start">
            <span className="font-bold mr-3">1.</span>
            <span>Navigate to the Prediction Form page</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold mr-3">2.</span>
            <span>Fill in all 12 required business metrics for your SME</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold mr-3">3.</span>
            <span>Click "Predict Growth Category" to submit</span>
          </li>
          <li className="flex items-start">
            <span className="font-bold mr-3">4.</span>
            <span>View your prediction with detailed confidence scores and visual charts</span>
          </li>
        </ol>
      </div>
    </div>
  );
}

export default About;
