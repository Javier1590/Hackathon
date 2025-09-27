import os
import sys
from datetime import datetime, timedelta

# Añade el directorio padre al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import django
from asgiref.sync import sync_to_async

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Backend.settings")
django.setup()

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import EmailStr
import jwt
from citas.models import Paciente, Especialidad, Medico
from django.contrib.auth.hashers import make_password, check_password

app = FastAPI()

# Configura CORS para permitir el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Puerto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clave secreta para JWT (debería estar en settings.py en producción)
SECRET_KEY = "nd*t&i9ntp%2@4i33@0e&k17dp=66vne)9(4ico-tt1o7nbg)4"  # Cámbiala en producción

@app.post("/api/pacientes/register")
async def register_paciente(
    cedula: str = Form(...),
    nombre1: str = Form(...),
    nombre2: str = Form(None),
    apellido1: str = Form(...),
    apellido2: str = Form(None),
    telefono: str = Form(...),
    correo: EmailStr = Form(...),
    contrasena: str = Form(...),
    foto: UploadFile = File(None)
):
    cedula_exists = await sync_to_async(Paciente.objects.filter(cedula=cedula).exists)()
    if cedula_exists:
        raise HTTPException(status_code=400, detail="Cédula ya registrada")
    email_exists = await sync_to_async(Paciente.objects.filter(email=correo).exists)()
    if email_exists:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    paciente = await sync_to_async(Paciente.objects.create_user)(
        email=correo,
        password=make_password(contrasena),
        cedula=cedula,
        nombre_1=nombre1,
        nombre_2=nombre2,
        apellido_1=apellido1,
        apellido_2=apellido2,
        telefono=telefono,
        rol="paciente"
    )

    if foto:
        paciente.foto_cedula_url = f"uploads/{foto.filename}"
        with open(paciente.foto_cedula_url, "wb") as buffer:
            buffer.write(await foto.read())
        await sync_to_async(paciente.save)()

    return {"message": "Paciente registrado", "id": paciente.id}

@app.post("/api/pacientes/login")
async def login_paciente(correo: EmailStr = Form(...), contrasena: str = Form(...)):
    paciente = await sync_to_async(Paciente.objects.get)(email=correo)
    if not await sync_to_async(check_password)(contrasena, paciente.password):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    payload = {
        "sub": str(paciente.id),
        "email": paciente.email,
        "rol": paciente.rol,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return {"message": "Login exitoso", "token": token, "id": paciente.id}

@app.get("/api/Especialidads")
async def get_especialidades():
    especialidades = await sync_to_async(list)(Especialidad.objects.all().values("nombre"))
    return {"especialidades": especialidades}

@app.get("/api/Medicos")
async def get_medicos():
    medicos = await sync_to_async(list)(Medico.objects.all().values())
    print(medicos)
    return {"medicos": medicos}
