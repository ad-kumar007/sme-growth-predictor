# 🔌 API Examples - SME Growth Predictor

Complete examples for interacting with the API.

## Base URL

```
http://localhost:8000
```

---

## 1️⃣ Health Check

### Request

```bash
curl http://localhost:8000/health
```

### Response

```json
{
  "status": "healthy",
  "message": "API running"
}
```

---

## 2️⃣ Make Prediction

### Request (cURL)

```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Location": 1.0,
    "About Enterprises, Owners Motivation": 3,
    "Enabler 2:Operational Process , Legacy & new machine to balance": 2,
    "Enabler 1: Effortable Digital technologies": 3,
    "Outcome : Growth and Effeciency": 65.5,
    "Enabler 2 :Certification &Standarization": 4,
    "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 2,
    "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 3,
    "Enabler 4: Engaging local hire": 2,
    "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 3,
    "Enterprise_Age": 15,
    "Small/Medium/Large": "Medium"
  }'
```

### Request (Python)

```python
import requests

url = "http://localhost:8000/api/predict"

payload = {
    "Location": 1.0,
    "About Enterprises, Owners Motivation": 3,
    "Enabler 2:Operational Process , Legacy & new machine to balance": 2,
    "Enabler 1: Effortable Digital technologies": 3,
    "Outcome : Growth and Effeciency": 65.5,
    "Enabler 2 :Certification &Standarization": 4,
    "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 2,
    "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 3,
    "Enabler 4: Engaging local hire": 2,
    "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 3,
    "Enterprise_Age": 15,
    "Small/Medium/Large": "Medium"
}

response = requests.post(url, json=payload)
print(response.json())
```

### Request (JavaScript)

```javascript
const url = 'http://localhost:8000/api/predict';

const payload = {
  "Location": 1.0,
  "About Enterprises, Owners Motivation": 3,
  "Enabler 2:Operational Process , Legacy & new machine to balance": 2,
  "Enabler 1: Effortable Digital technologies": 3,
  "Outcome : Growth and Effeciency": 65.5,
  "Enabler 2 :Certification &Standarization": 4,
  "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 2,
  "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 3,
  "Enabler 4: Engaging local hire": 2,
  "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 3,
  "Enterprise_Age": 15,
  "Small/Medium/Large": "Medium"
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(payload),
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### Response

```json
{
  "prediction": "Medium",
  "confidence_scores": {
    "High": 0.25,
    "Medium": 0.65,
    "Low": 0.10
  },
  "message": "Prediction successful"
}
```

---

## 3️⃣ Get Model Information

### Request

```bash
curl http://localhost:8000/api/model-info
```

### Response

```json
{
  "status": "success",
  "model_info": {
    "label_mapping": {
      "0": "High",
      "1": "Low",
      "2": "Medium"
    },
    "numeric_features": [
      "Location",
      "About Enterprises, Owners Motivation",
      "Enabler 2:Operational Process , Legacy & new machine to balance",
      "Enabler 1: Effortable Digital technologies",
      "Outcome : Growth and Effeciency",
      "Enabler 2 :Certification &Standarization",
      "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,",
      "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges",
      "Enabler 4: Engaging local hire",
      "Challenges 2: Skill Gap ,Retaining resources and workforce Management",
      "Enterprise_Age"
    ],
    "categorical_features": [
      "Small/Medium/Large"
    ],
    "performance": {
      "test_accuracy": 0.8095,
      "test_precision": 0.4740,
      "test_recall": 0.5030,
      "test_f1": 0.4847
    },
    "best_params": {
      "classifier__n_estimators": 200,
      "classifier__min_samples_split": 15,
      "classifier__min_samples_leaf": 5,
      "classifier__max_features": "sqrt",
      "classifier__max_depth": 8
    }
  }
}
```

---

## 4️⃣ Get Required Features

### Request

```bash
curl http://localhost:8000/api/features
```

### Response

```json
{
  "status": "success",
  "features": {
    "numeric": [
      "Location",
      "About Enterprises, Owners Motivation",
      "Enabler 2:Operational Process , Legacy & new machine to balance",
      "Enabler 1: Effortable Digital technologies",
      "Outcome : Growth and Effeciency",
      "Enabler 2 :Certification &Standarization",
      "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,",
      "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges",
      "Enabler 4: Engaging local hire",
      "Challenges 2: Skill Gap ,Retaining resources and workforce Management",
      "Enterprise_Age"
    ],
    "categorical": [
      "Small/Medium/Large"
    ],
    "all": [
      "Location",
      "About Enterprises, Owners Motivation",
      "Enabler 2:Operational Process , Legacy & new machine to balance",
      "Enabler 1: Effortable Digital technologies",
      "Outcome : Growth and Effeciency",
      "Enabler 2 :Certification &Standarization",
      "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,",
      "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges",
      "Enabler 4: Engaging local hire",
      "Challenges 2: Skill Gap ,Retaining resources and workforce Management",
      "Enterprise_Age",
      "Small/Medium/Large"
    ]
  }
}
```

---

## 📊 Sample Prediction Scenarios

### High Growth SME

```json
{
  "Location": 1.5,
  "About Enterprises, Owners Motivation": 5,
  "Enabler 2:Operational Process , Legacy & new machine to balance": 4,
  "Enabler 1: Effortable Digital technologies": 5,
  "Outcome : Growth and Effeciency": 85.0,
  "Enabler 2 :Certification &Standarization": 5,
  "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 1,
  "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 1,
  "Enabler 4: Engaging local hire": 4,
  "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 1,
  "Enterprise_Age": 20,
  "Small/Medium/Large": "Large"
}
```

**Expected Prediction:** High (with high confidence)

### Low Growth SME

```json
{
  "Location": 0.5,
  "About Enterprises, Owners Motivation": 2,
  "Enabler 2:Operational Process , Legacy & new machine to balance": 1,
  "Enabler 1: Effortable Digital technologies": 1,
  "Outcome : Growth and Effeciency": 25.0,
  "Enabler 2 :Certification &Standarization": 1,
  "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 5,
  "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 5,
  "Enabler 4: Engaging local hire": 1,
  "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 5,
  "Enterprise_Age": 3,
  "Small/Medium/Large": "Small"
}
```

**Expected Prediction:** Low (with high confidence)

### Medium Growth SME

```json
{
  "Location": 1.0,
  "About Enterprises, Owners Motivation": 3,
  "Enabler 2:Operational Process , Legacy & new machine to balance": 3,
  "Enabler 1: Effortable Digital technologies": 3,
  "Outcome : Growth and Effeciency": 55.0,
  "Enabler 2 :Certification &Standarization": 3,
  "Challanges3: Financial assistant & Incentive ,transparency in institutional support ,": 3,
  "Enabler 3: Administrative and Regulatory Hurdles & Eco system Integration challenges": 3,
  "Enabler 4: Engaging local hire": 3,
  "Challenges 2: Skill Gap ,Retaining resources and workforce Management": 3,
  "Enterprise_Age": 10,
  "Small/Medium/Large": "Medium"
}
```

**Expected Prediction:** Medium (with moderate confidence)

---

## 🔴 Error Responses

### Missing Required Field

**Request:**
```json
{
  "Location": 1.0,
  "Enterprise_Age": 15
}
```

**Response (400 Bad Request):**
```json
{
  "detail": "Missing required features: ['About Enterprises, Owners Motivation', ...]"
}
```

### Invalid Data Type

**Request:**
```json
{
  "Location": "invalid",
  "About Enterprises, Owners Motivation": 3,
  ...
}
```

**Response (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "Location"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

---

## 🧪 Testing with Postman

1. **Import Collection:**
   - Create new request
   - Set method to POST
   - URL: `http://localhost:8000/api/predict`
   - Headers: `Content-Type: application/json`
   - Body: Raw JSON (use examples above)

2. **Save as Collection** for reuse

---

## 📖 Interactive Documentation

Visit **http://localhost:8000/docs** for:
- Interactive API testing
- Automatic request/response examples
- Schema validation
- Try it out directly in browser

---

## 💡 Tips

1. **All numeric fields are required** - No null values allowed
2. **Size must be exact match** - "Small", "Medium", or "Large" (case-sensitive)
3. **Scores typically range 1-5** - For enabler and challenge fields
4. **Growth score is 0-100** - For "Outcome : Growth and Effeciency"
5. **Enterprise age in years** - Positive integer

---

**Need help? Check the [README.md](README.md) or [SETUP_GUIDE.md](SETUP_GUIDE.md)**
