from cmath import e

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import engine, get_db

router = APIRouter()

class Livro(BaseModel):
    id: int | None = None
    titulo: str
    autor: str
    ano: int

    class Config:
        schema_extra = {
                "example": {
                    "titulo": "Titulo",
                    "autor": "Autor",
                    "ano": 2022
                    }
                }   




models.Base.metadata.create_all(bind = engine)

@router.get("/book/", tags = ["Book"])
def get_book(db: Session = Depends(get_db)):
    all_data = db.query(models.Book).all()
    if(all_data != []):
        all_data_json = jsonable_encoder(all_data)
        return JSONResponse(status_code = status.HTTP_201_CREATED, content = {
                "message": "dados buscados com sucesso",
                "error": None,
                "data": all_data_json,
            })

    else:
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, content = {
            "message": "dados não encontrados",
            "error": str(e),
            "data": None,
        })

@router.post("/book/", tags = ["Book"])
def post_book(data: Livro, db: Session = Depends(get_db)):
    try:
        new_object = models.Book(**data.dict())
        db.add(new_object)
        db.commit()
        db.refresh(new_object)

        new_object_json = jsonable_encoder(new_object)

        return JSONResponse(status_code = status.HTTP_201_CREATED, content = {
            "message": "Dados cadastrados com sucesso",
            "error": None,
            "data": new_object_json,
            }, headers = {"content-type": "application/json"})
    except Exception as e:
        return JSONResponse(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, content = {
            "message": "Erro ao obter dados",
            "error": str(e),
            "data": None,
        })

