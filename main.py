import secrets
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ideas import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    idea = secrets.choice(projectsList)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "programming",
            "lang": idea["lang"],
            "idea": idea["idea"],
        },
    )

@app.get("/writing")
async def writing(request: Request):
    idea = secrets.choice(writingIdeas)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "writing",
            "genre": idea["genre"],
            "idea": idea["prompt"],
        },
    )


@app.get("/hackathon")
async def writing(request: Request):
    idea = secrets.choice(hackathonProjects)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "hackathon",
            "sector": idea["category"],
            "idea": idea["idea"],
        },
    )


@app.get("/music")
async def music(request: Request):
    idea = secrets.choice(musicPrompts)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "music",
            "genre": idea["genre"],
            "idea": idea["idea"],
        },
    )


@app.get("/art")
async def art(request: Request):
    idea = secrets.choice(artIdeas)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "art",
            "medium": idea["medium"],
            "idea": idea["idea"],
        },
    )


@app.get("/design")
async def design(request: Request):
    idea = secrets.choice(designIdeas)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "design",
            "sector": idea["category"],
            "idea": idea["idea"],
        },
    )


@app.get("/photography")
async def design(request: Request):
    idea = secrets.choice(photographyIdeas)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "photography",
            "genre": idea["genre"],
            "idea": idea["idea"],
        },
    )


@app.get("/film")
async def design(request: Request):
    idea = secrets.choice(filmIdeas)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "film",
            "genre": idea["genre"],
            "idea": idea["idea"],
        },
    )
