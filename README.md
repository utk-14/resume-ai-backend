# resume-ai-backend


This is a FastAPI-based backend for a resume analysis tool. It allows users to upload a PDF resume, extracts relevant details (such as skills and email), generates technical interview questions using the OpenRouter LLM API, and stores this information in a local SQLite database.

## Features

- Upload resumes in PDF format
- Extract skills and email address using simple parsing logic
- Generate five interview questions based on extracted skills using OpenRouter
- Store each upload and its results in the database with a timestamp
- Retrieve a history of past resume uploads

## Tech Stack

- FastAPI for the web framework
- SQLite with SQLAlchemy for data persistence
- PyMuPDF for PDF parsing
- OpenRouter LLM API for generating questions
- Python Dotenv for managing environment variables

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-ai-backend.git
cd resume-ai-backend
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Inside the root directory, create a `.env` file and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can visit `http://127.0.0.1:8000/docs` to test the API via Swagger UI.

## File Descriptions

* `main.py`: Main FastAPI application. Handles routes for upload and history.
* `models.py`: Contains the SQLAlchemy model for storing resume entries.
* `resume_parser.py`: Extracts email and skills from raw resume text.
* `openrouter_ai.py`: Handles communication with the OpenRouter API.
* `requirements.txt`: Lists all Python packages required.
* `.env`: Stores environment variables (not to be committed to Git).
* `database.db`: SQLite database created automatically.

## Deployment Notes

Make sure to exclude the following files from version control by adding them to `.gitignore`:

```
.env
__pycache__/
database.db
temp_resume.pdf
venv/
```

## License

This project is open-source and free to use for educational or personal use.

```

---


