# Bengaluru House Price Prediction

A Machine Learning project to predict house prices in Bengaluru, India using historical housing data. This project is fully Dockerized and can be deployed locally or on an AWS EC2 instance.

---

# Project Demo Link
http://ec2-18-169-184-55.eu-west-2.compute.amazonaws.com/

---

## Tech Stack
- Python (Pandas, Numpy, Data Cleaning, Outlier detection, Features Engineering, EDA)
- Machine Learning Model Development (Linear Regression, Lasso Regression, Decision Tree, Hyperparameter tuning)
- Flask (for backend Server Api)
- Nginx Webserver for frontend to interact with flask API Server
- Docker
- AWS EC2, ECR Services
- HTML, CSS, JavaScript (For Developing website Frontend to integrate CLient)
- Github

## Project Structure

```
house_prediction_price/
│
├── client/                  # Frontend files (HTML, CSS, JS)
│   ├── app.html
│   ├── app.js
│   └── app.css
│
├── model/                   # Machine learning models and artifacts
│   └── house_price_model.pkl
│   └── columns.json
│
├── dataset/                 # Dataset used for training
│   └── Bengaluru_House_Data.csv
│
├── notebook/                # Jupyter notebooks for EDA & model development
│   └── house_price_prediction.ipynb
├── Server/                # backend flask Server API
│   └── server.py
│   └── util.py
│
├── Dockerfile               # Docker configuration file
├── start.sh                 # Script to start Flask + Nginx inside Docker
├── requirements.txt         # Python dependencies
├── .dockerignore
└── README.md
```

---

## Dataset

- Kaggle link: [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- The dataset contains historical house price information including location, size, total_sqft, bath, price, etc.
- Used for training the Machine Learning model in this project.

---

## Features

- Predicts house prices based on input features like location, size, total_sqft, bathrooms, etc.
- Flask API serves predictions.
- Frontend allows users to interact with the model.
- Fully Dockerized with Nginx Web Server for serving the frontend and backend.

---

## Dockerized Deployment

### Prerequisites

- Docker installed locally
- AWS ECR account (optional for public image deployment)
- Linux or Windows system for running Docker

### Public Docker Image

The project is available as a Docker image on **AWS ECR Public**:

#### Install Docker on Ubuntu at AWS EC2 service

If Docker is not installed, run:
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```
### To check docker installation with:
```bash
docker --version
```
### To access docker image for public AWS Elastic Container Registry
```bash
public.ecr.aws/u6v5h4w6/abhishek/house-price-prediction:latest
```

### Pull and Run Docker Image

```bash
docker pull public.ecr.aws/u6v5h4w6/abhishek/house-price-prediction:latest
docker run -d -p 80:80 public.ecr.aws/u6v5h4w6/abhishek/house-price-prediction:latest
```

- `-p 80:80` maps the container's port 80 to your local machine’s port 80.
- The container runs Flask backend and Nginx frontend together.
- The server remains active even if you close the terminal.

---

## Local Deployment

1. Clone the repository:

```bash
git clone <repo-url>
cd house_prediction_price
```
2.  Install Docker on Windows
- Download Docker Desktop from https://www.docker.com/products/docker-desktop
3. Build Docker image locally:

```bash
docker build -t house-price-prediction .
```

4. Run the container:

```bash
docker run -d --name house-price-app -p 80:80 house-price-prediction
```

---

## API Endpoints

- **Health Check:**
  ```
  GET /api/health
  ```
- **Get Locations:**
  ```
  GET /api/get_location_names
  ```
- **Predict House Price:**
  ```
  POST /api/predict_home_price
  Content-Type: application/json
  Body: {
      "total_sqft": 1000,
      "location": "Whitefield",
      "bhk": 3,
      "bath": 2
  }
  ```

---

## Frontend & Backend

- Frontend files are in `client/` folder.
- Interacts with Flask API to fetch location names and predictions which is in `Server/` folder.
- Served via Nginx inside Docker.

---

## Development Notes

- ML model trained using `Bengaluru_House_Data.csv`.
- Jupyter notebook available in `notebook/` for EDA, preprocessing, and model training.
- Flask API loads the model and serves endpoints.
- Trained ML model saved in `model` folder with pickle file `bengaluru_house_price_model.pkl`
- `start.sh` is used in Docker to run Flask backend and Nginx frontend together.

---

## Acknowledgements

- Dataset from Kaggle: [Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- Docker & AWS ECR documentation for deployment guidance

