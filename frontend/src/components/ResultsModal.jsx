import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';

function ResultsModal({ result, onClose }) {
  const { prediction, confidence_scores } = result;

  // Prepare data for chart
  const chartData = Object.entries(confidence_scores).map(([category, score]) => ({
    category,
    confidence: (score * 100).toFixed(2),
    score: score,
  }));

  // Color mapping
  const colorMap = {
    High: '#10b981',
    Medium: '#f59e0b',
    Low: '#ef4444',
  };

  // Get prediction color
  const predictionColor = colorMap[prediction] || '#3b82f6';

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-2 sm:p-4">
      <div className="bg-white rounded-lg shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-6 rounded-t-lg">
          <div className="flex justify-between items-center">
            <h2 className="text-2xl font-bold text-white">Prediction Results</h2>
            <button
              onClick={onClose}
              className="text-white hover:text-gray-200 transition"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="p-4 sm:p-6 space-y-4 sm:space-y-6">
          {/* Prediction Badge */}
          <div className="text-center">
            <p className="text-sm sm:text-base text-gray-600 mb-2">Predicted Growth Category</p>
            <div
              className="inline-block px-6 sm:px-8 py-3 sm:py-4 rounded-lg text-white text-2xl sm:text-3xl font-bold shadow-lg"
              style={{ backgroundColor: predictionColor }}
            >
              {prediction}
            </div>
            <p className="text-xs sm:text-sm text-gray-500 mt-2">
              Confidence: {(confidence_scores[prediction] * 100).toFixed(2)}%
            </p>
          </div>

          {/* Confidence Scores */}
          <div>
            <h3 className="text-base sm:text-lg font-semibold text-gray-900 mb-3 sm:mb-4">Confidence Breakdown</h3>
            <div className="space-y-3">
              {Object.entries(confidence_scores)
                .sort((a, b) => b[1] - a[1])
                .map(([category, score]) => (
                  <div key={category}>
                    <div className="flex justify-between items-center mb-1">
                      <span className="text-sm font-medium text-gray-700">{category}</span>
                      <span className="text-sm font-semibold text-gray-900">
                        {(score * 100).toFixed(2)}%
                      </span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2 sm:h-3">
                      <div
                        className="h-2 sm:h-3 rounded-full transition-all duration-500"
                        style={{
                          width: `${score * 100}%`,
                          backgroundColor: colorMap[category],
                        }}
                      />
                    </div>
                  </div>
                ))}
            </div>
          </div>

          {/* Chart */}
          <div>
            <h3 className="text-base sm:text-lg font-semibold text-gray-900 mb-3 sm:mb-4">Visual Confidence</h3>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis label={{ value: 'Confidence (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value) => `${value}%`} />
                <Legend />
                <Bar dataKey="confidence" name="Confidence %" radius={[8, 8, 0, 0]}>
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={colorMap[entry.category]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Interpretation */}
          <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
            <h4 className="font-semibold text-blue-900 mb-2">What does this mean?</h4>
            <p className="text-sm text-blue-800">
              {prediction === 'High' && (
                'Your SME shows strong indicators for high growth potential. Focus on scaling operations and maintaining momentum.'
              )}
              {prediction === 'Medium' && (
                'Your SME demonstrates moderate growth potential. Consider addressing key challenges to move toward high growth.'
              )}
              {prediction === 'Low' && (
                'Your SME may face growth challenges. Focus on improving operational efficiency and addressing identified barriers.'
              )}
            </p>
          </div>

          {/* Action Button */}
          <div className="flex justify-center pt-4">
            <button
              onClick={onClose}
              className="w-full sm:w-auto px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition shadow-lg text-sm sm:text-base"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultsModal;
