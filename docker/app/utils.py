# docker/app/utils.py

import joblib
import numpy as np
import os

MODEL_PATH = os.path.join("model", "model.pkl")

def load_model():
    model, feature_names = joblib.load(MODEL_PATH)
    return model, feature_names

def kmer_counts(seq, k=3):
    counts = {}
    total = len(seq) - k + 1
    for i in range(total):
        kmer = seq[i:i+k]
        counts[kmer] = counts.get(kmer, 0) + 1
    for k in counts:
        counts[k] /= total
    return counts

def vectorize_sequence(seq, feature_names, k=3):
    counts = kmer_counts(seq, k)
    return np.array([[counts.get(kmer, 0) for kmer in feature_names]])

def predict_sequence(seq):
    model, feature_names = load_model()
    vec = vectorize_sequence(seq, feature_names)
    prediction = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0].tolist()
    return {"prediction": int(prediction), "probability": proba}
