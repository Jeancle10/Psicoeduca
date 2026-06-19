const fs = require('fs');

const content = fs.readFileSync('consultas_lotes.json', 'utf-8');
const allLotes = JSON.parse(content);

for (let i = 6; i <= 68; i++) {
  const loteNum = i + 1;
  const lote = allLotes[i];
  const outFile = `lote_${loteNum}.json`;
  fs.writeFileSync(outFile, JSON.stringify(lote, null, 0));
  console.log(`Guardado: ${outFile} (${lote.length} registros)`);
}
