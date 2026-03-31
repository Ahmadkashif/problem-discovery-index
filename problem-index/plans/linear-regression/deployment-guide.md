# Deployment Guide — Taking Linear Regression Models to Production

This guide covers how to move from a Jupyter notebook to a system that makes predictions on new data automatically. You don't need to deploy anything during this learning plan — but understanding the path from notebook to production is part of thinking like an ML engineer.

---

## The Gap Between Notebook and Production

In your notebook, you do:
```python
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

In production, you need to answer:
1. How does new data get in?
2. How does the prediction get out?
3. How do you know the model is still working?
4. When do you retrain?

---

## Step 1: Save Your Model

```python
import joblib

# Save
joblib.dump(model, 'energy_model.pkl')
joblib.dump(scaler, 'scaler.pkl')  # if you used feature scaling

# Load later
model = joblib.load('energy_model.pkl')
```

Save the model AND any preprocessors (scalers, encoders). If you trained on scaled data, you need the same scaler to transform new data.

---

## Step 2: Build a Prediction Function

Wrap your model in a function that takes raw input and returns a prediction:

```python
def predict_eui(building_type: str, sqft: float, year_built: int, floors: int) -> float:
    """Predict Energy Use Intensity for a building."""
    # Encode inputs the same way as training
    features = encode_features(building_type, sqft, year_built, floors)
    # Predict
    log_eui = model.predict([features])[0]
    # Inverse log transform
    return np.expm1(log_eui)
```

This function is your **inference pipeline**. It handles all the preprocessing so the caller just passes raw values.

---

## Step 3: Serve It (Three Options)

### Option A: Script (Simplest)
Run predictions in a Python script on new CSV files. Good for batch predictions (e.g., score all buildings once per year).

### Option B: REST API (Most Common)
Wrap the prediction function in a FastAPI or Flask endpoint:

```python
from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
def predict(building_type: str, sqft: float, year_built: int, floors: int):
    eui = predict_eui(building_type, sqft, year_built, floors)
    return {"predicted_eui": round(eui, 1)}
```

### Option C: Streamlit Dashboard (Best for Learning)
Build a simple web UI where you input building features and see the prediction:

```python
import streamlit as st
building_type = st.selectbox("Building Type", ["Office", "Multifamily", "Hotel"])
sqft = st.number_input("Square Footage", value=50000)
# ... predict and display
```

---

## Step 4: Monitor Model Performance

Models degrade over time. New buildings have different characteristics. Energy codes change. You need to track:

- **Prediction drift:** Are predictions shifting systematically higher or lower over time?
- **Feature drift:** Are incoming feature distributions changing? (e.g., more mixed-use buildings than before)
- **Accuracy on new labeled data:** When new actual EUI numbers come in (annually for LL84), compare to your predictions.

If performance drops below your threshold, retrain on the latest data.

---

## Step 5: Retrain Cadence

| Project | Natural retrain frequency | Trigger |
|---------|--------------------------|---------|
| Building Energy | Annually (when new LL84 data drops) | New benchmarking year published |
| Restaurant Inspections | Quarterly | Inspection results accumulate |
| Crop Yield | Annually (post-harvest) | USDA publishes final county yields |

---

## What NOT to Worry About Yet

- Kubernetes, Docker, cloud deployment — overkill for learning
- Model versioning systems (MLflow, Weights & Biases) — useful later, not now
- A/B testing — relevant when you have users, not when you're learning
- GPU inference — linear regression doesn't need a GPU

Focus on: **Can I make a prediction on data I've never seen before, and is it reasonable?** That's deployment at its core.
