# This is one of the my AI-Internship Project

## 🩺 Chest X-Ray Pneumonia Detection using Deep Learning

A Deep Learning web application that detects Pneumonia from Chest X-Ray images using a trained Convolutional Neural Network (CNN).

The application is built with Python, deployed with Docker, and automated using CI/CD pipelines.

## Project Overview

Pneumonia is a serious lung infection that can be identified through chest X-ray images.
This project uses Deep Learning to automatically classify X-ray images as:

- Normal

- Pneumonia

The system provides a simple web interface where users can upload a chest X-ray image and receive a prediction.

🛠️ Tech Stack

Python

TensorFlow

Streamlit

Docker

GitHub Actions

Docker Hub

## Project Structure
Chest-Xray-Project
│
├── app.py                 # Streamlit application
├── model3.keras           # Trained CNN model
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container configuration
├── README.md              # Project documentation
│
└── .github
     └── workflows
           docker.yml      # CI/CD pipeline

## Installation

Clone the repository:

git clone https://github.com/Nareshnear208/PRAICP-1012-Pneumonia-chest-x-ray-classification

cd chest-xray-project

## Install dependencies:

pip install -r requirements.txt

## Run the application:

streamlit run app.py

🐳 Run with Docker

#### Build the Docker image:

docker build -t nareshbabu2026ai/chest-xray .

#### Run the container:

docker run -p 8501:8501 nareshbabu2026ai/chest-xray

Open the app in your browser:

http://localhost:8501

## CI/CD Pipeline

This project uses GitHub Actions to automatically:

Build Docker images

Push images to Docker Hub

Docker Image:

docker pull nareshbabu2026ai/chest-xray-streamlit:latest

## Model Information

The model is trained using MobileNetV2 --> Build Transfer Learning Model to classify chest X-ray images.

Workflow

Image preprocessing

CNN model prediction

Classification output

Display result on web interface

## Application Demo

Upload a chest X-ray image and the system will predict:

Normal

Pneumonia

## Features

Deep Learning based medical image classification

Interactive web interface

Docker containerized deployment

Automated CI/CD pipeline

Easy deployment and scalability

## Future Improvements

Add more medical datasets

Improve model accuracy

Deploy on cloud platforms

Add Grad-CAM visualization for model explainability

## 👨‍💻 Author

Naresh Babu

AI / Machine Learning Enthusiast

⭐ If you like this project, consider giving it a star on GitHub.