from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Paciente

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Correo o contraseña incorrectos.")
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        cedula = request.POST["cedula"]
        nombre_1 = request.POST["nombre_1"]
        apellido_1 = request.POST["apellido_1"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        password = request.POST["password"]

        if Paciente.objects.filter(cedula=cedula).exists():
            messages.error(request, "Cédula ya registrada.")
            return redirect("register")
        if Paciente.objects.filter(email=email).exists():
            messages.error(request, "Correo ya registrado.")
            return redirect("register")

        Paciente.objects.create_user(email=email, password=password, cedula=cedula, nombre_1=nombre_1, apellido_1=apellido_1, telefono=telefono)
        messages.success(request, "Registro exitoso. Inicia sesión.")
        return redirect("login")
    return render(request, "register.html")

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "dashboard.html")

def agendar_cita_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        # Lógica para guardar cita (pendiente de implementación)
        pass
    return render(request, "agendar_cita.html")