FROM python:3.9-slim

WORKDIR /app

COPY ./models ./models
COPY ./data ./data
COPY api.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]