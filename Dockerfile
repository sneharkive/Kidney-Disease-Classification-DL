FROM python:3.10-slim

WORKDIR /app

# Install minimal OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only production requirements
COPY requirements-prod.txt ./requirements.txt

# Upgrade pip and install only what you need for inference
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy necessary application files only
COPY app.py .
COPY src ./src
COPY templates ./templates
COPY model ./model

ENV PYTHONPATH="/app/src"
# (optional) download model here OR at runtime
# RUN python src/download_model.py

EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "app:app"]

