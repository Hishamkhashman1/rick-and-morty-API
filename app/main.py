from fastapi import FastAPI
import json
app = FastAPI()

with open("/home/hisham/code/Hishamkhashman1/rick-and-morty-API/data/characters.json", "r") as f:
    data = json.load(f)

@app.get("/characters/character_id")
async def get_characters():
    return {character_id: character_id}




