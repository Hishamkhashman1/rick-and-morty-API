import json
from sqlmodel import Session, create_engine, SQLModel
from app.models import Character
import os
from dotenv import load_dotenv



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def seed_data():
    SQLModel.metadata.create_all(engine)

    with open("/home/hisham/code/Hishamkhashman1/rick-and-morty-API/data/characters.json", "r") as f:
        json_data = json.load(f)

    with Session(engine) as session:
        for character in json_data:
            character = Character(
                    id = character["id"],
                    name = character["name"],
                    status = character["status"],
                    species = character["species"],
                    type = character["type"],
                    gender = character["gender"],
                    place_of_origin = character["place of origin"]
                )
            session.add(character)

        session.commit()
        print("Data moved to Postgres successfully")
if __name__ == "__main__":
    seed_data()
