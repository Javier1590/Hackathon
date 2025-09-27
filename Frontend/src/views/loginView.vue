<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const tab = ref("login");
const router = useRouter();

const emailLogin = ref("");
const passwordLogin = ref("");
const registroData = ref({
  cedula: "",
  nombre1: "",
  nombre2: "",
  apellido1: "",
  apellido2: "",
  telefono: "",
  correo: "",
  contrasena: "",
  foto: null,
});

const iniciarSesionLogin = async (e) => {
  e.preventDefault();
  try {
    const response = await fetch("http://localhost:8001/api/pacientes/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        correo: emailLogin.value,
        contrasena: passwordLogin.value,
      }).toString(),
    });
    const data = await response.json();
    if (response.ok) {
      // Almacenar token (simplificado; usa localStorage o Vuex en producción)
      localStorage.setItem("token", data.token);
      localStorage.setItem("userId", data.id);
      alert("Login exitoso!");
      router.push("/dashboard");
    } else {
      alert(`Error: ${data.detail || "Intenta de nuevo"}`);
    }
  } catch (error) {
    alert("Error de conexión. Verifica el backend.");
    console.error(error);
  }
};

const iniciarSesionRegister = async (e) => {
  e.preventDefault();
  const formData = new FormData();
  formData.append("cedula", registroData.value.cedula);
  formData.append("nombre1", registroData.value.nombre1);
  formData.append("nombre2", registroData.value.nombre2 || "");
  formData.append("apellido1", registroData.value.apellido1);
  formData.append("apellido2", registroData.value.apellido2 || "");
  formData.append("telefono", registroData.value.telefono);
  formData.append("correo", registroData.value.correo);
  formData.append("contrasena", registroData.value.contrasena);
  if (registroData.value.foto) {
    formData.append("foto", registroData.value.foto);
  }

  try {
    const response = await fetch("http://localhost:8001/api/pacientes/register", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    if (response.ok) {
      alert("Paciente registrado con éxito!");
      router.push("/dashboard");
    } else {
      alert(`Error: ${data.detail || "Intenta de nuevo"}`);
    }
  } catch (error) {
    alert("Error de conexión. Verifica el backend.");
    console.error(error);
  }
};
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-100 p-6 cont-login">
    <div class="w-full max-w-2xl rounded-2xl bg-white shadow-xl p-8">
      <!-- Tabs -->
      <div class="flex border-b mb-6">
        <button @click="tab = 'login'" :class="[
          'w-1/2 py-2 text-center font-semibold',
          tab === 'login'
            ? 'border-b-2 border-blue-600 text-blue-600'
            : 'text-gray-500'
        ]">
          Usuario existente
        </button>
        <button @click="tab = 'register'" :class="[
          'w-1/2 py-2 text-center font-semibold',
          tab === 'register'
            ? 'border-b-2 border-blue-600 text-blue-600'
            : 'text-gray-500'
        ]">
          Usuario nuevo
        </button>
      </div>

      <!-- Usuario existente -->
      <form v-if="tab === 'login'" class="space-y-4" @submit="iniciarSesionLogin">
        <div>
          <label class="block text-sm font-medium text-gray-700">Correo</label>
          <input v-model="emailLogin" type="email" placeholder="ejemplo@correo.com" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2 focus:ring-2 focus:ring-blue-200"
            aria-label="Correo electrónico" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Contraseña</label>
          <input v-model="passwordLogin" type="password" placeholder="********" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2 focus:ring-2 focus:ring-blue-200"
            aria-label="Contraseña" />
        </div>
        <button type="submit"
          class="w-full rounded-lg bg-[#004AAD] py-2 text-white font-semibold hover:bg-blue-700 transition">
          Iniciar sesión
        </button>
      </form>

      <!-- Usuario nuevo -->
      <form v-else class="grid grid-cols-1 gap-4 sm:grid-cols-2" @submit="iniciarSesionRegister">
        <div class="col-span-1 sm:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Cédula</label>
          <input v-model="registroData.cedula" type="text" placeholder="Número de cédula" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Nombre 1</label>
          <input v-model="registroData.nombre1" type="text" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Nombre 2</label>
          <input v-model="registroData.nombre2" type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Apellido 1</label>
          <input v-model="registroData.apellido1" type="text" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Apellido 2</label>
          <input v-model="registroData.apellido2" type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div class="col-span-1 sm:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Teléfono</label>
          <input v-model="registroData.telefono" type="tel" placeholder="(505) 8888-8888" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div class="col-span-1 sm:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Correo</label>
          <input v-model="registroData.correo" type="email" placeholder="ejemplo@correo.com" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div class="col-span-1 sm:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Contraseña</label>
          <input v-model="registroData.contrasena" type="password" placeholder="********" required
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div class="col-span-1 sm:col-span-2">
          <label class="block text-sm font-medium text-gray-700">Foto de cédula (opcional)</label>
          <input @change="registroData.foto = $event.target.files[0]" type="file" accept="image/*"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2" />
        </div>
        <div class="col-span-1 sm:col-span-2">
          <button type="submit"
            class="w-full rounded-lg bg-[#004AAD] py-2 text-white font-semibold hover:bg-blue-700 transition">
            Registrarse
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.cont-login {
  min-height: 100vh;
  padding-bottom: 60px;
}

.max-w-md {
  max-width: 100%;
}

@media (min-width: 640px) {
  .max-w-md {
    max-width: 28rem;
  }

  .sm:p-8 {
    padding: 2rem;
  }

  .sm:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .max-w-md {
    max-width: 30rem;
  }
}
</style>