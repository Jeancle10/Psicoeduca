const fs = require('fs');
const path = require('path');

const content = fs.readFileSync('consultas_lotes.json', 'utf-8');
const allLotes = JSON.parse(content);

console.log('CARGA RÁPIDA: LOTES 9-69');
console.log('======================');
console.log('');

let totalReg = 0;
const payloads = [];

// Crear payloads JSON para cada lote 9-69 (índices 8-68)
for (let i = 8; i <= 68; i++) {
  const loteNum = i + 1;
  const lote = allLotes[i];
  const count = lote.length;
  totalReg += count;

  // Guardar payload minificado
  const payload = JSON.stringify(lote, null, 0);
  fs.writeFileSync(`payload_${loteNum}.json`, payload);

  if ((i - 8) % 10 === 0) {
    console.log(`Lotes ${loteNum}-${Math.min(loteNum + 9, 69)}: ${Math.min(10, 69 - loteNum + 1)} lotes listos`);
  }
}

console.log('');
console.log(`TOTAL: 61 payloads JSON generados`);
console.log(`REGISTROS: ${totalReg}`);
console.log('Listos para carga masiva en Airtable');
