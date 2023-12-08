FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app 
RUN pip install -r requirements.txt

COPY app_penguins.py app_penguins.py

# Copy the pickled model
COPY model.pkl model.pkl

CMD ["uvicorn", "--host", "0.0.0.0", "app_penguins:app"]

