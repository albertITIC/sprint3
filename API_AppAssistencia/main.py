from fastapi import FastAPI, HTTPException, Query
import db_assistencia
from typing import List, Optional

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tablaUsuari(BaseModel):
    nuid: int # -> el que identifica la targeta que rebem AWS
    idUsuari: int
    nomUsuari: str
    cognomUsuari: str
    correuUsuari: str
    contrassenyaUsuari: str
    tipusUsuari: str
    estat: str

@app.get("/usuaris/{id}", response_model=tablaUsuari)
def read_usuari_id(id:int):
    if db_assistencia.read_id(id) is not None:
        usuari = tablaUsuari(db_assistencia.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return usuari