import json
import subprocess
import sys

# Configuración
BASE_ID = 'appfPbIIS3UgNvOKC'
TABLE_ID = 'tblfohS1ZEkvFkGFw'

# Cargar todos los batches
records = []
for i in range(10):
    batch_file = f'C:\Users\MI PC\psicoeduca\batch_33_42_{i:02d}.json'
    with open(batch_file, 'r') as f:
        batch = json.load(f)
        if isinstance(batch, list):
            records.extend(batch)
        else:
            records.append(batch)

print(f'Total registros a cargar: {len(records)}')

# Crear comando para cada batch de 50
for batch_idx in range(0, len(records), 50):
    batch_records = records[batch_idx:batch_idx+50]
    
    # Crear el JSON para la llamada
    cmd = [
        'npx', 'claude-mcp',
        'call', 'mcp__claude_ai_Airtable__create_records_for_table',
        '--input', json.dumps({
            'baseId': BASE_ID,
            'tableId': TABLE_ID,
            'records': batch_records
        })
    ]
    
    print(f'Batch {batch_idx//50}: {len(batch_records)} registros')

print('Script listo para ejecución manual.')
