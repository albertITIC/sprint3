from fastapi import FastAPI, HTTPException, Query, File, UploadFile

import db_assistencia
from typing import List, Optional

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tablaUsuari(BaseModel):
    idUsuari: int
    nomUsuari: str
    cognomUsuari: str
    correuUsuari: str
    contrassenyaUsuari: str
    tipusUsuari: str
    estat: str

class tablaAssistencia(BaseModel):
    idUsuari: int
    estat: str
    hEntrada: str
    hSortida: str
    dia: str

class tablaGrup(BaseModel):
    idGrup: int
    nomGrup: str
    nomClasse: str
    
class tablaClasse(BaseModel):
    idClasse: int
    nomClasse: str
    nomGrup: str
    
class tablaClasse(BaseModel):
    idModul: int
    nomModul: str
    idClasse: str
             
@app.get("/usuaris/{id}", response_model=tablaUsuari)
def read_usuari_id(id: int):
    try:
        # Llama a la función en db_assistencia para obtener datos del usuario
        usuari = db_assistencia.fetch_usuari_by_id(id)

        if usuari is None:
            # Lanzar excepción si no se encuentra el usuario
            raise HTTPException(status_code=404, detail="Usuari no trobat")

        # Retorna el usuario como un modelo Pydantic
        return tablaUsuari(**usuari)

    except Exception as e:
        # Manejo genérico de errores
        raise HTTPException(status_code=500, detail=f"Error intern: {e}")