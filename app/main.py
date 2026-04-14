from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select
from app.models import Character

import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

app = FastAPI()


@app.get("/")
async def root():
    return [{"Read the docs and enjoy": "wubalubadubdub"}, {"Get all the characters": "/characters"}]



@app.get("/characters/{character_id}")
async def get_character(character_id: int):
    with Session(engine) as session:
        character = session.exec(select(Character).where(Character.id == character_id)).first()
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.get("/characters")
async def list_characters():
    with Session(engine) as session:
        characters = session.exec(select(Character)).all()
    return characters
