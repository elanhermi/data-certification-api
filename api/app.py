
from fastapi import FastAPI
import requests
import joblib
import json

app = FastAPI()

with open("model.joblib") as f:
        my_model = joblib.load(f)

@app.get("/predict")

def predict_popularity():
    url = 'http://localhost:8000/predict'
    params = {
    'acousticness': 0.654,
    'danceability': 0.499,
    'duration_ms': 219827,
    'energy': 0.19,
    'explicit': 0,
    'id': '0B6BeEUd6UwFlbsHMQKjob',
    'instrumentalness': 0.00409,
    'key': 7,
    'liveness': 0.0898,
    'loudness': 16.435,
    'mode': 1,
    'name': 'Back in the Goodle Days',
    'release_date': 1971,
    'speechiness': 0.0454,
    'tempo': 149.46,
    'valence': 0.43, 
    'artist': 'John Hartford'
    }
    response = requests.get(url, params=params)
    return response.json()


# Implement a /predict endpoint
