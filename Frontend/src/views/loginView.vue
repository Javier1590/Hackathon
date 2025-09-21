<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const tab = ref("login");
const router = useRouter();

const iniciarSesionLogin = (e) => {
  e.preventDefault();
  // 🚀 Aquí puedes usar fetch o axios para validar en backend
  // por ahora, solo redirigimos
  router.push("/dashboard");
};

const iniciarSesionRegister = (e) => {
  e.preventDefault();
  // 🚀 Aquí igual mandarás datos al backend
  router.push("/dashboard");
};
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-100 p-6">
    <div class="w-full max-w-2xl rounded-2xl bg-white shadow-xl p-8">
      <!-- Tabs -->
      <div class="flex border-b mb-6">
        <button
          @click="tab = 'login'"
          :class="[
            'w-1/2 py-2 text-center font-semibold',
            tab === 'login'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-500'
          ]"
        >
          Usuario existente
        </button>
        <button
          @click="tab = 'register'"
          :class="[
            'w-1/2 py-2 text-center font-semibold',
            tab === 'register'
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-500'
          ]"
        >
          Usuario nuevo
        </button>
      </div>

      <!-- Usuario existente -->
      <form v-if="tab === 'login'" class="space-y-4" @submit="iniciarSesionLogin">
        <div>
          <label class="block text-sm font-medium">Correo</label>
          <input
            type="email"
            placeholder="ejemplo@correo.com"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2 focus:ring focus:ring-blue-200"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">Contraseña</label>
          <input
            type="password"
            placeholder="********"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2 focus:ring focus:ring-blue-200"
          />
        </div>
        <button
          type="submit"
          class="w-full rounded-lg  py-2 text-white font-semibold btn-primary"
        >
          Iniciar sesión
        </button>
      </form>

      <!-- Usuario nuevo -->
      <form v-else class="grid grid-cols-2 gap-4" @submit="iniciarSesionRegister">
        <div class="col-span-2">
          <label class="block text-sm font-medium">Cédula</label>
          <input
            type="text"
            placeholder="Número de cédula"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">Nombre 1</label>
          <input
            type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">Nombre 2</label>
          <input
            type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">Apellido 1</label>
          <input
            type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">Apellido 2</label>
          <input
            type="text"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div class="col-span-2">
          <label class="block text-sm font-medium">Teléfono</label>
          <input
            type="tel"
            placeholder="(505) 8888-8888"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div class="col-span-2">
          <label class="block text-sm font-medium">Correo</label>
          <input
            type="email"
            placeholder="ejemplo@correo.com"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div class="col-span-2">
          <label class="block text-sm font-medium">Contraseña</label>
          <input
            type="password"
            placeholder="********"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div class="col-span-2">
          <label class="block text-sm font-medium">Foto de cédula</label>
          <input
            type="file"
            accept="image/*"
            class="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2"
          />
        </div>
        <div class="col-span-2">
          <button
            type="submit"
            class="w-full rounded-lg py-2 font-semibold text-white btn-primary"
          >
            Registrarse
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
