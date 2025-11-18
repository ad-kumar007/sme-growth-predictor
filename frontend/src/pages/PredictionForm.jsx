import React, { useState } from 'react';
import { predictGrowth } from '../services/api';
import ResultsModal from '../components/ResultsModal';

function PredictionForm() {
  const [formData, setFormData] = useState({
    Location: '',
    'About Enterprises, Owners Motivation': '',
    'Enabler 2:Operational Process , Legacy & new machine to balance': '',
    'Enabler 1: Effortable Digital technologies': '',
    'Outcome : Growth and Effeciency': '',
    'Enabler 2 :Certification &Standarization': '',
    'Challanges3: Financial assistant & Incentive ,transparency in institutional support ,': '',
    'Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges': '',
    'Enabler 4: Engaging local hire': '',
    'Challenges 2: Skill Gap ,Retaining resources and workforce Management': '',
    Enterprise_Age: '',
    'Small/Medium/Large': 'Medium',
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Convert numeric fields to numbers
      const processedData = {
        ...formData,
        Location: parseFloat(formData.Location),
        'About Enterprises, Owners Motivation': parseInt(formData['About Enterprises, Owners Motivation']),
        'Enabler 2:Operational Process , Legacy & new machine to balance': parseInt(formData['Enabler 2:Operational Process , Legacy & new machine to balance']),
        'Enabler 1: Effortable Digital technologies': parseInt(formData['Enabler 1: Effortable Digital technologies']),
        'Outcome : Growth and Effeciency': parseFloat(formData['Outcome : Growth and Effeciency']),
        'Enabler 2 :Certification &Standarization': parseInt(formData['Enabler 2 :Certification &Standarization']),
        'Challanges3: Financial assistant & Incentive ,transparency in institutional support ,': parseInt(formData['Challanges3: Financial assistant & Incentive ,transparency in institutional support ,']),
        'Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges': parseInt(formData['Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges']),
        'Enabler 4: Engaging local hire': parseInt(formData['Enabler 4: Engaging local hire']),
        'Challenges 2: Skill Gap ,Retaining resources and workforce Management': parseInt(formData['Challenges 2: Skill Gap ,Retaining resources and workforce Management']),
        Enterprise_Age: parseInt(formData.Enterprise_Age),
      };

      const response = await predictGrowth(processedData);
      setResult(response);
      setShowModal(true);
    } catch (err) {
      setError(err.detail || 'An error occurred during prediction');
      console.error('Prediction error:', err);
    } finally {
      setLoading(false);
    }
  };

  const formFields = [
    { name: 'Location', label: 'Location Code', type: 'number', step: '0.1', placeholder: '1.0', help: 'Geographic location identifier' },
    { name: 'About Enterprises, Owners Motivation', label: 'Owner Motivation Level', type: 'number', placeholder: '1-5', help: 'Owner motivation score (1-5)' },
    { name: 'Enabler 2:Operational Process , Legacy & new machine to balance', label: 'Operational Process Enabler', type: 'number', placeholder: '1-5', help: 'Operational process maturity (1-5)' },
    { name: 'Enabler 1: Effortable Digital technologies', label: 'Digital Technology Affordability', type: 'number', placeholder: '1-5', help: 'Access to affordable digital tech (1-5)' },
    { name: 'Outcome : Growth and Effeciency', label: 'Growth & Efficiency Score', type: 'number', step: '0.1', placeholder: '0-100', help: 'Current growth and efficiency metric' },
    { name: 'Enabler 2 :Certification &Standarization', label: 'Certification & Standardization', type: 'number', placeholder: '1-5', help: 'Level of certifications (1-5)' },
    { name: 'Challanges3: Financial assistant & Incentive ,transparency in institutional support ,', label: 'Financial Assistance Challenges', type: 'number', placeholder: '1-5', help: 'Financial support challenges (1-5)' },
    { name: 'Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges', label: 'Administrative Hurdles', type: 'number', placeholder: '1-5', help: 'Regulatory challenges (1-5)' },
    { name: 'Enabler 4: Engaging local hire', label: 'Local Hiring Engagement', type: 'number', placeholder: '1-5', help: 'Local workforce engagement (1-5)' },
    { name: 'Challenges 2: Skill Gap ,Retaining resources and workforce Management', label: 'Skill Gap & Workforce Challenges', type: 'number', placeholder: '1-5', help: 'Workforce management challenges (1-5)' },
    { name: 'Enterprise_Age', label: 'Enterprise Age (Years)', type: 'number', placeholder: '5', help: 'Age of the enterprise in years' },
  ];

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-xl p-4 sm:p-6 md:p-8">
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-2">SME Growth Prediction</h1>
        <p className="text-sm sm:text-base text-gray-600 mb-6 sm:mb-8">
          Fill in your enterprise details to predict the growth category
        </p>

        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-6">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="ml-3">
                <p className="text-sm text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4 sm:space-y-6">
          {/* Enterprise Size */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Enterprise Size *
            </label>
            <select
              name="Small/Medium/Large"
              value={formData['Small/Medium/Large']}
              onChange={handleChange}
              required
              className="w-full px-3 sm:px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm sm:text-base"
            >
              <option value="">Select Size</option>
              <option value="Small">Small</option>
              <option value="Medium">Medium</option>
              <option value="Large">Large</option>
            </select>
          </div>

          {/* Dynamic Fields */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
            {formFields.map((field) => (
              <div key={field.name}>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  {field.label} *
                </label>
                <input
                  type={field.type}
                  name={field.name}
                  value={formData[field.name]}
                  onChange={handleChange}
                  placeholder={field.placeholder}
                  step={field.type === 'number' && field.name === 'Location' ? '0.1' : '1'}
                  required
                  className="w-full px-3 sm:px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm sm:text-base"
                />
                {field.help && (
                  <p className="mt-1 text-xs text-gray-500">{field.help}</p>
                )}
              </div>
            ))}
          </div>

          {/* Submit Button */}
          <div className="flex justify-center pt-6">
            <button
              type="submit"
              disabled={loading}
              className={`px-8 py-3 rounded-lg text-white font-semibold text-lg transition shadow-lg ${
                loading
                  ? 'bg-gray-400 cursor-not-allowed'
                  : 'bg-blue-600 hover:bg-blue-700 hover:shadow-xl'
              }`}
            >
              {loading ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </span>
              ) : (
                'Predict Growth Category'
              )}
            </button>
          </div>
        </form>
      </div>

      {/* Results Modal */}
      {showModal && result && (
        <ResultsModal
          result={result}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
}

export default PredictionForm;
