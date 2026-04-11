from fastapi import FastAPI

app = FastAPI()

@app.get("/characters/character_id")
async def get_characters():
    return {character_id: character_id}




