// Script automático para cargar todos los lotes a Airtable
// Este archivo contiene todas las instrucciones necesarias para hacer las llamadas API

const cargas = [
  {
    numeroLote: 32,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 33,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 34,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 35,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 36,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 37,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 38,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 39,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 40,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 41,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 42,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 43,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 44,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 45,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 46,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 47,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 48,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 49,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 50,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 51,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 52,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 53,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 54,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 55,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 56,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 57,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 58,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 59,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 60,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 61,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 62,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 63,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 64,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 65,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 66,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 67,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 68,
    cantidad: 50,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  },
  {
    numeroLote: 69,
    cantidad: 39,
    baseId: "appfPbIIS3UgNvOKC",
    tableId: "tblfohS1ZEkvFkGFw"
  }

];

console.log('Total de llamadas a hacer: ' + cargas.length);
cargas.forEach(c => {
  console.log(`Lote ${c.numeroLote}: ${c.cantidad} registros`);
});
