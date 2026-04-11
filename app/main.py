from fastapi import FastAPI
import json
app = FastAPI()

with open("/home/hisham/code/Hishamkhashman1/rick-and-morty-API/data/characters.json", "r") as f:
    data = json.load(f)

@app.get("/characters/{character_id}")
async def get_characters(character_id: int):
    for character in data:
        if character["id"] == character_id:
            return character


from fastapi import FastAPI
from fastapi import FastAPI
import json
app = FastAPI()

with open("/home/hisham/code/Hishamkhashman1/rick-and-morty-API/data/characters.json", "r") as f:
    data = json.load(f)

@app.get("/characters/{character_id}")
async def get_characters(character_id: int):
    return {character_id: character_id}



@app.get("/characters")
async def get_characters():
    return data





