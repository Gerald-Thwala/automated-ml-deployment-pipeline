# docker/Dockerfile

FROM python:3.10-slim

WORKDIR /app

COPY model /app/model
COPY docker/app /app/app

RUN pip install fastapi uvicorn scikit-learn joblib

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
