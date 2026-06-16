// API Client para PsicoEduca
// Detecta automáticamente la URL base

const API_BASE = (() => {
  // En producción, usa el dominio actual
  if (window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
    return `https://${window.location.hostname}`;
  }
  // En desarrollo, conecta a localhost:5000
  return 'http://localhost:5000';
})();

console.log('API_BASE:', API_BASE);

// Mostrar alertas
function showAlert(message, type = 'info') {
  const alertContainer = document.getElementById('alert-container');
  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${type}`;
  alertDiv.textContent = message;
  alertContainer.appendChild(alertDiv);

  setTimeout(() => {
    alertDiv.remove();
  }, 4000);
}

// Listar consultantes
async function getConsultantes(nombre = '', edadMin = null, edadMax = null) {
  try {
    let url = `${API_BASE}/api/consultantes/`;
    const params = new URLSearchParams();
    if (nombre) params.append('nombre', nombre);
    if (edadMin) params.append('edad_min', edadMin);
    if (edadMax) params.append('edad_max', edadMax);

    if (params.toString()) url += '?' + params.toString();

    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching consultantes:', error);
    showAlert('Error al cargar consultantes', 'error');
    return [];
  }
}

// Obtener consultante específico
async function getConsultante(id) {
  try {
    const response = await fetch(`${API_BASE}/api/consultantes/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching consultante:', error);
    return null;
  }
}

// Crear consultante
async function createConsultante(data) {
  try {
    const response = await fetch(`${API_BASE}/api/consultantes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error creating consultante:', error);
    throw error;
  }
}

// Crear evaluación
async function createEvaluacion(consultanteId, respuestas) {
  try {
    const response = await fetch(`${API_BASE}/api/evaluaciones/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        consultante_id: consultanteId,
        respuestas: respuestas
      })
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    console.error('Error creating evaluacion:', error);
    throw error;
  }
}

// Obtener evaluaciones de un consultante
async function getEvaluacionesConsultante(consultanteId) {
  try {
    const response = await fetch(`${API_BASE}/api/evaluaciones/${consultanteId}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching evaluaciones:', error);
    return [];
  }
}

// Obtener comparativa temporal
async function getComparativaConsultante(consultanteId) {
  try {
    const response = await fetch(`${API_BASE}/api/resultados/comparativa/${consultanteId}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching comparativa:', error);
    return null;
  }
}

// Obtener estadísticas generales
async function getEstadisticas() {
  try {
    const response = await fetch(`${API_BASE}/api/resultados/estadisticas`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching estadisticas:', error);
    return null;
  }
}
