#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Leer el archivo de lotes
const filePath = path.join(__dirname, 'consultas_lotes.json');
const content = fs.readFileSync(filePath, 'utf-8');
const allLotes = JSON.parse(content);

console.log('=== ANÁLISIS DE LOTES PARA CARGA ===');
console.log(`Total de lotes en archivo: ${allLotes.length}`);
console.log('');

// Generar los comandos para cargar lotes 7-69 (índices 6-68)
const cargas = [];
for (let i = 6; i <= 68; i++) {
  const loteNum = i + 1;
  const lote = allLotes[i];
  const recordCount = Array.isArray(lote) ? lote.length : 1;

  cargas.push({
    loteNum,
    index: i,
    recordCount,
    records: lote
  });
}

console.log(`Lotes a cargar: ${cargas.length}`);
console.log(`Rango: Lote ${cargas[0].loteNum} a Lote ${cargas[cargas.length - 1].loteNum}`);
console.log('');

// Mostrar resumen de registros por lote
let totalRegistros = 0;
for (let j = 0; j < Math.min(10, cargas.length); j++) {
  console.log(`Lote ${cargas[j].loteNum}: ${cargas[j].recordCount} registros`);
  totalRegistros += cargas[j].recordCount;
}
console.log('...');
for (let j = Math.max(0, cargas.length - 3); j < cargas.length; j++) {
  console.log(`Lote ${cargas[j].loteNum}: ${cargas[j].recordCount} registros`);
}

console.log('');
// Contar total de registros
totalRegistros = cargas.reduce((sum, c) => sum + c.recordCount, 0);
console.log(`Total de registros a cargar: ${totalRegistros}`);

// Guardar en un archivo para referencia
const output = {
  totalLotes: cargas.length,
  totalRegistros,
  lotes: cargas.map(c => ({
    loteNum: c.loteNum,
    recordCount: c.recordCount
  }))
};

fs.writeFileSync(
  path.join(__dirname, 'cargas_info.json'),
  JSON.stringify(output, null, 2)
);

console.log('Información guardada en cargas_info.json');
console.log('');
console.log('Ahora llamar a Airtable API para cada lote...');
