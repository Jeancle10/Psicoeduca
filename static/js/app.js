// Estado global
let currentStep = 1;
let currentConsultanteId = null;
let chartTemporal = null;

// Preguntas de cada test
const PREGUNTAS = {
  stai: [
    "Me siento calmado/a",
    "Me siento seguro/a",
    "Estoy tenso/a",
    "Me siento angustiado/a",
    "Estoy relajado/a",
    "Estoy preocupado/a",
    "Me siento tranquilo/a",
    "Me siento ansioso/a",
    "Me siento confiado/a",
    "Me siento nervioso/a",
    "Estoy desasosegado/a",
    "Me siento bien",
    "Estoy asustado/a",
    "Me siento cómodo/a",
    "Tengo confianza en mí mismo",
    "Me siento indeciso/a",
    "Estoy relajado/a",
    "Me siento satisfecho/a",
    "Me preocupan los posibles desastres",
    "Me siento feliz" // P23
  ],
  bdi: [
    "Tristeza",
    "Pesimismo",
    "Sentimiento de fracaso",
    "Pérdida de placer",
    "Sentimientos de culpa",
    "Sentimiento de castigo",
    "Disconformidad con uno mismo",
    "Auto-crítica",
    "Pensamientos suicidas",
    "Llanto",
    "Agitación",
    "Pérdida de interés",
    "Indecisión",
    "Sensación de inutilidad",
    "Pérdida de energía",
    "Cambios en los patrones de sueño",
    "Irritabilidad",
    "Cambios de apetito",
    "Dificultad de concentración",
    "Cansancio o fatiga",
    "Pérdida de interés en el sexo" // P66
  ],
  bfi: [
    "Es tímido, reservado",
    "Es conversador, extrovertido",
    "Es original, ideador",
    "Es considerado, amable",
    "Es minucioso, organizado"
  ],
  scl90Items: 64 // Items 72-135
};

// Inicializar cuando carga la página
document.addEventListener('DOMContentLoaded', () => {
  setupNavigation();
  loadDashboard();
  generateQuestionnaires();
});

// Setup navegación
function setupNavigation() {
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const section = btn.dataset.section;
      showSection(section);
    });
  });
}

// Mostrar sección
function showSection(sectionId) {
  // Actualizar botones
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  event.target.classList.add('active');

  // Mostrar sección
  document.querySelectorAll('.section').forEach(section => {
    section.classList.remove('active');
  });
  document.getElementById(sectionId).classList.add('active');

  // Cargar datos específicos
  if (sectionId === 'resultados') {
    loadResultadosSection();
  }
}

// Cargar dashboard
async function loadDashboard() {
  const consultantes = await getConsultantes();
  renderConsultantesTable(consultantes);
  loadConsultantesSelect();
  loadResultadosSelect();
}

// Renderizar tabla de consultantes
function renderConsultantesTable(consultantes) {
  const tbody = document.getElementById('consultantes-tbody');
  tbody.innerHTML = '';

  if (consultantes.length === 0) {
    tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; padding: 40px;">No hay consultantes registrados</td></tr>';
    return;
  }

  consultantes.forEach(c => {
    const row = tbody.insertRow();
    row.innerHTML = `
      <td><strong>${c.nombre} ${c.apellido}</strong></td>
      <td>${c.edad}</td>
      <td>${c.celular}</td>
      <td>${c.email || '—'}</td>
      <td><span style="background: #e0f7ff; padding: 4px 8px; border-radius: 4px;">${c.total_evaluaciones}</span></td>
      <td>
        <button class="btn-view" onclick="viewConsultante(${c.id})">Ver</button>
      </td>
    `;
  });
}

// Filtrar consultantes
async function filtrarConsultantes() {
  const nombre = document.getElementById('filter-nombre').value;
  const edadMin = document.getElementById('filter-edad-min').value || null;
  const edadMax = document.getElementById('filter-edad-max').value || null;

  const consultantes = await getConsultantes(nombre, edadMin, edadMax);
  renderConsultantesTable(consultantes);
}

// Ver consultante
async function viewConsultante(id) {
  const consultante = await getConsultante(id);
  if (!consultante) return;

  const evaluaciones = consultante.evaluaciones || [];
  alert(`
${consultante.nombre} ${consultante.apellido}
Edad: ${consultante.edad} años
Celular: ${consultante.celular}
Email: ${consultante.email || 'N/A'}
Evaluaciones: ${evaluaciones.length}
  `.trim());
}

// Cargar selects
async function loadConsultantesSelect() {
  const consultantes = await getConsultantes();
  const select = document.getElementById('consultante-select');
  select.innerHTML = '<option value="">Seleccionar...</option>';
  consultantes.forEach(c => {
    const option = document.createElement('option');
    option.value = c.id;
    option.textContent = `${c.nombre} ${c.apellido} (${c.edad} años)`;
    select.appendChild(option);
  });
}

async function loadResultadosSelect() {
  const consultantes = await getConsultantes();
  const select = document.getElementById('consultante-resultados');
  select.innerHTML = '<option value="">Seleccionar consultante...</option>';
  consultantes.forEach(c => {
    const option = document.createElement('option');
    option.value = c.id;
    option.textContent = `${c.nombre} ${c.apellido}`;
    select.appendChild(option);
  });
}

// Toggle consultante existente
function toggleConsultanteExistente() {
  const select = document.getElementById('consultante-existente').value;
  const group = document.getElementById('consultantes-select-group');
  group.style.display = select === 'si' ? 'block' : 'none';
}

// Generar formularios
function generateQuestionnaires() {
  // STAI (40 preguntas)
  const staiContainer = document.getElementById('stai-questions');
  staiContainer.innerHTML = '';

  // STAI Estado (P4-P23, índices 0-19)
  const staiEstadoDiv = document.createElement('div');
  staiEstadoDiv.innerHTML = '<h4 style="color: #667eea; margin-bottom: 15px;">Sección A: Estado de Ansiedad Actual</h4>';
  for (let i = 0; i < 20; i++) {
    const q = PREGUNTAS.stai[i];
    const p = 4 + i;
    staiEstadoDiv.appendChild(createQuestion(p, `${p}. ${q}`, 'scale', [0, 1, 2, 3]));
  }
  staiContainer.appendChild(staiEstadoDiv);

  // STAI Rasgo (P24-P43, índices 20-39)
  const staiRasgoDiv = document.createElement('div');
  staiRasgoDiv.innerHTML = '<h4 style="color: #667eea; margin: 20px 0 15px 0;">Sección B: Ansiedad Habitual</h4>';
  for (let i = 20; i < 40; i++) {
    const q = PREGUNTAS.stai[i - 20];
    const p = 24 + (i - 20);
    staiRasgoDiv.appendChild(createQuestion(p, `${p}. ${q}`, 'scale', [0, 1, 2, 3]));
  }
  staiContainer.appendChild(staiRasgoDiv);

  // BDI (23 preguntas)
  const bdiContainer = document.getElementById('bdi-questions');
  bdiContainer.innerHTML = '';
  for (let i = 0; i < 23; i++) {
    const q = PREGUNTAS.bdi[i];
    const p = 44 + i;
    bdiContainer.appendChild(createQuestion(p, `${p}. ${q}`, 'scale', [0, 1, 2, 3]));
  }

  // BFI-5 (5 preguntas)
  const bfiContainer = document.getElementById('bfi-questions');
  bfiContainer.innerHTML = '';
  const bfiLabels = [
    "Neuroticismo",
    "Extraversión",
    "Apertura",
    "Amabilidad",
    "Responsabilidad"
  ];
  for (let i = 0; i < 5; i++) {
    const p = 67 + i;
    bfiContainer.appendChild(createQuestion(p, `${p}. ${PREGUNTAS.bfi[i]}`, 'scale', [1, 2, 3, 4, 5]));
  }

  // SCL-90-R (64 preguntas)
  const scl90Container = document.getElementById('scl90-questions');
  scl90Container.innerHTML = '';
  const scl90Labels = [
    "¿Dolores de cabeza?",
    "Nerviosismo o agitación",
    "Pensamientos indeseables",
    "Desmayos o vértigos",
    "Pérdida de interés sexual",
    "Crítica de ti mismo",
    "Culpa",
    "Falta de concentración",
    "Falta de apetito",
    "Dificultad para dormir",
    "Preocupación",
    "Facilidad para enfadarse",
    "Intranquilidad",
    "Tristeza",
    "Labilidad emocional",
    "Baja autoestima",
    "Sentimientos de inferioridad",
    "Pensamientos suicidas",
    "Alucinaciones",
    "Sensación de extrañeza",
    "Miedos u obsesiones",
    "Falta de energía",
    "Ideas de persecución",
    "Habla excesiva",
    "Dificultad para expresarse",
    "Dolores musculares",
    "Temblores",
    "Dolores de espalda",
    "Debilidad",
    "Mareos",
    "Palpitaciones",
    "Falta de aliento",
    "Dolores en el pecho",
    "Náuseas",
    "Molestias abdominales",
    "Trastornos digestivos",
    "Problemas para tragar",
    "Eructos",
    "Sensación de ardor",
    "Molestias abdominales",
    "Inflamación abdominal",
    "Constipación",
    "Diarrea",
    "Intolerancia alimentaria",
    "Dolor menstrual",
    "Irregularidad menstrual",
    "Sangrado menstrual excesivo",
    "Problemas sexuales",
    "Indiferencia sexual",
    "Miedo a los lugares abiertos",
    "Miedo a los viajes",
    "Ansiedad en la multitud",
    "Timidez",
    "Facilidad para asustarse",
    "Poca confianza en ti mismo",
    "Perfeccionismo excesivo",
    "Sentimiento de culpa",
    "Insomnio inicial",
    "Insomnio intermedio",
    "Insomnio terminal",
    "Sueño excesivo",
    "Despertar temprano",
    "Sueño inquieto",
    "Fatiga por las mañanas",
    "Falta de energía durante el día"
  ];

  for (let i = 0; i < 64; i++) {
    const p = 72 + i;
    const label = scl90Labels[i] || `Pregunta ${p}`;
    scl90Container.appendChild(createQuestion(p, `${p}. ${label}`, 'scale', [0, 1, 2, 3, 4]));
  }
}

// Crear elemento de pregunta
function createQuestion(id, label, type, options) {
  const div = document.createElement('div');
  div.className = 'question-group';

  if (type === 'scale') {
    div.innerHTML = `<label>${label}</label><div class="scale-options" id="scale-${id}"></div>`;
    const scaleDiv = div.querySelector(`#scale-${id}`);

    options.forEach(opt => {
      const label_elem = document.createElement('label');
      label_elem.innerHTML = `<input type="radio" name="p${id}" value="${opt}"> ${opt}`;
      scaleDiv.appendChild(label_elem);
    });
  }

  return div;
}

// Navegación de steps
function nextStep(step) {
  if (validateStep(currentStep)) {
    currentStep = step;
    updateFormSteps();
  }
}

function prevStep(step) {
  currentStep = step;
  updateFormSteps();
}

function updateFormSteps() {
  document.querySelectorAll('.form-step').forEach(step => {
    step.classList.remove('active');
  });
  document.querySelector(`[data-step="${currentStep}"]`).classList.add('active');

  // Actualizar progress bar
  const progress = (currentStep / 4) * 100;
  document.querySelector('.form-progress-bar').style.width = progress + '%';
}

// Validar step
function validateStep(step) {
  if (step === 1) {
    const nombre = document.getElementById('p1').value.trim();
    const fecha = document.getElementById('p2').value;
    const celular = document.getElementById('p3').value.trim();

    if (!nombre || !fecha || !celular) {
      showAlert('Por favor completa todos los campos obligatorios', 'error');
      return false;
    }

    // Validar fecha
    const age = new Date().getFullYear() - new Date(fecha).getFullYear();
    if (age < 13 || age > 120) {
      showAlert('Edad debe estar entre 13 y 120 años', 'error');
      return false;
    }
  }

  return true;
}

// Enviar formulario
async function submitForm() {
  if (!validateStep(4)) return;

  // Recopilar respuestas
  const respuestas = {};
  document.querySelectorAll('input[type="radio"]:checked').forEach(input => {
    respuestas[input.name] = input.value;
  });

  // Validar que todas las preguntas están respondidas
  const expectedQuestions = 4 + 20 + 20 + 23 + 5 + 64; // P4 a P135
  if (Object.keys(respuestas).length < expectedQuestions - 3) { // -3 por P1, P2, P3
    showAlert(`Por favor responde todas las preguntas (${Object.keys(respuestas).length}/${expectedQuestions - 3})`, 'error');
    return;
  }

  // Determinar consultante_id
  let consultanteId = currentConsultanteId;

  if (!consultanteId) {
    // Crear nuevo consultante
    try {
      const consultanteData = {
        nombre: document.getElementById('p1').value.trim(),
        apellido: '', // Podríamos parsear el nombre completo
        fecha_nacimiento: document.getElementById('p2').value,
        celular: document.getElementById('p3').value.trim(),
        email: document.getElementById('email').value.trim() || null
      };

      const nuevoConsultante = await createConsultante(consultanteData);
      consultanteId = nuevoConsultante.id;
      currentConsultanteId = consultanteId;
    } catch (error) {
      showAlert(`Error al crear consultante: ${error.message}`, 'error');
      return;
    }
  }

  // Crear evaluación
  try {
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'loading';
    loadingDiv.innerHTML = '<div class="spinner"></div><p>Procesando evaluación...</p>';
    document.querySelector('.form-section').appendChild(loadingDiv);

    const evaluacion = await createEvaluacion(consultanteId, respuestas);

    loadingDiv.remove();
    showAlert('✓ Evaluación registrada exitosamente', 'success');

    // Mostrar resultados
    setTimeout(() => {
      showResultados(evaluacion);
    }, 1000);
  } catch (error) {
    showAlert(`Error: ${error.message}`, 'error');
  }
}

// Mostrar resultados
function showResultados(evaluacion) {
  document.querySelector('[data-section="resultados"]').style.display = 'block';
  showSection('resultados');
  renderResultados(evaluacion);
}

// Cargar sección de resultados
async function loadResultadosSection() {
  const stats = await getEstadisticas();
  if (stats) {
    renderEstadisticas(stats);
  }
}

// Renderizar estadísticas generales
function renderEstadisticas(stats) {
  const grid = document.getElementById('estadisticas-grid');
  grid.innerHTML = `
    <div class="result-card">
      <h3>Evaluaciones Totales</h3>
      <div class="result-value">${stats.total_evaluaciones}</div>
    </div>
    <div class="result-card">
      <h3>Consultantes</h3>
      <div class="result-value">${stats.consultantes_evaluados}</div>
    </div>
    <div class="result-card">
      <h3>Promedio STAI</h3>
      <div class="result-value">${stats.promedios.stai_estado}</div>
      <div class="result-subtitle">Estado</div>
    </div>
    <div class="result-card">
      <h3>Promedio BDI</h3>
      <div class="result-value">${stats.promedios.bdi}</div>
      <div class="result-subtitle">Depresión</div>
    </div>
  `;
}

// Cargar resultados de consultante
async function cargarResultadosConsultante() {
  const id = document.getElementById('consultante-resultados').value;
  if (!id) return;

  const comparativa = await getComparativaConsultante(id);
  if (!comparativa) return;

  const consultante = comparativa.consultante;
  const evaluaciones = comparativa.evaluaciones;

  if (evaluaciones.length === 0) {
    document.getElementById('resultados-container').style.display = 'none';
    showAlert('Este consultante no tiene evaluaciones', 'info');
    return;
  }

  document.getElementById('resultados-container').style.display = 'block';
  document.getElementById('resultado-nombre').textContent = `${consultante.nombre} ${consultante.apellido}`;
  document.getElementById('resultado-fecha').textContent = `Última evaluación: ${new Date(evaluaciones[evaluaciones.length - 1].fecha).toLocaleDateString('es-AR')}`;

  // Gráfico temporal
  renderGraficoTemporal(evaluaciones);

  // Listado de evaluaciones
  renderEvaluacionesList(evaluaciones);
}

// Renderizar gráfico temporal
function renderGraficoTemporal(evaluaciones) {
  const ctx = document.getElementById('chart-temporal');
  if (!ctx) return;

  if (chartTemporal) {
    chartTemporal.destroy();
  }

  const fechas = evaluaciones.map(e => new Date(e.fecha).toLocaleDateString('es-AR'));
  const staiEstado = evaluaciones.map(e => e.stai_estado);
  const bdi = evaluaciones.map(e => e.bdi);
  const scl90 = evaluaciones.map(e => e.scl90);

  chartTemporal = new Chart(ctx, {
    type: 'line',
    data: {
      labels: fechas,
      datasets: [
        {
          label: 'STAI Estado',
          data: staiEstado,
          borderColor: '#667eea',
          tension: 0.4,
          fill: false
        },
        {
          label: 'BDI',
          data: bdi,
          borderColor: '#764ba2',
          tension: 0.4,
          fill: false
        },
        {
          label: 'SCL-90-R',
          data: scl90,
          borderColor: '#ff6b6b',
          tension: 0.4,
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top'
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

// Renderizar listado de evaluaciones
function renderEvaluacionesList(evaluaciones) {
  const list = document.getElementById('evaluaciones-list');
  list.innerHTML = '';

  evaluaciones.reverse().forEach(e => {
    const div = document.createElement('div');
    div.style.padding = '15px';
    div.style.borderBottom = '1px solid #eee';
    div.innerHTML = `
      <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
        <strong>${new Date(e.fecha).toLocaleDateString('es-AR')}</strong>
        <small style="color: #666;">${new Date(e.fecha).toLocaleTimeString('es-AR')}</small>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 13px;">
        <div>STAI Estado: <strong>${e.stai_estado}</strong></div>
        <div>BDI: <strong>${e.bdi}</strong></div>
        <div>SCL-90-R: <strong>${e.scl90}</strong></div>
      </div>
    `;
    list.appendChild(div);
  });
}

// Renderizar resultados de una evaluación
function renderResultados(evaluacion) {
  const grid = document.getElementById('resultados-grid');
  grid.innerHTML = `
    <div class="result-card">
      <h3>STAI - Estado</h3>
      <div class="result-value">${evaluacion.stai_estado.puntuacion}</div>
      <div class="result-subtitle">Percentil: ${evaluacion.stai_estado.percentil}</div>
      <div class="result-category category-${evaluacion.stai_estado.categoria.toLowerCase()}">${evaluacion.stai_estado.categoria}</div>
    </div>

    <div class="result-card">
      <h3>STAI - Rasgo</h3>
      <div class="result-value">${evaluacion.stai_rasgo.puntuacion}</div>
      <div class="result-subtitle">Percentil: ${evaluacion.stai_rasgo.percentil}</div>
      <div class="result-category category-${evaluacion.stai_rasgo.categoria.toLowerCase()}">${evaluacion.stai_rasgo.categoria}</div>
    </div>

    <div class="result-card">
      <h3>BDI</h3>
      <div class="result-value">${evaluacion.bdi.puntuacion}</div>
      <div class="result-subtitle">Depresión</div>
      <div class="result-category category-${evaluacion.bdi.categoria.toLowerCase().replace(/\s+/g, '-')}">${evaluacion.bdi.categoria}</div>
    </div>

    <div class="result-card">
      <h3>BFI-5</h3>
      <div style="font-size: 12px; line-height: 1.8;">
        Neuroticismo: <strong>${evaluacion.bfi.neuroticismo}/5</strong><br>
        Extraversión: <strong>${evaluacion.bfi.extraversion}/5</strong><br>
        Apertura: <strong>${evaluacion.bfi.apertura}/5</strong><br>
        Amabilidad: <strong>${evaluacion.bfi.amabilidad}/5</strong><br>
        Responsabilidad: <strong>${evaluacion.bfi.responsabilidad}/5</strong>
      </div>
    </div>

    <div class="result-card">
      <h3>SCL-90-R</h3>
      <div class="result-value">${evaluacion.scl90.puntuacion}</div>
      <div class="result-subtitle">Síntomas</div>
      <div class="result-category category-${evaluacion.scl90.categoria.toLowerCase()}">${evaluacion.scl90.categoria}</div>
    </div>
  `;
}
