from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",  
    "http://localhost:3000",
    "https://testapimanu.pages.dev"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos
datos = [
    {"id": 1, "nombre": "EL PONCHO", "edad": 25, "pais": "GUACOCHE", "image": "https://www.sena.edu.co/Style%20Library/alayout/images/logoSena.png"},
    {"id": 2, "nombre": "EL PEPO", "edad": 30, "pais": "EL TOTUMO", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 3, "nombre": "EL MENBER", "edad": 22, "pais": "TOCAINA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 4, "nombre": "LA MARIA", "edad": 28, "pais": "MOROCHOA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 5, "nombre": "LUCHO", "edad": 35, "pais": "LA PAZ", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 6, "nombre": "Sofía", "edad": 27, "pais": "LA NEVADA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 7, "nombre": "Pedro", "edad": 40, "pais": "LOS HATICOS", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 8, "nombre": "Lucía", "edad": 19, "pais": "SOLONDRIA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 9, "nombre": "Carlos", "edad": 33, "pais": "VALLEDUPAR", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 10, "nombre": "Ana", "edad": 24, "pais": "BARRANQUILLA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 11, "nombre": "Manuel", "edad": 29, "pais": "CARTAGENA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 12, "nombre": "Marta", "edad": 31, "pais": "SANTA MARTA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 13, "nombre": "Luis", "edad": 45, "pais": "RIOHACHA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 14, "nombre": "Camila", "edad": 26, "pais": "MAICAO", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 15, "nombre": "Andrés", "edad": 38, "pais": "FONSECA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 16, "nombre": "Paula", "edad": 21, "pais": "SAN JUAN", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 17, "nombre": "Diego", "edad": 34, "pais": "VILLANUEVA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 18, "nombre": "Valentina", "edad": 23, "pais": "URUMITA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 19, "nombre": "Fernando", "edad": 41, "pais": "DIBULLA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 20, "nombre": "Daniela", "edad": 28, "pais": "ALBANIA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 21, "nombre": "Ricardo", "edad": 36, "pais": "HATONUEVO", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 22, "nombre": "Natalia", "edad": 27, "pais": "BOSCONIA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 23, "nombre": "Héctor", "edad": 39, "pais": "AGUACHICA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 24, "nombre": "Laura", "edad": 22, "pais": "CODAZZI", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"},
    {"id": 25, "nombre": "Oscar", "edad": 44, "pais": "CHIRIGUANA", "image": "https://pixabay.com/es/vectors/camafeo-mujer-ni%c3%b1a-perfil-silueta-2023867/"}
]

@app.get("/")
def get_datos():
    return {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "total": len(datos),
        "datos": datos
    }

# handler para serverless
handler = Mangum(app)