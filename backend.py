from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fuzzywuzzy import fuzz
import random
import json

# Initialize FastAPI app
app = FastAPI()

# Setup for templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load knowledge base
with open("chama_data.json", "r") as f:
    knowledge_base = json.load(f)

# Load quotes
with open("quotes.json", "r") as f:
    quotes = json.load(f)

# Route: Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Model for incoming user message
class QueryRequest(BaseModel):
    query: str

# Route: Chatbot API endpoint
@app.post("/chat")
async def chat_endpoint(query: QueryRequest):
    user_query = query.query.lower()

    best_score = 0
    best_answer = None

    for qa in knowledge_base:
        score = fuzz.partial_ratio(user_query, qa["question"].lower())
        if score > best_score:
            best_score = score
            best_answer = qa["answer"]

    if best_score >= 60:
        return {"response": best_answer}
    else:
        return {"response": "Sorry, I don't have an answer for that. Try rephrasing!"}

# Route: Random quote API
@app.get("/quote")
async def quote_endpoint():
    return {"quote": random.choice(quotes)}
