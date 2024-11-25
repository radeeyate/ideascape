import secrets
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ideas import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request})


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


@app.get("/python")
async def python(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Python"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "python",
            "lang": "Python",
            "idea": idea,
        },
    )


@app.get("/cpp")
async def cpp(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "C++"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "c++",
            "lang": "C++",
            "idea": idea,
        },
    )


@app.get("/javascript")
async def javascript(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "JavaScript"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "javascript",
            "lang": "JavaScript",
            "idea": idea,
        },
    )


@app.get("/rust")
async def rust(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Rust"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "rust",
            "lang": "Rust",
            "idea": idea,
        },
    )


@app.get("/lua")
async def lua(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Lua"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "lua",
            "lang": "Lua",
            "idea": idea,
        },
    )


@app.get("/java")
async def java(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Java"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "java",
            "lang": "Java",
            "idea": idea,
        },
    )


@app.get("/swift")
async def swift(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Swift"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "swift",
            "lang": "Swift",
            "idea": idea,
        },
    )


@app.get("/ruby")
async def ruby(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Ruby"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "ruby",
            "lang": "Ruby",
            "idea": idea,
        },
    )


@app.get("/php")
async def php(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "PHP"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "php",
            "lang": "PHP",
            "idea": idea,
        },
    )


@app.get("/typescript")
async def typescript(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "TypeScript"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "typescript",
            "lang": "TypeScript",
            "idea": idea,
        },
    )


@app.get("/kotlin")
async def kotlin(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "Kotlin"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "kotlin",
            "lang": "Kotlin",
            "idea": idea,
        },
    )


@app.get("/csharp")
async def csharp(request: Request):
    idea = secrets.choice(
        [idea["idea"] for idea in projectsList if idea["lang"] == "C#"]
    )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "category": "c#",
            "lang": "C#",
            "idea": idea,
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
