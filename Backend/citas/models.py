from django.db import models
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom User Manager para Paciente
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, cedula, nombre_1, apellido_1, telefono, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            cedula=cedula,
            nombre_1=nombre_1,
            apellido_1=apellido_1,
            telefono=telefono,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, cedula, nombre_1, apellido_1, telefono, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, cedula, nombre_1, apellido_1, telefono, **extra_fields)

# Modelo Paciente (usuarios)
class Paciente(AbstractBaseUser, PermissionsMixin):
    cedula = models.CharField(max_length=20, unique=True)
    nombre_1 = models.CharField(max_length=50)
    nombre_2 = models.CharField(max_length=50, blank=True, null=True)
    apellido_1 = models.CharField(max_length=50)
    apellido_2 = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=True)
    foto_cedula_url = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=[('paciente', 'Paciente'), ('admin', 'Admin')], default='paciente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["cedula", "nombre_1", "apellido_1", "telefono"]

    def __str__(self):
        return f"{self.nombre_1} {self.apellido_1}"

# Modelo Especialidad
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Modelo Medico
class Medico(models.Model):
    numero_inss = models.CharField(max_length=15, unique=True)
    cedula = models.CharField(max_length=15, unique=True)
    nombre_1 = models.CharField(max_length=50)
    nombre_2 = models.CharField(max_length=50, blank=True, null=True)
    apellido_1 = models.CharField(max_length=50)
    apellido_2 = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name="medicos")
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr/a. {self.nombre_1} {self.apellido_1}"
# Modelo Cita
class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    comentarios = models.TextField(blank=True, null=True)
    estado_cita = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    codigo_cita = models.CharField(max_length=20, unique=True, default=uuid.uuid4().hex[:20])  
    codigo_historial = models.CharField(max_length=20, unique=True, default=uuid.uuid4().hex[:20])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita {self.id} - {self.paciente} con {self.medico}"

# Modelo Historial
class Historial(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    notas_medico = models.TextField(blank=True, null=True)
    resultados_examenes = models.TextField(blank=True, null=True)
    prescripcion_medica = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    medico_actualizacion = models.ForeignKey(Medico, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.cita}"