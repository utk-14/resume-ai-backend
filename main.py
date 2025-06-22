# # main.py
# from fastapi import FastAPI, UploadFile, File
# import fitz  # PyMuPDF
# from resume_parser import parse_resume
# from openrouter_ai import generate_questions
# from models import SessionLocal, ResumeQuery

# app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "Resume AI backend is running!"}


# @app.post("/upload-resume/")
# async def upload_resume(file: UploadFile = File(...)):
#     if file.content_type != "application/pdf":
#         return {"error": "Only PDF files are supported for now."}

#     # Save and read PDF
#     contents = await file.read()
#     with open("temp_resume.pdf", "wb") as f:
#         f.write(contents)

#     doc = fitz.open("temp_resume.pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     doc.close()

#     # Parse resume
#     parsed = parse_resume(text)
#     skills = parsed.get("skills", [])
#     email = parsed.get("email", "unknown@example.com")

#     # Generate questions
#     questions = generate_questions(skills)

#     # Save to database
#     db = SessionLocal()
#     new_query = ResumeQuery(
#         email=email,
#         skills=", ".join(skills),
#         questions="\n".join(questions)
#     )
#     db.add(new_query)
#     db.commit()
#     db.close()

#     # ✅ This return was accidentally placed after the get_history route before
#     return {
#         "parsed_data": parsed,
#         "interview_questions": questions
#     }


# @app.get("/history/")
# def get_history():
#     db = SessionLocal()
#     entries = db.query(ResumeQuery).order_by(ResumeQuery.timestamp.desc()).all()
#     db.close()
#     return [
#         {
#             "email": entry.email,
#             "skills": entry.skills,
#             "questions": entry.questions,
#             "timestamp": entry.timestamp
#         }
#         for entry in entries
#     ]
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware  # ✅ Import this
import fitz  # PyMuPDF
from resume_parser import parse_resume
from openrouter_ai import generate_questions
from models import SessionLocal, ResumeQuery

app = FastAPI()

# ✅ Enable CORS so frontend (localhost:5173 or localhost:3000) can access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://localhost:5173"] if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Resume AI backend is running!"}

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "Only PDF files are supported for now."}

    contents = await file.read()
    with open("temp_resume.pdf", "wb") as f:
        f.write(contents)

    doc = fitz.open("temp_resume.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    parsed = parse_resume(text)
    skills = parsed.get("skills", [])
    email = parsed.get("email", "unknown@example.com")
    questions = generate_questions(skills)

    db = SessionLocal()
    new_query = ResumeQuery(
        email=email,
        skills=", ".join(skills),
        questions="\n".join(questions)
    )
    db.add(new_query)
    db.commit()
    db.close()

    return {
        "parsed_data": parsed,
        "interview_questions": questions
    }

@app.get("/history/")
def get_history():
    db = SessionLocal()
    entries = db.query(ResumeQuery).order_by(ResumeQuery.timestamp.desc()).all()
    db.close()
    return [
        {
            "email": entry.email,
            "skills": entry.skills,
            "questions": entry.questions,
            "timestamp": entry.timestamp
        }
        for entry in entries
    ]
