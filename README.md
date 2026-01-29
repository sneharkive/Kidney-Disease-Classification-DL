# Kidney Disease Classification using Deep Learning

This project is an end-to-end Deep Learning application designed to classify kidney CT scan images into **Tumor** or **Normal** categories. It follows MLOps best practices by using **DVC** for pipeline orchestration, **MLflow** for experiment tracking, and **GitHub Actions** for CI/CD deployment on AWS.

## 🔗 Live Demo

You can access the live application here:

**[Kidney Disease Classification Web App](https://kidney-disease-classification-dl-1.onrender.com/)**

---

Would you like me to help you format this into a "Live Demo" button or badge for your README?

## 📊 Model Performance & Metrics

Based on the latest evaluation run, the model achieves the following performance:

* **Accuracy**: 89.4%
* **Loss Score**: 0.6214
* **Base Architecture**: VGG16 with Global Average Pooling
* **Optimization**: Adam Optimizer with a Learning Rate of 0.0001

---

## 🚀 Key Features

* **Modular Architecture**: Clean separation between data ingestion, model preparation, training, and evaluation.
* **DVC Integration**: Pipelines are version-controlled via `dvc.yaml`, ensuring reproducibility of artifacts.
* **Experiment Tracking**: Full integration with **MLflow** and **DagsHub** to monitor parameters and metrics.
* **Interactive Web App**: A Flask-based UI for users to upload CT scans and get instant predictions.
* **Dockerized Deployment**: Production-ready container using Gunicorn and lightweight Python images.

---

## 🛠️ Tech Stack

* **Framework**: TensorFlow/Keras
* **Tools**: DVC, MLflow, DagsHub
* **Web**: Flask, HTML/CSS
* **Cloud/DevOps**: AWS (ECR, EC2), GitHub Actions, Docker

---

## 📂 Project Structure

```text
├── .github/workflows/   # CI/CD pipeline definitions
├── config/              # YAML configuration for pipeline stages
├── logs/                # Project log files
├── model/               # Final trained model storage (.h5)
├── research/            # Experimental Jupyter Notebooks (.ipynb)
├── src/                 # Source Code
│   └── cnnClassifier/
│       ├── components/  # Data ingestion, training, evaluation logic
│       ├── config/      # Configuration manager
│       ├── constants/   # Project constants (file paths)
│       ├── entity/      # Data entities (dataclasses)
│       ├── pipeline/    # Stage-wise execution scripts (Data Ingestion to Eval)
│       └── utils/       # Common helper functions (read_yaml, save_json)
├── templates/           # HTML files for the Flask app (index.html)
├── app.py               # Flask Web Server entry point
├── Dockerfile           # Docker image configuration
├── dvc.yaml             # DVC Pipeline definition
├── main.py              # Training pipeline execution script
├── params.yaml          # Global hyperparameters
├── requirements.txt     # Development dependencies
└── setup.py             # Package installation script

```

---

## 🏃 How to Run

### 1. Environment Setup

```bash
conda create -n kidney python=3.10 -y
conda activate kidney
pip install -r requirements.txt

```

### 2. Run the Full Pipeline

You can trigger the entire workflow (Data Ingestion -> Base Model -> Training -> Evaluation) using:

```bash
dvc repro

```

*Alternatively, run `python main.py` to execute stages sequentially.*

### 3. Start the Web Application

```bash
python app.py

```

Open `http://localhost:8080` in your browser.

---

## 🐳 Docker Production Setup

```bash
docker build -t kidney-app .
docker run -p 8080:8080 kidney-app

```

---

## 🌐 CI/CD & Deployment

The project is configured with GitHub Actions to automate deployment to AWS:

1. **Continuous Integration**: Code linting and unit testing.
2. **Continuous Delivery**: Build Docker image and push to **Amazon ECR**.
3. **Continuous Deployment**: Deploy the latest image to **Amazon EC2**.

### Required GitHub Secrets:

* `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`
* `AWS_REGION`
* `AWS_ECR_LOGIN_URI`
* `ECR_REPOSITORY_NAME`
* `MLFLOW_TRACKING_URI` / `MLFLOW_TRACKING_USERNAME` / `MLFLOW_TRACKING_PASSWORD`

---

## 🛡️ API Endpoints

* `GET /`: Access the web interface.
* `GET /health`: Verify service status.
* `POST /predict`: Upload image (Base64 or File) for classification.

---

