# Rick and Morty API (MVP)

A reliable, deployed FastAPI MVP that serves Rick and Morty character data from a Postgres database.

## What This MVP Does

- Serves character data over a clean JSON API
- Supports listing all characters
- Supports fetching a single character by ID

## API Endpoints

- `GET /characters`
- `GET /characters/{character_id}`

## How to Use (End Users)

You can call the API directly over HTTPS. No auth required.

Swagger UI:
https://rick-and-morty-api-9871cc72.fastapicloud.dev/docs

### cURL

```bash
curl https://rick-and-morty-api-9871cc72.fastapicloud.dev/characters
```

```bash
curl https://rick-and-morty-api-9871cc72.fastapicloud.dev/characters/1
```

### JavaScript (fetch)

```js
const res = await fetch("https://rick-and-morty-api-9871cc72.fastapicloud.dev/characters/1");
const data = await res.json();
console.log(data);
```

### Python (requests)

```python
import requests

res = requests.get("https://rick-and-morty-api-9871cc72.fastapicloud.dev/characters/1")
print(res.json())
```

## Example Response

```bash
curl https://rick-and-morty-api-9871cc72.fastapicloud.dev/characters/1
```

Response:

```json
{
  "id": 1,
  "name": "Rick Sanchez",
  "status": "Alive",
  "species": "Human",
  "type": "Legendary",
  "gender": "Male",
  "place_of_origin": "Earth (C-137)"
}
```

## Tech Stack

- FastAPI
- SQLModel
- Uvicorn
- Postgres
- FastAPI Cloud

## Roadmap

- Pagination and filtering
- More resources (episodes, locations)
- Better error handling and validation

## Contact

Hisham Khashman
hisham.khashman@gmail.com
https://www.hishamkhashman.dev
