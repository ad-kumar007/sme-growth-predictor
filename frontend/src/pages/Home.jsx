import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="bg-white rounded-lg shadow-xl p-8 md:p-12">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Predict Your SME's Growth Potential
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Leverage advanced machine learning to forecast your small and medium enterprise's
            growth category based on key business indicators and operational metrics.
          </p>
          <Link
            to="/predict"
            className="inline-block bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition shadow-lg hover:shadow-xl"
          >
            Start Prediction →
          </Link>
        </div>
      </div>

      {/* Features Grid */}
      <div className="grid md:grid-cols-3 gap-6">
        <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
          <div className="text-4xl mb-4">🎯</div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Accurate Predictions</h3>
          <p className="text-gray-600">
            Our ML model analyzes 12 key features to provide reliable growth category predictions
            with confidence scores.
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
          <div className="text-4xl mb-4">⚡</div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Instant Results</h3>
          <p className="text-gray-600">
            Get immediate predictions with detailed confidence breakdowns for High, Medium, and Low
            growth categories.
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition">
          <div className="text-4xl mb-4">📊</div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Data-Driven Insights</h3>
          <p className="text-gray-600">
            Built on real SME data with advanced preprocessing and feature selection for optimal
            performance.
          </p>
        </div>
      </div>

      {/* How It Works */}
      <div className="bg-white rounded-lg shadow-md p-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-6 text-center">How It Works</h2>
        <div className="grid md:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-blue-600">1</span>
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">Fill the Form</h4>
            <p className="text-sm text-gray-600">
              Enter your SME's operational and business metrics
            </p>
          </div>

          <div className="text-center">
            <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-blue-600">2</span>
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">Submit Data</h4>
            <p className="text-sm text-gray-600">
              Our backend processes and validates your input
            </p>
          </div>

          <div className="text-center">
            <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-blue-600">3</span>
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">ML Prediction</h4>
            <p className="text-sm text-gray-600">
              Advanced model analyzes your data instantly
            </p>
          </div>

          <div className="text-center">
            <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-blue-600">4</span>
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">View Results</h4>
            <p className="text-sm text-gray-600">
              Get prediction with confidence scores
            </p>
          </div>
        </div>
      </div>

      {/* Stats */}
      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg shadow-xl p-8 text-white">
        <div className="grid md:grid-cols-3 gap-6 text-center">
          <div>
            <div className="text-4xl font-bold mb-2">81%</div>
            <div className="text-blue-100">Test Accuracy</div>
          </div>
          <div>
            <div className="text-4xl font-bold mb-2">0.76</div>
            <div className="text-blue-100">F1 Score (Macro)</div>
          </div>
          <div>
            <div className="text-4xl font-bold mb-2">12</div>
            <div className="text-blue-100">Key Features</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
