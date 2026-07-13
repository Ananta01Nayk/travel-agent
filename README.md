#  Namaste India Trip AI Travel Agent

An AI-powered travel assistant that helps users discover the best travel
packages across India using Retrieval-Augmented Generation (RAG),
FastAPI, React, ChromaDB, and Google's Gemini API.

##  Live Demo

**Frontend:** https://travel-agent-frontend-13tg.onrender.com

**Backend API:** https://travel-agent-5yk7.onrender.com

##  Features

-   AI Travel Assistant (Bharti)
-   RAG-based package retrieval
-   Google Gemini 2.5 Flash
-   ChromaDB vector database
-   FastAPI backend
-   React + Tailwind frontend
-   Docker
-   GitHub Actions
-   Render & Vercel deployment

##  Architecture

User → React → FastAPI → RAG → ChromaDB → Gemini API

##  Tech Stack

Frontend: React, Vite, Tailwind CSS, Axios

Backend: FastAPI, Uvicorn, Python

AI: Gemini, ChromaDB, Sentence Transformers

Deployment: Docker, Render, Vercel, GitHub Actions

##  Installation

``` bash
git clone https://github.com/Ananta01Nayk/travel-agent.git
cd travel-agent

python -m venv travel-agent
travel-agent\Scripts\activate

pip install -r requirements.txt

uvicorn api.main:app --reload
```

Frontend:

``` bash
cd frontend
npm install
npm run dev
```

##  Environment Variables

``` env
GOOGLE_API_KEY=your_google_api_key
VITE_API_URL=http://127.0.0.1:8000(local run)
```

##  Author

**Ananta Nayak**

GitHub: https://github.com/Ananta01Nayk

LinkedIn: https://www.linkedin.com/in/ananta-nayak

## ⭐ Support

If you like this project, please give it a star on GitHub.
