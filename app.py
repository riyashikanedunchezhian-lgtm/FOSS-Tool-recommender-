from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from database import collection
from recommender import recommend_tool

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")

# Static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Input model
class UserInput(BaseModel):
    genre: str
    difficulty: str


#  Landing Page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Tool Page
@app.get("/tool", response_class=HTMLResponse)
def tool_page(request: Request):
    return templates.TemplateResponse("tool.html", {"request": request})

@app.get("/genres")
def get_genres():
    genres = collection.distinct("genre")
    return {"genres": genres}

# Recommendation API
@app.post("/recommend")
def recommend(user: UserInput):

    result = recommend_tool(
        collection,
        user.genre,
        user.difficulty
    )

    if "error" in result:
        return result

    return {
        "tool_name": result["tool_name"],
        "description": result["description"],
        "website": result["website"]
    }