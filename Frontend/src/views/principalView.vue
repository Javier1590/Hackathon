
<!-- src/components/Dashboard.vue -->
<template>
  <div class="min-h-screen bg-gray-100 font-sans relative">
    <!-- Encabezado Fijo -->
    <header class="fixed top-0 left-0 right-0 bg-white shadow-md z-10">
      <div class="container mx-auto px-4 py-3 flex items-center justify-between">
        <!-- Logo -->
        <div class="flex items-center">
          LOGO
        </div>
        <!-- Barra de búsqueda -->
        <div class="flex-1 mx-4 max-w-md">
          <input type="text" placeholder="Buscar médicos o especialidades..."
            class="w-full px-4 py-2 rounded-full border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Buscar médicos o especialidades" />
        </div>
        <!-- Íconos de usuario -->
        <div class="flex items-center space-x-4">
          img user
          <!-- Ícono de calendario para citas -->
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

    <!-- Contenido Principal -->
    <main class="container mx-auto px-4 pt-20 pb-16 flex flex-col lg:flex-row gap-6">
      <!-- Sidebar Izquierda: Especialidades Médicas (fija/sticky) -->
      <aside class="lg:sticky lg:top-20 lg:self-start w-64 lg:w-64 cont-especialidades h-dvh">
        <h2 class="text-2xl font-semibold text-gray-800 mb-4 text-center">Especialidades</h2>
        <div class="space-y-4">
          <button v-for="especialidad in especialidades" :key="especialidad.nombre"
            class="flex items-center p-4 rounded-lg shadow hover:shadow-lg transition w-full btn-spe" 
            @click="verMedicos(especialidad.nombre)" :aria-label="'Ver médicos de ' + especialidad.nombre">
            <svg class="w-8 h-8 text-white mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="especialidad.icono" />
            </svg>
            <span class="text-lg font-medium">{{ especialidad.nombre }}</span>
          </button>
        </div>
      </aside>

      <!-- Contenido Principal (vacío por ahora, para otros aspectos) -->
      <section class="flex-1">
        <!-- Placeholder para otros aspectos (ej. resumen de salud, noticias) -->
        <div class="p-6 bg-white rounded-lg shadow text-gray-600 text-center">
          Aquí puedes agregar más contenido como resumen de salud o noticias.
        </div>
      </section>
    </main>

    <!-- Sección Inferior: Promociones (fuera de main, deslizable) -->
    <div class="fixed bottom-0 left-0 right-0 bg-white shadow-md p-2 z-10 overflow-x-auto whitespace-nowrap">
      <div class="flex space-x-4 py-2">
        <div v-for="promocion in promociones" :key="promocion.titulo"
          class="inline-block w-48 p-2 bg-gray-50 rounded-lg shadow-sm text-sm text-gray-700">
          <img :src="promocion.imagen" :alt="promocion.titulo"
            class="w-12 h-12 object-cover rounded mr-2 inline-block" />
          <div class="inline-block align-middle">
            <h3 class="font-medium">{{ promocion.titulo }}</h3>
            <p class="text-xs">{{ promocion.descripcion }}</p>
          </div>
        </div>
      </div>
    </div>

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
                class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition flex-1">Detalles</button>
              <button @click="reagendarCita(cita)"
                class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition flex-1">Reagendar</button>
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

<script>
export default {
  data() {
    return {
      mostrarCitas: false,
      especialidades: [
        { nombre: 'Cardiología', icono: 'M5.414 11.414L12 4.828l6.586 6.586A2 2 0 0116.172 14H7.828a2 2 0 01-2.414-2.586z' },
        { nombre: 'Ginecología', icono: 'M12 4a8 8 0 100 16 8 8 0 000-16zm0 10a2 2 0 110-4 2 2 0 010 4z' },
        { nombre: 'Psicología', icono: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14a6 6 0 00-6 6c0 1.66.67 3.16 1.76 4.24l1.42-1.42C8.45 10.55 8 9.27 8 8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 1.27-.45 2.55-1.18 3.82l1.42 1.42C17.33 11.16 18 9.66 18 8a6 6 0 00-6-6z' },
        { nombre: 'Cardiología', icono: 'M5.414 11.414L12 4.828l6.586 6.586A2 2 0 0116.172 14H7.828a2 2 0 01-2.414-2.586z' },
        { nombre: 'Ginecología', icono: 'M12 4a8 8 0 100 16 8 8 0 000-16zm0 10a2 2 0 110-4 2 2 0 010 4z' },
        { nombre: 'Psicología', icono: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14a6 6 0 00-6 6c0 1.66.67 3.16 1.76 4.24l1.42-1.42C8.45 10.55 8 9.27 8 8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 1.27-.45 2.55-1.18 3.82l1.42 1.42C17.33 11.16 18 9.66 18 8a6 6 0 00-6-6z' },
        { nombre: 'Pediatría', icono: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2h-2zm0-4a1 1 0 011 1v2a1 1 0 11-2 0v-2a1 1 0 011-1zm0-4a1 1 0 10-2 0v2a1 1 0 102 0v-2z' },
      ],
      citas: [
        { id: 1, medico: 'Dr. Juan Pérez', especialidad: 'Cardiología', fecha: '2025-09-25', hora: '10:00 AM' },
        { id: 2, medico: 'Dra. Ana López', especialidad: 'Ginecología', fecha: '2025-09-26', hora: '2:00 PM' },
      ],
      promociones: [
        { titulo: 'Descuento en chequeo de rutina', descripcion: '20% de descuento.', imagen: '/promo1.jpg' },
        { titulo: 'Nueva especialidad disponible', descripcion: 'Psiquiatría ahora.', imagen: '/promo2.jpg' },
      ],
    };
  },
  methods: {
    verMedicos(especialidad) {
      console.log(`Ver médicos de ${especialidad}`);
    },
    verDetalles(cita) {
      console.log('Ver detalles de:', cita);
      // Lógica para mostrar detalles (ej. modal secundario o redirección)
    },
    reagendarCita(cita) {
      console.log('Reagendar cita:', cita);
      // Lógica para abrir formulario de reagendamiento
    },
  },
};
</script>


<style scoped>
/* Ajustes para carousel manual/automatico */
.promociones {
  -webkit-overflow-scrolling: touch;
  /* Suavidad en móvil */
}

.promociones::-webkit-scrollbar {
  display: none;
  /* Ocultar scrollbar en WebKit */
}
</style>