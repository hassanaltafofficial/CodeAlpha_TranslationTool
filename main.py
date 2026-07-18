from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deep_translator import GoogleTranslator

# App initialization
app = FastAPI(title="Language Translation API")

# CORS setup for scalable frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data structure validation
class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "auto"
    target_lang: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        translator = GoogleTranslator(source=request.source_lang, target=request.target_lang)
        translated_text = translator.translate(request.text)
        
        return {
            "status": "success",
            "original_text": request.text,
            "translated_text": translated_text,
            "target_language": request.target_lang
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.get("/languages")
async def get_supported_languages():
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    return {"languages": langs_dict}