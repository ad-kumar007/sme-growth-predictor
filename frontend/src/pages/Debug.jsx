import React, { useState } from 'react';

function Debug() {
  const [testResult, setTestResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const apiUrl = import.meta.env.VITE_API_BASE_URL || 'NOT SET';

  const testConnection = async () => {
    setLoading(true);
    setTestResult(null);

    try {
      const response = await fetch(`${apiUrl}/health`);
      const data = await response.json();
      setTestResult({
        success: true,
        status: response.status,
        data: data
      });
    } catch (error) {
      setTestResult({
        success: false,
        error: error.message
      });
    } finally {
      setLoading(false);
    }
  };

  const testDashboard = async () => {
    setLoading(true);
    setTestResult(null);

    try {
      const response = await fetch(`${apiUrl}/api/dashboard/stats`);
      const data = await response.json();
      setTestResult({
        success: true,
        status: response.status,
        data: data
      });
    } catch (error) {
      setTestResult({
        success: false,
        error: error.message
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-4 sm:p-6">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h1 className="text-2xl font-bold text-gray-900 mb-6">🔧 Debug Information</h1>

        {/* Environment Info */}
        <div className="mb-6 p-4 bg-blue-50 rounded-lg">
          <h2 className="text-lg font-semibold text-blue-900 mb-2">Environment Variables</h2>
          <div className="space-y-2 text-sm">
            <div>
              <span className="font-medium">VITE_API_BASE_URL:</span>
              <code className="ml-2 px-2 py-1 bg-blue-100 rounded">{apiUrl}</code>
            </div>
            <div>
              <span className="font-medium">Current URL:</span>
              <code className="ml-2 px-2 py-1 bg-blue-100 rounded">{window.location.href}</code>
            </div>
          </div>
        </div>

        {/* Test Buttons */}
        <div className="mb-6 space-y-3">
          <button
            onClick={testConnection}
            disabled={loading}
            className="w-full px-4 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 font-semibold"
          >
            {loading ? 'Testing...' : '✓ Test Backend Health'}
          </button>

          <button
            onClick={testDashboard}
            disabled={loading}
            className="w-full px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 font-semibold"
          >
            {loading ? 'Testing...' : '📊 Test Dashboard API'}
          </button>
        </div>

        {/* Results */}
        {testResult && (
          <div className={`p-4 rounded-lg ${testResult.success ? 'bg-green-50 border-l-4 border-green-500' : 'bg-red-50 border-l-4 border-red-500'}`}>
            <h3 className={`font-semibold mb-2 ${testResult.success ? 'text-green-900' : 'text-red-900'}`}>
              {testResult.success ? '✅ Success' : '❌ Failed'}
            </h3>
            
            {testResult.success ? (
              <div className="space-y-2">
                <div>
                  <span className="font-medium">Status:</span> {testResult.status}
                </div>
                <div>
                  <span className="font-medium">Response:</span>
                  <pre className="mt-2 p-3 bg-white rounded text-xs overflow-auto">
                    {JSON.stringify(testResult.data, null, 2)}
                  </pre>
                </div>
              </div>
            ) : (
              <div className="text-red-700">
                <p className="font-medium">Error:</p>
                <p className="mt-1">{testResult.error}</p>
                
                <div className="mt-4 p-3 bg-red-100 rounded text-sm">
                  <p className="font-semibold mb-2">Possible Issues:</p>
                  <ul className="list-disc list-inside space-y-1">
                    <li>Backend is down or sleeping (wait 30s and retry)</li>
                    <li>CORS issue (check backend CORS settings)</li>
                    <li>Wrong API URL in environment variables</li>
                    <li>Network/firewall blocking the request</li>
                  </ul>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Instructions */}
        <div className="mt-6 p-4 bg-gray-50 rounded-lg text-sm">
          <h3 className="font-semibold text-gray-900 mb-2">📝 What to check:</h3>
          <ol className="list-decimal list-inside space-y-1 text-gray-700">
            <li>Is VITE_API_BASE_URL set correctly above?</li>
            <li>Does it point to: <code className="px-1 bg-gray-200 rounded">https://sme-growth-predictor-1.onrender.com</code></li>
            <li>Click "Test Backend Health" - does it succeed?</li>
            <li>Click "Test Dashboard API" - does it succeed?</li>
            <li>If both succeed, the dashboard should work!</li>
          </ol>
        </div>

        {/* Quick Fixes */}
        <div className="mt-4 p-4 bg-yellow-50 rounded-lg text-sm">
          <h3 className="font-semibold text-yellow-900 mb-2">⚡ Quick Fixes:</h3>
          <ul className="list-disc list-inside space-y-1 text-yellow-800">
            <li>Hard refresh: <kbd className="px-2 py-1 bg-yellow-100 rounded">Ctrl+Shift+R</kbd></li>
            <li>Try incognito/private mode</li>
            <li>Clear browser cache</li>
            <li>Wait 30 seconds if backend is sleeping</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Debug;
