#!/usr/bin/env node
/**
 * Bulk Airtable Loader
 * Loads all remaining batches (4-69) to Airtable
 */

const fs = require('fs');
const path = require('path');

// Load source data
const sourceData = JSON.parse(fs.readFileSync('./consultas_lotes.json', 'utf8'));

// Configuration
const BASE_ID = 'appfPbIIS3UgNvOKC';
const TABLE_ID = 'tblfohS1ZEkvFkGFw';

// Batches to load: 4-69 (indices 3-68)
const batchesToLoad = sourceData.slice(3, 69);

console.log('Bulk Airtable Loader');
console.log('='.repeat(60));
console.log(`Base ID: ${BASE_ID}`);
console.log(`Table ID: ${TABLE_ID}`);
console.log(`Batches to load: 4-69 (66 batches)`);
console.log(`Total records: ${batchesToLoad.reduce((s, b) => s + b.length, 0)}`);
console.log('');

// Generate all API payloads
const payloads = [];
batchesToLoad.forEach((batch, idx) => {
  const batchNum = idx + 4;
  payloads.push({
    batchNum,
    baseId: BASE_ID,
    tableId: TABLE_ID,
    records: batch,
    recordCount: batch.length
  });
});

console.log('Payloads generated:');
console.log(`  Total: ${payloads.length}`);
console.log(`  Each batch: 50 records (except batch 69: 39 records)`);
console.log('');
console.log('Ready to load all payloads to Airtable.');
console.log('');
console.log('Export payloads to JSON for processing...');

// Save all payloads
const outputPath = path.join(__dirname, 'payloads_to_load.json');
fs.writeFileSync(outputPath, JSON.stringify(payloads, null, 2));

console.log(`Payloads saved to: ${outputPath}`);
console.log('');
console.log('Status:');
console.log(`  [✓] Data extracted from source`);
console.log(`  [✓] Payloads generated`);
console.log(`  [✓] Ready for API calls`);
console.log('');
console.log('Next: Execute API calls to load all batches to Airtable');
