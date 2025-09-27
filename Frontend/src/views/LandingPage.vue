<!-- src/views/LandingPage.vue -->
<template>
  <div class="min-h-screen bg-gray-100 font-sans text-gray-900">
    <!-- Hero Section -->
    <header class=" text-white py-16 px-4 text-center encabezado">
      <img src="../assets/Logo Full Color.png" alt="Logo Life PX" class="mx-auto h-20 w-auto mb-4" />
      <h1 class="text-4xl font-bold mb-2">Life PX - Portal de Salud Digital</h1>
      <p class="text-xl mb-6">Tu cita médica, sin filas ni esperas. Plataforma digital para gestionar citas, agendas y expedientes clínicos en Nicaragua.</p>
      <div class="space-x-4">
        <router-link to="/login" class="btn-reg px-6 py-3  rounded-lg font-semibold hover:bg-gray-100 transition" aria-label="Registrarse como paciente">Registrarse</router-link>
        <router-link to="/login" class="btn-new px-6 py-3  rounded-lg font-semibold hover:bg-blue-900 transition" aria-label="Iniciar sesión">Iniciar Sesión</router-link>
      </div>
    </header>

    <!-- Descripción y Problemática -->
    <section class="py-12 px-4 container mx-auto">
      <h2 class="text-3xl font-bold text-center mb-8">Descripción del Proyecto</h2>
      <p class="text-lg mb-4">La plataforma Life PX es una solución digital de atención médica en línea que permite a los pacientes registrarse, gestionar sus agendas y solicitar citas médicas. Además, gestiona expedientes clínicos y envía notificaciones. Enfocada en Nicaragua, dirigida a la población general.</p>
      <h3 class="text-2xl font-semibold mb-4">Problemática</h3>
      <p class="text-lg mb-4">La falta de gestión digital en los procesos de atención médica hospitalaria en Nicaragua genera retrasos, duplicidad de registros y pérdida de información. Los procedimientos manuales con papel causan ineficiencia en la asignación y administración de citas.</p>
    </section>

    <!-- Solución Propuesta -->
    <section class="py-12 px-4 bg-gray-200 container mx-auto">
      <h2 class="text-3xl font-bold text-center mb-8">Solución Propuesta</h2>
      <p class="text-lg mb-4">Una plataforma digital que reemplaza procesos manuales, eliminando el uso de papel y reduciendo la carga administrativa. Los pacientes acceden rápidamente a citas, evitando filas; los hospitales mejoran eficiencia y trazabilidad.</p>
      <p class="text-lg mb-4">En definitiva, Life PX transforma un proceso lento en un servicio moderno, eficiente y escalable, elevando la calidad de la atención médica.</p>
    </section>

    <!-- Funcionalidades Clave -->
    <section class="py-12 px-4 container mx-auto">
      <h2 class="text-3xl font-bold text-center mb-8">Funcionalidades Clave</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-6 bg-white rounded-lg shadow-md">
          <h3 class="text-xl font-semibold mb-2">Para Pacientes</h3>
          <ul class="list-disc pl-5 text-lg">
            <li>Gestión de agendas y citas medicas.</li>
            <li>Notificaciones de solicitudes de citas.</li>
            <li>Gestión de expedientes clínicos.</li>
          </ul>
        </div>
        <div class="p-6 bg-white rounded-lg shadow-md">
          <h3 class="text-xl font-semibold mb-2">Para Médicos</h3>
          <ul class="list-disc pl-5 text-lg">
            <li>Gestión de agendas y citas de pacientes.</li>
            <li>Notificaciones de solicitudes de citas.</li>
            <li>Gestión de expedientes clínicos.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Justificación y Análisis -->
    <section class="py-12 px-4 bg-gray-200 container mx-auto">
      <h2 class="text-3xl font-bold text-center mb-8">Justificación del Sistema</h2>
      <p class="text-lg mb-4">La gestión de citas y seguimiento en Nicaragua enfrenta desafíos geográficos y logísticos. En zonas rurales, agendar citas implica costos altos en transporte y riesgos para la salud. La comunicación posterior es limitada, llevando a dudas no resueltas.</p>
      <h3 class="text-2xl font-semibold mb-4">Análisis de la Problemática</h3>
      <p class="text-lg mb-4">Barreras como transporte incómodo, ausencias médicas imprevistas y dependencia de apps de terceros agravan el acceso. Sin un sistema centralizado, los pacientes viajan en vano.</p>
    </section>

    <!-- Objetivos e Impacto -->
    <section class="py-12 px-4 container mx-auto">
      <h2 class="text-3xl font-bold text-center mb-8">Objetivos e Impacto Esperado</h2>
      <h3 class="text-2xl font-semibold mb-4">Objetivos</h3>
      <ul class="list-disc pl-5 text-lg mb-6">
        <li>Optimizar gestión de agendas médicas.</li>
        <li>Mejorar experiencia del paciente y reducir burocracia.</li>
        <li>Facilitar comunicación proactiva y reducir viajes innecesarios.</li>
        <li>Modernizar administración de citas.</li>
      </ul>
      <h3 class="text-2xl font-semibold mb-4">Impacto Esperado</h3>
      <p class="text-lg mb-4">Para pacientes: equidad, accesibilidad y empoderamiento. Para personal médico: eficiencia operativa, toma de decisiones informada y reducción de aglomeraciones.</p>
    </section>

    <!-- Call-to-Action Footer -->
    <footer class=" text-white py-8 px-4 text-center">
      <h2 class="text-2xl font-bold mb-4">Únete a Life PX y transforma la salud en Nicaragua</h2>
      <router-link to="/login" class="px-6 py-3 btn-new2 text-white rounded-lg font-semibold hover:bg-gray-100 transition" aria-label="Comenzar ahora">Comenzar Ahora</router-link>
      <p class="mt-4 text-sm">UNMRMA CUR Chontales, Equipo Nicazúl 2025. Todos los Derechos Reservados.</p>
    </footer>
  </div>
</template>

<script>
export default {
  // Puedes agregar lógica aquí si necesitas, como redirecciones dinámicas
};
</script>
<style scoped>
/* Ajustes específicos para responsividad en pantallas comunes */
@media (max-width: 640px) { /* Móviles (ej. 320px-640px) */
  .text-4xl { font-size: 2rem; }
  .text-xl { font-size: 1rem; }
  .text-lg { font-size: 0.9rem; }
  .h-24 { height: 16px; } /* Ajuste del logo para móviles pequeños */
  .px-6 { padding-left: 1rem; padding-right: 1rem; }
  .py-3 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
  .space-x-4 > * { margin-left: 0.5rem; }
  .grid-cols-1 { grid-template-columns: 1fr; }
}

@media (min-width: 641px) and (max-width: 1024px) { /* Tablets (641px-1024px) */
  .text-4xl { font-size: 2.5rem; }
  .text-xl { font-size: 1.2rem; }
  .text-lg { font-size: 1rem; }
  .container { max-width: 90%; }
  .grid-cols-2 { grid-template-columns: 1fr; } /* Apila funcionalidades en tablet */
}

@media (min-width: 1025px) and (max-width: 1440px) { /* Laptops (1025px-1440px) */
  .container { max-width: 80%; }
  .grid-cols-2 { grid-template-columns: 1fr 1fr; } /* Restaura columnas */
  .text-3xl { font-size: 2rem; }
}

@media (min-width: 1441px) { /* Desktops (1440px+) */
  .container { max-width: 1200px; }
  .text-4xl { font-size: 3rem; }
  .text-xl { font-size: 1.5rem; }
  .h-24 { height: 28px; } /* Logo más grande en desktops */
}

/* Ajustes generales para suavidad y scroll */
html {
  scroll-behavior: smooth;
}
.container {
  max-width: 100%;
  padding-left: 1rem;
  padding-right: 1rem;
}
.btn-reg, .btn-new, .btn-new2 {
  background: #004AAD;
}
</style>