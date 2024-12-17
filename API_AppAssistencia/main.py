from fastapi import FastAPI, HTTPException, Query
import db_assistencia
from typing import List, Optional
import assistencia
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
    nuid: int

@app.get("/")
def read_root():
    return {"Assistències API"}

@app.get("/usuaris/{id}", response_model=tablaUsuari)
def read_usuari_id(id:int):
    if db_assistencia.fetch_usuari_by_id(id) is not None:
        tablaUsuari = assistencia.usuari_schema(db_assistencia.fetch_usuari_by_id(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return tablaUsuari

@app.get("/marcatge/{id}")
def read_marcatges(id:int):
    if db_assistencia.fetch_usuari_marcatge(id) is not None:
        marcatge = assistencia.usuari_schema(db_assistencia.fetch_usuari_marcatge(id))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return marcatge