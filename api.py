from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.generators.content_generator import generar_contenido

app = FastAPI(title="MultiversoApp API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerarRequest(BaseModel):
    plataforma: str
    modelo: str
    audiencia: str
    idioma: str
    tono: str
    tema: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generar")
def generar(req: GenerarRequest):
    try:
        contenido = generar_contenido(
            tema=req.tema,
            plataforma=req.plataforma,
            audiencia=req.audiencia,
            tono=req.tono,
            nombre_modelo=req.modelo,
            idioma=req.idioma,
        )
        return {"contenido": contenido}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
