<template>
  <div class="min-h-screen bg-gray-100 font-sans relative cont-principal">
    <!-- Encabezado Fijo -->
    <header class="fixed top-0 left-0 right-0 bg-white shadow-md z-10">
      <div class="container mx-auto px-4 py-3 flex items-center justify-between">
        <!-- Logo -->
        <div class="flex items-center lg:start-0">
          <img src="../assets/Logo Full Color.png" alt="Logo" class="w-auto h-16" />
        </div>
        <!-- Barra de búsqueda -->
        <div class="flex-1 mx-4 max-w-md">
          <input type="text" placeholder="Buscar médicos o especialidades..."
            class="w-full px-4 py-2 rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Buscar médicos o especialidades" />
        </div>
        <!-- Íconos de usuario -->
        <div class="flex items-center space-x-4">
          <button aria-label="Próximas Citas" @click="mostrarCitas = true">
            <svg class="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </button>
          <button aria-label="Notificaciones">
            <svg class="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
          </button>
          <button aria-label="Ajustes">
            <svg class="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37a1.724 1.724 0 002.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </button>
        </div>
      </div>
    </header>

    <main class="container px-4 pt-25 flex flex-col lg:flex-row gap-6">
      <!-- Sidebar Izquierda: Especialidades Médicas (fija/sticky) -->
      <aside class="lg:sticky lg:top-20 lg:start w-full lg:w-80 cont-especialidades h-dvh">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Especialidades</h2>
        <div class="space-y-4">
          <button v-for="especialidad in especialidades" :key="especialidad.nombre"
            class="flex items-center p-4 rounded-lg shadow hover:shadow-lg transition w-full btn-spe"
            @click="abrirMedicosEspecialidad(especialidad.nombre)"
            :aria-label="'Ver médicos de ' + especialidad.nombre">
            <svg class="w-8 h-8 text-black mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                :d="especialidad.icono || 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z'" />
            </svg>
            <span class="text-lg font-medium">{{ especialidad.nombre }}</span>
          </button>
        </div>
      </aside>

      <!-- Contenido Dinámico dentro de main -->
      <section class="flex-1">
        <div v-if="mostrarMedicos" class="p-6 bg-white rounded-lg shadow">
          <h2 class="text-2xl font-bold text-gray-900 mb-6 text-center border-b-2 border-blue-200 pb-2">Médicos en {{ especialidadSeleccionada }}</h2>
          <div v-if="medicos.length" class="space-y-4 max-h-[70vh] overflow-y-auto pr-2">
            <div v-for="medico in medicos.filter(m => m.especialidad === especialidadSeleccionada)" :key="medico.id"
              class="p-4 bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-md hover:shadow-lg transition">
              <h3 class="text-lg font-semibold text-gray-800">{{ medico.nombre }}</h3>
              <p class="text-gray-600">{{ medico.especialidad }}</p>
              <p class="text-gray-600" :class="medico.disponible ? 'text-green-600' : 'text-red-600'">
                {{ medico.disponible ? 'Disponible' : 'No Disponible' }}</p>
              <button v-if="medico.disponible" @click="abrirFormularioAgenda(medico)"
                class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition">Agendar Cita</button>
            </div>
          </div>
          <div v-else class="text-gray-500 text-center py-4">No hay médicos disponibles en esta especialidad.</div>
        </div>
        <div v-if="mostrarFormularioAgenda" class="p-6 bg-white rounded-lg shadow">
          <h2 class="text-2xl font-bold text-gray-900 mb-6 text-center border-b-2 border-blue-200 pb-2">Agendar Cita con
            {{ medicoSeleccionado.nombre }}</h2>
          <form @submit.prevent="agendarCita">
            <div class="mb-4">
              <label class="block text-gray-700 mb-2">Código de Cita (Auto-generado)</label>
              <input type="text" :value="nuevaCita.codigoCita" disabled
                class="w-full px-4 py-2 border rounded-lg bg-gray-100" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 mb-2">Código de Historial Médico</label>
              <input type="text" class="w-full px-4 py-2 border rounded-lg bg-gray-100" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 mb-2">Nombre y Apellido del Paciente</label>
              <input type="text" class="w-full px-4 py-2 border rounded-lg bg-gray-100" />
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 mb-2">Motivo de la Cita</label>
              <textarea v-model="nuevaCita.motivo" class="w-full px-4 py-2 border rounded-lg" rows="4"
                required></textarea>
            </div>
            <div class="flex justify-between gap-2">
              <button type="submit"
                class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition flex-1">Agendar</button>
              <button @click="mostrarFormularioAgenda = false"
                class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition flex-1">Cancelar</button>
            </div>
          </form>
        </div>
        <div v-if="!mostrarMedicos && !mostrarFormularioAgenda"
          class="p-6 bg-white rounded-lg shadow text-gray-600 text-center">
          Aquí puedes agregar más contenido como resumen de salud o noticias.
        </div>
      </section>
    </main>

    <!-- Modal para Próximas Citas -->
    <div v-if="mostrarCitas"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 overflow-y-auto">
      <div
        class="bg-white rounded-xl shadow-2xl p-6 w-full max-w-md mx-4 transform transition-all duration-300 ease-in-out">
        <h2 class="text-2xl font-bold text-gray-900 mb-6 text-center border-b-2 border-blue-200 pb-2">Próximas Citas
        </h2>
        <div v-if="citas.length" class="space-y-4 max-h-[70vh] overflow-y-auto pr-2">
          <div v-for="cita in citas" :key="cita.id"
            class="p-4 bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-md hover:shadow-lg transition">
            <h3 class="text-lg font-semibold text-gray-800">{{ cita.medico }}</h3>
            <p class="text-gray-600">{{ cita.especialidad }}</p>
            <p class="text-gray-600">{{ cita.fecha }} - {{ cita.hora }}</p>
            <div class="mt-4 flex justify-between gap-2">
              <button @click="verDetalles(cita)"
                class="px-4 py-2 bg-[#004AAD] text-white rounded-lg hover:bg-blue-600 transition flex-1">Detalles</button>
              <button @click="reagendarCita(cita)"
                class="px-4 py-2 bg-[#0A999D] text-white rounded-lg hover:bg-blue-600 transition flex-1">Reagendar</button>
            </div>
          </div>
        </div>
        <div v-else class="text-gray-500 text-center py-4">No tienes citas programadas.</div>
        <button @click="mostrarCitas = false"
          class="mt-6 w-full px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition">Cerrar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const mostrarCitas = ref(false);
const mostrarMedicos = ref(false);
const mostrarFormularioAgenda = ref(false);
const especialidadSeleccionada = ref("");
const medicoSeleccionado = ref({});
const nuevaCita = ref({
  codigoCita: "CITA-" + Math.floor(Math.random() * 10000),
  motivo: "",
});
const especialidades = ref([]);
const medicos = ref([]);

const citas = ref([
  { id: 1, medico: "Dr. Juan Pérez", especialidad: "Cardiología", fecha: "2025-09-25", hora: "10:00 AM" },
  { id: 2, medico: "Dra. Ana López", especialidad: "Ginecología", fecha: "2025-09-26", hora: "2:00 PM" },
]);

// Cargar especialidades dinámicamente
onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8001/api/Especialidads");
    const data = await response.json();
    if (response.ok) {
      especialidades.value = data.especialidades.map((esp) => ({
        nombre: esp.nombre,
        icono: "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z",
      }));
    } else {
      console.error("Error al cargar especialidades:", data);
    }
  } catch (error) {
    console.error("Error de conexión:", error);
  }
});

// Cargar medicos dinámicamente
onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8001/api/Medicos");
    const data = await response.json();
    if (response.ok) {
      medicos.value = data.medicos.map((medico) => ({
        numero_inss: medico.numero_inss,
        nombre_1: medico.nombre_1,
        apellido_1: medico.apellido_1,
        especialidad: medico.Especialidad,
        disponible: medico.disponible,
      }));
      console.log(medicos.value);
    } else {
      console.error("Error al cargar médicos:", data);
    }
  } catch (error) {
    console.error("Error de conexión:", error);
  }
});

const abrirMedicosEspecialidad = (especialidad) => {
  especialidadSeleccionada.value = especialidad;
  mostrarMedicos.value = true;
  mostrarFormularioAgenda.value = false;
  medicos.value = [];
  
};

const abrirFormularioAgenda = (medico) => {
  medicoSeleccionado.value = medico;
  nuevaCita.value.codigoCita = "CITA-" + Math.floor(Math.random() * 10000);
  nuevaCita.value.motivo = "";
  mostrarMedicos.value = false;
  mostrarFormularioAgenda.value = true;
};

const agendarCita = () => {
  const nuevaCitaAgendada = {
    id: citas.value.length + 1,
    medico: medicoSeleccionado.value.nombre,
    especialidad: especialidadSeleccionada.value,
    fecha: "2025-10-01",
    hora: "09:00 AM",
  };
  citas.value.push(nuevaCitaAgendada);
  mostrarFormularioAgenda.value = false;
};

const verDetalles = (cita) => {
  console.log("Ver detalles de:", cita);
};

const reagendarCita = (cita) => {
  console.log("Reagendar cita:", cita);
};
</script>

<style scoped>
/* Ajustes para responsividad en pantallas comunes */
.cont-principal {
  min-height: 100vh;
  padding-bottom: 60px;
}

.cont-especialidades {
  min-height: 100vh;
  overflow-y: auto;
}

.btn-spe {
  width: 100%;
  text-align: left;
}

/* Móviles (320px-640px) */
@media (max-width: 640px) {
  .w-12 {
    width: 1rem;
    height: 1rem;
  }

  .text-2xl {
    font-size: 1.5rem;
  }

  .text-lg {
    font-size: 1rem;
  }

  .max-w-md {
    max-width: 100%;
  }

  .lg:w-80 {
    width: 100%;
  }

  .p-4 {
    padding: 0.5rem;
  }

  .space-x-4>* {
    margin-left: 0.5rem;
  }

  .flex-1 {
    width: 100%;
  }

  .h-dvh {
    height: auto;
  }
}

/* Tablets (641px-1024px) */
@media (min-width: 641px) and (max-width: 1024px) {
  .container {
    max-width: 90%;
  }

  .lg:w-80 {
    width: 50%;
  }

  .text-2xl {
    font-size: 1.75rem;
  }

  .text-lg {
    font-size: 1.1rem;
  }

  .max-w-md {
    max-width: 80%;
  }
}

/* Laptops (1025px-1440px) */
@media (min-width: 1025px) and (max-width: 1440px) {
  .container {
    max-width: 80%;
  }

  .lg:w-80 {
    width: 20rem;
  }

  .text-2xl {
    font-size: 2rem;
  }

  .text-lg {
    font-size: 1.2rem;
  }

  .max-w-md {
    max-width: 60%;
  }
}

/* Desktops (1441px+) */
@media (min-width: 1441px) {
  .container {
    max-width: 1200px;
  }

  .lg:w-80 {
    width: 20%;
  }

  .text-2xl {
    font-size: 2.5rem;
  }

  .text-lg {
    font-size: 1.5rem;
  }

  .max-w-md {
    max-width: 50%;
  }
}

/* Ajustes generales para modal y promociones */
.max-h-\[70vh\] {
  max-height: 70vh;
}

.overflow-y-auto {
  -webkit-overflow-scrolling: touch;
}

.promociones {
  -webkit-overflow-scrolling: touch;
}

.promociones::-webkit-scrollbar {
  display: none;
}

.h-dvh {
  height: 100vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
</style>