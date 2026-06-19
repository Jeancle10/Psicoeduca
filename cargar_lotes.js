const fs = require('fs');

// Leer JSON
const data = JSON.parse(fs.readFileSync('consultas_lotes.json', 'utf8'));

// Extraer lotes 9-69 (índices 8-68)
const lotesACargar = [];
for (let i = 8; i < 69; i++) {
  const numeroLote = i + 1;
  const lote = data[i];
  lotesACargar.push({
    numeroLote,
    registros: lote,
    cantidad: lote.length
  });
}

// Generar comandos para cargador (será ejecutado por herramienta externa)
console.log('LOTES A CARGAR:');
console.log('===============');
lotesACargar.forEach(lote => {
  console.log(`Lote ${lote.numeroLote}: ${lote.cantidad} registros`);
});

console.log('');
console.log(`Total: ${lotesACargar.length} lotes`);
console.log(`Total registros: ${lotesACargar.reduce((sum, l) => sum + l.cantidad, 0)}`);

// Exportar para uso en otros scripts
fs.writeFileSync('lotes_9_69_data.json', JSON.stringify(lotesACargar, null, 2));
console.log('');
console.log('Datos exportados a lotes_9_69_data.json');
