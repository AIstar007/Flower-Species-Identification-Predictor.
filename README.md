# 🌸 Iris Classifier API (FastAPI + Docker)

A simple machine learning API built with **FastAPI**, containerized using **Docker**, and deployed on **Render**. It predicts the species of an Iris flower based on its features.

---

## 🚀 Features

- 🔍 Predict iris species from input features
- 🧠 Trained with `scikit-learn`
- ⚡ Powered by `FastAPI`
- 🐳 Dockerized
- 🌐 Live-deployed on Render
- 🧪 Includes unit tests with `pytest`
- 🖼️ Optional HTML form frontend

---

## 🔧 Requirements

- Python 3.8+
- Docker (for local containerization)
- Uvicorn / FastAPI
- Scikit-learn
- Joblib

---

## 🧠 Model

The model is trained on the classic Iris dataset and saved as `iris_model.joblib`.

---

## 📦 Installation (Local)

```bash
git clone https://github.com/YOUR_USERNAME/iris-fastapi.git
cd iris-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)  
Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Setup

```bash
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```

---

## 🌍 Deployment (Render) [Optional]

1. Push project to GitHub
2. Go to [https://render.com](https://render.com)
3. Click **"New Web Service"**
4. Connect GitHub repo
5. Select **Docker environment**
6. Deploy 🚀

Visit: [https://flower-species-identification-predictor.onrender.com](https://flower-species-identification-predictor.onrender.com)  
Swagger docs: [https://flower-species-identification-predictor.onrender.com/docs](https://flower-species-identification-predictor.onrender.com/docs)

---

## 📬 Prediction Endpoint

**POST** `/predict`

Example input:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "predicted_species": "setosa"
}
```

---

## 🧪 Run Tests

```bash
pytest test_app.py
```

---

## 📁 Project Structure

```ini
iris-fastapi/
├── main.py              # FastAPI app with model and UI
├── test_app.py          # Pytest API tests using TestClient
├── test_predict.py      # Optional Python script to test /predict
├── test_model.py        # Optional script to test model loading
├── iris_model.joblib    # Trained model
├── index.html           # Optional HTML form served by FastAPI
├── requirements.txt     # Dependencies
├── .dockerignore        # Ignored files in Docker context
├── Dockerfile           # Containerization
└── README.md            # Project guide
```

---

## 📄 License

MIT License.
