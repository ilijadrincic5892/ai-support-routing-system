from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from classifier import classify_message
from logger import route_decision

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request):
    form = await request.form()
    user_message = form.get("message")

    category = classify_message(user_message)
    decision = route_decision(category)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": {
                "message": user_message,
                "category": category,
                "decision": decision
            }
        }
    )
