from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import os

app = FastAPI()

# Load trained model
model_path = "iris_model.joblib"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = joblib.load(model_path)

# Define input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Root endpoint – serve form
@app.get("/", response_class=HTMLResponse)
def serve_form():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head><title>Iris Predictor</title></head>
    <body>
      <h2>Iris Species Predictor</h2>
      <form id="irisForm">
        <input type="number" step="any" name="sepal_length" placeholder="Sepal Length" required><br>
        <input type="number" step="any" name="sepal_width" placeholder="Sepal Width" required><br>
        <input type="number" step="any" name="petal_length" placeholder="Petal Length" required><br>
        <input type="number" step="any" name="petal_width" placeholder="Petal Width" required><br>
        <button type="submit">Predict</button>
      </form>
      <p id="result"></p>

      <script>
        document.getElementById('irisForm').addEventListener('submit', async (e) => {
          e.preventDefault();
          const formData = new FormData(e.target);
          const data = Object.fromEntries(formData.entries());
          Object.keys(data).forEach(k => data[k] = parseFloat(data[k]));

          const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
          });

          const result = await response.json();
          document.getElementById('result').innerText = `Predicted Species: ${result.predicted_species}`;
        });
      </script>
    </body>
    </html>
    """
    return html_content

# Prediction endpoint
@app.post("/predict")
def predict_species(features: IrisFeatures):
    input_data = np.array([[features.sepal_length,
                            features.sepal_width,
                            features.petal_length,
                            features.petal_width]])
    prediction = model.predict(input_data)
    return {"predicted_species": prediction[0]}