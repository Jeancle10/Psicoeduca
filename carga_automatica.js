const fs = require('fs');

// Script de carga automatizada para Airtable
console.log('=================================================');
console.log('SCRIPT DE CARGA AUTOMATICA - LOTES 9-69');
console.log('=================================================');
console.log('');

const baseId = 'appfPbIIS3UgNvOKC';
const tableId = 'tblfohS1ZEkvFkGFw';

// Función para generar comando de carga
function generarComandoCarga(numeroLote, datos) {
  return {
    lote: numeroLote,
    cantidad: datos.length,
    comando: `mcp__claude_ai_Airtable__create_records_for_table`,
    baseId: baseId,
    tableId: tableId,
    registros: datos
  };
}

// Procesar todos los lotes
const comandos = [];
let totalRegistros = 0;

for (let i = 9; i <= 69; i++) {
  try {
    const dataPath = `lote${i}_data.json`;
    if (fs.existsSync(dataPath)) {
      const datos = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
      const cmd = generarComandoCarga(i, datos);
      comandos.push(cmd);
      totalRegistros += datos.length;
      
      if (i % 10 === 0) {
        console.log(`✓ Lote ${i} preparado (${datos.length} registros)`);
      }
    }
  } catch (e) {
    console.error(`✗ Error en lote ${i}: ${e.message}`);
  }
}

console.log('');
console.log(`Total de lotes preparados: ${comandos.length}`);
console.log(`Total de registros: ${totalRegistros}`);
console.log('');

// Guardar comandos para referencia
fs.writeFileSync('comandos_carga.json', JSON.stringify({
  total_lotes: comandos.length,
  total_registros: totalRegistros,
  baseId: baseId,
  tableId: tableId,
  lotes: comandos.map(cmd => ({lote: cmd.lote, cantidad: cmd.cantidad}))
}, null, 2));

console.log('LOTES LISTOS PARA CARGAR EN AIRTABLE:');
console.log('======================================');
comandos.forEach(cmd => {
  console.log(`Lote ${cmd.lote}: ${cmd.cantidad} registros`);
});

console.log('');
console.log('Comando guardado en comandos_carga.json');
console.log('');
console.log('ESTADO ACTUAL:');
console.log('- Lotes 7-8: CARGADO (100 registros)');
console.log(`- Lotes 9-69: PENDIENTE (${totalRegistros} registros)`);
console.log(`- TOTAL ESPERADO: ${totalRegistros + 100} registros`);
