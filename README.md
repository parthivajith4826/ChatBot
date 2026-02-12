# 🤖 ChatBot – FastAPI AI Chat Application

A Dockerized FastAPI-based chatbot application deployed on Render.  
This project demonstrates backend API development, containerization with Docker, and cloud deployment using a free-tier hosting service.

---

## 🚀 Live Demo

👉 **Access the live application here:**  
https://chatbot-oeew.onrender.com/

> ⚠️ Note:  
> This app is hosted on Render’s free tier.  
> If the app is inactive, the first request may take **30–60 seconds** to load due to cold start.

---

## 📌 Features

- FastAPI backend
- AI-powered chat responses (Gemini API)
- Dockerized for consistent environments
- Deployed on Render using Docker
- Environment variable–based configuration
- Swagger API documentation

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python)
- **AI API:** Google Gemini
- **Containerization:** Docker
- **Deployment:** Render (Docker Web Service)
- **Language:** Python 3.12

---

## 📂 Project Structure

ChatBot/
├── Dockerfile
├── main.py
├── requirements.txt
├── templates/
├── static/
└── .dockerignore


---

## ⚙️ Environment Variables

The following environment variable is required:

GEMINI_API_KEY=your_api_key_here


This is configured securely on the hosting platform and **not committed to the repository**.

---

## 🧪 API Documentation

Once the app is running, Swagger UI is available at:

/docs


Example:
https://chatbot-oeew.onrender.com/docs


---

## ▶️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
Then open:

http://127.0.0.1:8000/docs
🐳 Run with Docker
Build the image:

docker build -t fastapi-chatbot .
Run the container:

docker run -p 8000:8000 fastapi-chatbot
🌐 Deployment
This project is deployed on Render using a Docker-based web service.

Key deployment highlights:

Docker runtime

Dynamic port binding using $PORT

Environment variables injected at runtime

Free-tier hosting with automatic sleep

⚠️ Known Limitations
Cold start delay on first request (Render free tier)

Limited request quota based on AI API free tier

📌 Purpose of This Project
This project was built to:

Learn FastAPI in a real-world setup

Understand Docker fundamentals

Practice cloud deployment workflows

Demonstrate backend engineering skills in a portfolio-ready project
