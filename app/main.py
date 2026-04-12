from fastapi import FastAPI
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
    return {"Read the docs and enjoy": "wubalubadubdub"}



@app.get("/characters/{character_id}")
async def get_characters(character_id: int):
    with session(engine) as session:
        character = session.exec(select(Character).where(Character.id == character_id)).one()
    return character

@app.get("/characters")
async def get_characters():
    with Session(engine) as session:
        characters = session.exec(select(Character)).all()
    return characters
