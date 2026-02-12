from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles

load_dotenv()  # reads .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",response_class=HTMLResponse)
def show_chat(request:Request):
    return templates.TemplateResponse(
        "chat.html",{"request":request}
    )


@app.post("/chat")
async def chat(
    request: Request,
    message: str = Form(...)
):
    print("USER MESSAGE:", message)

    # Fake AI logic (temporary)
    ai_reply = await get_gemini_reply(message)

    return templates.TemplateResponse(
        "chat.html",
        {
            "request": request,
            "user_message": message,
            "ai_reply": ai_reply
        }
    )


import httpx

async def get_gemini_reply(message: str):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        "models/gemini-flash-latest:generateContent"
        f"?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": (
                            "You are a Junior Developer Learning Assistant.\n\n"

                            "Identity:\n"
                            "- You are NOT a general-purpose chatbot\n"
                            "- You exist only to help people learn programming, software, and IT concepts\n\n"

                            "Target audience:\n"
                            "- Assume the user is a beginner by default\n"
                            "- Explain concepts from scratch unless the user asks for an advanced explanation\n"
                            "- Adjust explanation depth if the user explicitly requests it\n\n"

                            "What you CAN do:\n"
                            "- Explain programming concepts clearly\n"
                            "- Explain backend and web development concepts\n"
                            "- Explain FastAPI, Python, APIs, databases, and software basics\n"
                            "- Use simple English, step-by-step explanations, and real-life analogies\n"
                            "- Give small illustrative examples when helpful\n\n"

                            "Strict limitations:\n"
                            "- Do NOT act as a general chatbot\n"
                            "- Do NOT discuss non-technical topics\n"
                            "- Do NOT generate images or claim you can generate images\n"
                            "- If asked for images, clearly say you cannot do that\n"
                            "- Do NOT return JSON, code blocks, tool calls, or internal reasoning\n"
                            "- Do NOT use heavy jargon unless the user asks for it\n\n"

                            "Out-of-scope handling:\n"
                            "- If a user asks something outside programming or software concepts, politely refuse\n"
                            "- Clearly explain that it is outside your role\n"
                            "- Redirect the conversation back to a related technical concept if possible\n\n"

                            f"User question: {message}"
                        )
                    }
                ]
            }
        ]
    }


    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, json=payload)

    data = response.json()
    if "candidates" not in data:
        # Gemini failed — return readable error instead of crashing
        return "AI error: Gemini did not return a valid response."

    return data["candidates"][0]["content"]["parts"][0]["text"]



