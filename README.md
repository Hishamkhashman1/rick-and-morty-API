#  Rick and Morty API

A simple FastAPI-based API that provides information about characters from the show *Rick and Morty*.

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Hishamkhashman1/rick-and-morty-API.git
cd rick-and-morty-API
```

### 2. Install dependencies

Since this project uses `pyproject.toml`:

```bash
pip install .
```

---

### 3. Run the API

```bash
uvicorn app.main:app --reload
```

---

## 📡 Usage

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

This gives you interactive Swagger UI.

---

## 📚 Endpoints

### Get all characters

```
GET /characters
```

### Get character by ID

```
GET /characters/{character_id}
```

---

## 🧠 Example

```bash
curl http://127.0.0.1:8000/characters/1
```

Response:

```json
{
  "id": 1,
  "name": "Rick Sanchez",
  "status": "Alive",
  "species": "Human",
  "gender": "Male"
}
```

---

## 🛠 Tech Stack

* FastAPI
* Uvicorn
* Python 3.8+

---

## 📌 Notes

* This is an MVP project focused on learning backend fundamentals.
* Data is currently served from a local JSON file.
* Future improvements will include filtering, pagination, additional resources, and deployment as a publicly accessible API.

---

## 📫 Contact

Hisham Khashman
📧 [hisham.khashman@gmail.com](mailto:hisham.khashman@gmail.com)
🌐 https://www.hishamkhashman.dev
  
    
    
