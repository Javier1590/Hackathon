from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Paciente, Especialidad, Medico, Cita, Historial

# Formulario personalizado para Paciente 
class PacienteCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Paciente
        fields = ('email', 'cedula', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'telefono', 'foto_cedula_url')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Configuración personalizada para Paciente
class PacienteAdmin(UserAdmin):
    add_form = PacienteCreationForm
    form = PacienteCreationForm
    list_display = ('email', 'cedula', 'nombre_1', 'apellido_1', 'telefono', 'rol', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_active')
    search_fields = ('email', 'cedula', 'nombre_1', 'apellido_1')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('cedula', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'telefono', 'foto_cedula_url')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'rol', 'groups', 'user_permissions')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'cedula', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'telefono', 'foto_cedula_url', 'password1', 'password2'),
        }),
    )
    exclude = ('username',)

# Configuración para Especialidad
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created_at')
    search_fields = ('nombre',)
    ordering = ('nombre',)

# Configuración para Medico
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_1', 'apellido_1', 'email', 'especialidad', 'disponible', 'created_at')
    list_filter = ('especialidad', 'disponible')
    search_fields = ('email', 'cedula', 'nombre_1')
    ordering = ('nombre_1',)

# Configuración para Cita
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'fecha_cita', 'hora_cita', 'estado_cita', 'codigo_cita', 'created_at')
    list_filter = ('estado_cita', 'fecha_cita', 'medico__especialidad')
    search_fields = ('paciente__email', 'medico__nombre_1', 'codigo_cita')
    ordering = ('fecha_cita',)

# Configuración para Historial
@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('cita', 'medico_actualizacion', 'fecha_actualizacion', 'created_at')
    list_filter = ('medico_actualizacion', 'fecha_actualizacion')
    search_fields = ('cita__codigo_cita', 'notas_medico')
    ordering = ('fecha_actualizacion',)

# Registra los modelos
admin.site.register(Paciente, PacienteAdmin)