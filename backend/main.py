from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL del frontend Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos de ejemplo
users = [
    {
        "id": 1,
        "name": "Vicent",
        "surname": "Foo",
        "email": "vicent@example.com"
    },
    {
        "id": 2,
        "name": "María",
        "surname": "García",
        "email": "maria.garcia@example.com"
    },
    {
        "id": 3,
        "name": "Juan",
        "surname": "Pérez",
        "email": "juan.perez@example.com"
    },
    {
        "id": 4,
        "name": "Ana",
        "surname": "Martínez",
        "email": "ana.martinez@example.com"
    }
]

@app.get("/")
def read_root():
    return {"message": "API de Usuarios - Backend en Python"}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}, 404
