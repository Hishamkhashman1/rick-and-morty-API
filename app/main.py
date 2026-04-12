from fastapi import FastAPI
import json
app = FastAPI()

with open("/home/hisham/code/Hishamkhashman1/rick-and-morty-API/data/characters.json", "r") as f:
    data = json.load(f)

@app.get("/")
async dfe root():
    return {"Read the docs and enjoy": "wubalubadubdub"}



@app.get("/characters/{character_id}")
async def get_characters(character_id: int):
    for character in data:
        if character["id"] == character_id:
            return character

@app.get("/characters")
async def get_characters():
    return data
