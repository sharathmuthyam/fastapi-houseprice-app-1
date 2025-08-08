FastAPI House Price Prediction API
This project demonstrates the basic creation of a REST API for a machine learning model using FastAPI, and its containerization with Docker for deployment on AWS EC2.

What’s Included
A trained ML model (joblib)

FastAPI application to serve predictions

Docker setup to containerize the app

Deployment steps for running on an AWS EC2 instance

Tech Stack
Python (FastAPI, scikit-learn, joblib)

Docker

AWS EC2

📦 Project Structure
bash
Copy
Edit
app.py               # FastAPI app with prediction endpoint
model.joblib         # Trained ML model
scaler.joblib        # Feature scaler
features.pkl         # Feature names used by the model
Dockerfile           # Instructions to containerize the app
requirements.txt     # Python dependencies
🛠️ How to Run
Build Docker Image

bash
Copy
Edit
docker build -t housepriceapp .
Run Container

bash
Copy
Edit
docker run -d -p 8000:8000 housepriceapp
Access the API
Open your browser or use Postman:
http://<your-ip>:8000/docs

