# Rubix Language Translation Tool

This project is a real-time language translation system built for the CodeAlpha Artificial Intelligence Internship. Instead of a basic monolithic script, this project implements a scalable client-server architecture.

## Tech Stack
* **Backend:** FastAPI (Python), Uvicorn, deep-translator
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
* **Features:** Real-time translation with debouncing, Auto-detect languages, Text-to-Speech (TTS) integration, and Dark/Light Mode.

## How to Run Locally
1. Clone the repository.
2. Set up a Python virtual environment and install dependencies: `pip install fastapi uvicorn deep-translator`
3. Start the backend server: `uvicorn main:app --reload`
4. Open `index.html` in your browser.
