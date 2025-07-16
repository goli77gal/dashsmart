from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai, os

router = APIRouter()

openai.api_key = os.getenv("OPENAI_API_KEY")

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class TranslationResponse(BaseModel):
    translated_text: str

@router.post("/", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    prompt = f"Translate this to {request.target_language}: {request.text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip()
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
